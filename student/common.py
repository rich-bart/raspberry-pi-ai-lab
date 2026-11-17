"""Small reusable helpers. Students can inspect this after the guided exercises."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

PIXELS = [f'pixel_{i:02d}' for i in range(64)]
LABELS = list(range(10))


def load_labeled(path):
    path = Path(path)
    frame = pd.read_csv(path)
    expected = PIXELS + ['digit']
    if list(frame.columns) != expected:
        raise ValueError(f'{path}: expected 64 pixel columns followed by digit label')
    if frame.empty or frame[PIXELS].isna().any().any() or frame['digit'].isna().any():
        raise ValueError(f'{path}: missing or empty data')
    if not frame['digit'].isin(LABELS).all():
        raise ValueError(f'{path}: digit must be in 0..9')
    return frame[PIXELS], frame['digit'].astype(int)


def save_matrix(y_true, y_pred, path, title):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    matrix = confusion_matrix(y_true, y_pred, labels=LABELS)
    view = ConfusionMatrixDisplay(matrix, display_labels=LABELS)
    view.plot(cmap='Blues', values_format='d', colorbar=False)
    view.ax_.set_title(title)
    view.figure_.set_size_inches(7, 6)
    view.figure_.tight_layout()
    view.figure_.savefig(path, dpi=120)
    plt.close(view.figure_)
    return matrix
