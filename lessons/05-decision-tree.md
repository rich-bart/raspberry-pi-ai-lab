# Train Your First AI: Decision Tree

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** A trained model and confusion matrix.  
**Learning goals:** Explain a tree split, training and predictions; identify diagonal entries of a confusion matrix.

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

Play a yes/no guessing game with the class. Explain how a tree asks feature questions. Students run a Decision Tree at maximum depth 6 and open the confusion matrix. Re-run at depth 2 and 12, keeping the test file unchanged. Record scores and a hypothesis.

## Command(s) to practice

```bash
python3 student/03_decision_tree.py --max-depth 6
--max-depth 2 --out results/tree2
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Run the prepared tree code and point to one correct/incorrect cell.
- **Independent:** Change maximum depth and explain why score changes.
- **Stretch:** Compare very shallow vs deep trees; discuss overfitting.

## Exit question

Why might a deeper tree memorize training examples but fail on new ones?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
