"""Sessions 6–7: train on one dataset, evaluate on THREE held-out challenges."""
import argparse
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from common import load_labeled, save_matrix

parser = argparse.ArgumentParser()
parser.add_argument('--train', type=Path, default=Path('data/train_clean.csv'))
parser.add_argument('--data-dir', type=Path, default=Path('data'))
parser.add_argument('--trees', type=int, default=100)
parser.add_argument('--max-depth', type=int, default=None)
parser.add_argument('--out', type=Path, default=Path('results/forest'))
args = parser.parse_args()
if args.trees < 1 or (args.max_depth is not None and args.max_depth < 1):
    parser.error('--trees and --max-depth must be positive numbers')

train_X, train_y = load_labeled(args.train)
forest = RandomForestClassifier(n_estimators=args.trees, max_depth=args.max_depth,
                                random_state=42, n_jobs=1)
forest.fit(train_X, train_y)
args.out.mkdir(parents=True, exist_ok=True)
rows = []
for case in ['test_clean', 'test_noisy', 'test_shifted']:
    test_X, test_y = load_labeled(args.data_dir / f'{case}.csv')
    guesses = forest.predict(test_X)
    accuracy = accuracy_score(test_y, guesses)
    print(f'{case:>13}: {accuracy:.1%} correct')
    save_matrix(test_y, guesses, args.out / f'confusion_{case}.png',
                f'{case}: {args.trees} trees, {args.train.stem}')
    rows.append(dict(train=args.train.name, trees=args.trees, max_depth=args.max_depth,
                     dataset=case, accuracy=accuracy,
                     balanced_accuracy=balanced_accuracy_score(test_y, guesses)))
pd.DataFrame(rows).to_csv(args.out / 'summary.csv', index=False)
print(f'Check the graphs and summary.csv inside {args.out}')
