"""Session 7: compare separate experiments using their generated summary files."""
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('summary_files', nargs='+', help='results/.../summary.csv paths')
args = parser.parse_args()
rows = []
for path in args.summary_files:
    frame = pd.read_csv(path)
    frame.insert(0, 'experiment', path)
    rows.append(frame)
print(pd.concat(rows, ignore_index=True).to_string(index=False, float_format=lambda x: f'{x:.3f}'))
