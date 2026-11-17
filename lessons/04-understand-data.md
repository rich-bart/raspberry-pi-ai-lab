# What Is Training Data?

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** A saved page of handwritten digits.  
**Learning goals:** Understand features (pixel measurements), labels, and the difference between training and evaluation.

## Instructor timing

| Time within session | Task |
|---|---|
| 0–35 min | Arrival, powering on, attendance, troubleshooting |
| 35–45 min | Review previous lesson / demo |
| 45–60 min | Introduce today's concept |
| 60–105 min | Guided hands-on lab and student challenges |
| 105–115 min | Share results; answer the reflection prompt |
| 115–120 min | Save work, turn off / tidy stations |

## Hands-on lab

Show an 8×8 grid and have students draw a simple digit by coloring squares. Each grayscale cell is one of 64 features; the label is the actual digit. Students inspect the `train_clean.csv` headers, then run the viewer to reconstruct pictures. Discuss why testing on training data gives an unrealistic score.

## Command(s) to practice

```bash
python3 student/02_view_digits.py --data data/test_clean.csv
results/digit_examples.png
head -n 2 data/train_clean.csv
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Match pictured digits to their labels and point out a single pixel feature.
- **Independent:** Count the rows in train and test files and explain why labels must be separate from features.
- **Stretch:** Predict what adding noise to pixel values might do before seeing test results.

## Exit question

Why should we keep some examples hidden while training? What is a feature?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
