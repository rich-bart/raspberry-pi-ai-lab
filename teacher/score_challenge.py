"""Grade student prediction CSVs against private instructor labels, without pickle."""
import argparse
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score
# Import shared plotting tools without requiring installation of a package.
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'student'))
from common import save_matrix

parser = argparse.ArgumentParser()
parser.add_argument('--answers', type=Path, default=Path('data/private/challenge_answers.csv'))
parser.add_argument('--predictions', type=Path, required=True)
parser.add_argument('--out', type=Path, default=Path('results/challenge'))
args = parser.parse_args()
truth = pd.read_csv(args.answers)
guesses = pd.read_csv(args.predictions)
if truth.columns.tolist() != ['sample_id', 'digit'] or guesses.columns.tolist() != ['sample_id','prediction']:
    raise ValueError('Wrong headers: answers=sample_id,digit; predictions=sample_id,prediction')
if truth['sample_id'].duplicated().any() or guesses['sample_id'].duplicated().any():
    raise ValueError('Duplicate sample_id found')
if truth.isna().any().any() or guesses.isna().any().any():
    raise ValueError('Missing answers or predictions found')
if set(truth.sample_id) != set(guesses.sample_id):
    raise ValueError('Missing, extra, or incorrect sample IDs in predictions')
if not guesses.prediction.isin(range(10)).all():
    raise ValueError('Predictions must be integer digits 0 through 9')
joined = truth.merge(guesses, on='sample_id', validate='one_to_one', sort=False)
score = accuracy_score(joined.digit, joined.prediction)
args.out.mkdir(parents=True, exist_ok=True)
save_matrix(joined.digit, joined.prediction, args.out / 'confusion.png',
            f'Challenge: {args.predictions.stem} ({score:.1%})')
print(f'{args.predictions.name}: {score:.1%} correct on {len(joined)} examples')
print(f'Instructor-only results: {args.out / "confusion.png"}')
