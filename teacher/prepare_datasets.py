"""Create separate train/public test/hidden holdout splits from sklearn digits.

Public files go to data/public. NEVER copy data/private/challenge_answers.csv
into the classroom SSH share or a public git repository.
"""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

FEATURES = [f'pixel_{i:02d}' for i in range(64)]


def save_labeled(path, X, y):
    path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(X, columns=FEATURES)
    df['digit'] = y.astype(int)
    df.to_csv(path, index=False)
    print(f'Created {path}: {len(df)} examples')


def make_data(root, seed=42):
    public = root / 'public'
    private = root / 'private'
    public.mkdir(parents=True, exist_ok=True)
    private.mkdir(parents=True, exist_ok=True)
    X, y = load_digits(return_X_y=True)
    # First reserve 15% of original images for the challenge. These never
    # appear in training or any of the public evaluation files.
    pool_X, hidden_X, pool_y, hidden_y = train_test_split(
        X, y, test_size=0.15, random_state=23, stratify=y)
    train_X, test_X, train_y, test_y = train_test_split(
        pool_X, pool_y, test_size=0.30, random_state=42, stratify=pool_y)
    rng = np.random.default_rng(seed)
    noisy_train = np.clip(train_X + rng.normal(0, 3, train_X.shape), 0, 16)
    noisy_test = np.clip(test_X + rng.normal(0, 4, test_X.shape), 0, 16)
    shifted = np.zeros_like(test_X.reshape(-1, 8, 8))
    shifted[:, :, 1:] = test_X.reshape(-1, 8, 8)[:, :, :-1]
    # Use separate hidden identities; different noise from public tests.
    hidden_aug = np.clip(hidden_X + rng.normal(0, 2, hidden_X.shape), 0, 16)
    save_labeled(public / 'train_clean.csv', train_X, train_y)
    save_labeled(public / 'train_augmented.csv',
                 np.vstack([train_X, noisy_train]), np.concatenate([train_y, train_y]))
    save_labeled(public / 'test_clean.csv', test_X, test_y)
    save_labeled(public / 'test_noisy.csv', noisy_test, test_y)
    save_labeled(public / 'test_shifted.csv', shifted.reshape(-1, 64), test_y)
    ids = [f'H{i:04d}' for i in range(len(hidden_y))]
    challenge = pd.DataFrame(hidden_aug, columns=FEATURES)
    challenge.insert(0, 'sample_id', ids)
    challenge.to_csv(private / 'challenge_features.csv', index=False)
    pd.DataFrame({'sample_id': ids, 'digit': hidden_y}).to_csv(
        private / 'challenge_answers.csv', index=False)
    print('Challenge feature CSV generated; answers saved privately and NOT shared.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=Path('data'))
    parser.add_argument('--seed', type=int, default=42,
                        help='Seed for noise generation; write down to reproduce your class')
    args = parser.parse_args()
    make_data(args.out, seed=args.seed)
