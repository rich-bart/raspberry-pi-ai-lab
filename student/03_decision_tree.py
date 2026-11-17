"""Session 5: one decision tree. Evaluate using held-out clean examples only."""
import argparse
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from common import load_labeled, save_matrix

parser = argparse.ArgumentParser()
parser.add_argument('--train', type=Path, default=Path('data/train_clean.csv'))
parser.add_argument('--test', type=Path, default=Path('data/test_clean.csv'))
parser.add_argument('--max-depth', type=int, default=6)
parser.add_argument('--out', type=Path, default=Path('results/tree'))
args = parser.parse_args()
if args.max_depth is not None and args.max_depth < 1:
    parser.error('--max-depth must be at least 1')
X_train, y_train = load_labeled(args.train)
X_test, y_test = load_labeled(args.test)
model = DecisionTreeClassifier(max_depth=args.max_depth, random_state=42)
model.fit(X_train, y_train)
answers = model.predict(X_test)
score = accuracy_score(y_test, answers)
args.out.mkdir(parents=True, exist_ok=True)
save_matrix(y_test, answers, args.out / 'confusion.png', 'Decision Tree')
print(f'Decision Tree: {score:.1%} correct on {len(y_test)} unseen digits')
print(f'Wrote {args.out / "confusion.png"}')
