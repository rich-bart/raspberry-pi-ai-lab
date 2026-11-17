"""Check split sizes, file schema and that a small model works offline."""
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'teacher'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'student'))
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from prepare_datasets import FEATURES, make_data
from common import load_labeled


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        make_data(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_public_schema_and_counts(self):
        train_x, train_y = load_labeled(self.root / 'public/train_clean.csv')
        test_x, test_y = load_labeled(self.root / 'public/test_clean.csv')
        self.assertEqual(train_x.shape[1], 64)
        self.assertEqual(test_x.shape[1], 64)
        self.assertGreater(len(train_y), 1000)
        self.assertGreater(len(test_y), 400)
        for suffix in ('noisy', 'shifted'):
            _, labels = load_labeled(self.root / f'public/test_{suffix}.csv')
            self.assertEqual(labels.tolist(), test_y.tolist())

    def test_training_and_hidden_are_different_identities(self):
        train_x, _ = load_labeled(self.root / 'public/train_clean.csv')
        test_x, _ = load_labeled(self.root / 'public/test_clean.csv')
        # Exact 8x8 raw digits are distinct across these two generated splits.
        self.assertFalse(set(map(tuple, train_x.to_numpy())) & set(map(tuple, test_x.to_numpy())))
        hidden = pd.read_csv(self.root / 'private/challenge_features.csv')
        answers = pd.read_csv(self.root / 'private/challenge_answers.csv')
        self.assertEqual(hidden.shape[0], len(answers))
        self.assertEqual(hidden.columns.tolist(), ['sample_id'] + FEATURES)
        self.assertEqual(hidden.sample_id.tolist(), answers.sample_id.tolist())
        self.assertNotIn('digit', hidden)

    def test_model_runs_on_pi_scale_data(self):
        train_x, train_y = load_labeled(self.root / 'public/train_clean.csv')
        test_x, test_y = load_labeled(self.root / 'public/test_clean.csv')
        classifier = RandomForestClassifier(n_estimators=10, random_state=42, n_jobs=1)
        classifier.fit(train_x, train_y)
        self.assertGreater(np.mean(classifier.predict(test_x) == test_y), 0.80)

if __name__ == '__main__':
    unittest.main()
