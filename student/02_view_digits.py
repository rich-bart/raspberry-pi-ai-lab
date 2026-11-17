"""Session 4: turn rows of 64 pixel numbers into handwritten-digit pictures."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common import PIXELS, load_labeled

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=Path, default=Path('data/test_clean.csv'))
parser.add_argument('--out', type=Path, default=Path('results/digit_examples.png'))
args = parser.parse_args()
features, labels = load_labeled(args.data)
fig, axes = plt.subplots(3, 4, figsize=(9, 6))
for index, axis in enumerate(axes.flat):
    pixels = features.iloc[index][PIXELS].to_numpy(dtype=float)
    axis.imshow(pixels.reshape(8, 8), cmap='gray_r', vmin=0, vmax=16)
    axis.set_title(f'True digit: {labels.iloc[index]}')
    axis.axis('off')
fig.tight_layout()
args.out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(args.out, dpi=130)
plt.close(fig)
print(f'Saved {args.out} — open it in the file manager')
