# Break the AI: Noise and Shifts

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** Three confusion matrices and a written finding.  
**Learning goals:** Explain accuracy vs generalization and discover how distribution shift hurts predictions.

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

Students examine `confusion_test_clean.png`, `confusion_test_noisy.png`, and `confusion_test_shifted.png` from one run. Each student writes a hypothesis for which test is hardest, compares scores, and identifies confusing digit pairs. Run the augmented training experiment, then compare two summary CSVs.

## Command(s) to practice

```bash
python3 student/04_random_forest.py --out results/baseline
python3 student/04_random_forest.py --train data/train_augmented.csv --out results/augmented
python3 student/05_compare_results.py results/baseline/summary.csv results/augmented/summary.csv
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Find the lowest score and highlight one off-diagonal cell.
- **Independent:** Explain why augmentation changes noisy-test performance more than shifted-test performance.
- **Stretch:** Propose a different augmentation for pixel shifts while keeping test images held out.

## Exit question

Which failure surprised you? Could this matter for a real-world medical or engineering AI?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
