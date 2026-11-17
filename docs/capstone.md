# Capstone: sealed challenge (Session 8)

The teacher generated a **third, independent holdout split** and has not published its answer labels. On Session 8 only, copy its features to the master SSH share:

```bash
sudo cp data/private/challenge_features.csv /srv/ai-lab/
sudo chown root:root /srv/ai-lab/challenge_features.csv
sudo chmod 644 /srv/ai-lab/challenge_features.csv
```

Student downloads only the feature file:

```bash
cd ~/ai-lab
scp classroom@192.168.50.1:/srv/ai-lab/challenge_features.csv data/
python3 student/06_make_predictions.py \
  --features data/challenge_features.csv \
  --output submissions/team07.csv \
  --train data/train_clean.csv --trees 100
```

The student script writes `sample_id,prediction` to `submissions/team07.csv` **without** needing answer labels. For team comparisons, allow tuning with *public training/test sets*, not challenge answer labels. Each team should preserve a test-results log and explain its choice.

**Collect results:** Use an instructor-controlled USB transfer or an approved per-student local handoff. Avoid asking the teacher Pi to unpickle student-created model files. Do not publish the key or accept arbitrary executable code as a submission.

On the **teacher Pi** (after copying student CSVs into `submissions/`):

```bash
python3 teacher/score_challenge.py \
  --answers data/private/challenge_answers.csv \
  --predictions submissions/team07.csv \
  --out results/team07
```

Output: exact accuracy, integer confusion matrix and a PNG heatmap. Missing IDs, duplicate IDs, invalid digits or wrong headers are rejected rather than silently counted as zero.

The instructor can reveal a summary score at the end, then discuss where the model failed. **Important:** the source handwritten digits dataset is public and the holdout split is reproducible; this is a pedagogical withheld dataset, not a tamper-proof high-stakes benchmark.
