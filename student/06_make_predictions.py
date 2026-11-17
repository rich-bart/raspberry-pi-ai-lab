"""Session 8: predict hidden challenge features; no true labels are provided."""
import argparse
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from common import PIXELS, load_labeled

parser = argparse.ArgumentParser()
parser.add_argument('--train', type=Path, default=Path('data/train_clean.csv'))
parser.add_argument('--features', type=Path, default=Path('data/challenge_features.csv'))
parser.add_argument('--output', type=Path, default=Path('submissions/team01.csv'))
parser.add_argument('--trees', type=int, default=100)
parser.add_argument('--max-depth', type=int, default=None)
args = parser.parse_args()
if args.trees < 1 or (args.max_depth is not None and args.max_depth < 1):
    parser.error('--trees and --max-depth must be positive')
X_train, y_train = load_labeled(args.train)
challenge = pd.read_csv(args.features)
if list(challenge.columns) != ['sample_id'] + PIXELS:
    raise ValueError('challenge must have sample_id then pixel_00..pixel_63')
if challenge.empty or challenge['sample_id'].duplicated().any() or challenge.isna().any().any():
    raise ValueError('challenge contains duplicate sample IDs, missing values, or no samples')
forest = RandomForestClassifier(n_estimators=args.trees, max_depth=args.max_depth,
                                random_state=42, n_jobs=1)
forest.fit(X_train, y_train)
preds = forest.predict(challenge[PIXELS])
args.output.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame({'sample_id': challenge['sample_id'], 'prediction': preds}).to_csv(args.output, index=False)
print(f'Wrote {len(preds)} predictions to {args.output} (no answers exposed)')
