# Optional: Better Training Data and Responsible AI

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** Results table and discussion of responsible evaluation.  
**Learning goals:** Interpret data augmentation and reflect on limits of supervised learning.

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

Show a distorted image and ask whether a human can still recognize it. Students compare `train_clean.csv` with `train_augmented.csv` in the forest. Ask who/what is represented by the dataset and how deployment conditions might differ. Optionally discuss privacy, fair evaluation, and reporting failures. Place this session before Session 8.

## Command(s) to practice

```bash
python3 student/04_random_forest.py --train data/train_augmented.csv --out results/augmented
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Run augmentation test and describe where performance improved.
- **Independent:** Write a controlled experiment holding parameters and test files constant.
- **Stretch:** Propose a new training transformation and discuss whether it might harm accuracy elsewhere.

## Exit question

Why might a model tested on one type of handwriting fail on another?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
