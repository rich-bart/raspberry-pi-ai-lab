# Train a Random Forest

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** A fair comparison of at least two forest sizes.  
**Learning goals:** Understand voting across trees and how model parameters change performance.

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

Use a classroom voting analogy: one decision tree vs many trees. Students run a 10-tree forest then a 100-tree forest; compare accuracy and elapsed time by observation. Show how `random_state=42` makes repeated tests comparable. Explore `max-depth`. Save individual result folders.

## Command(s) to practice

```bash
python3 student/04_random_forest.py --trees 10 --out results/forest10
python3 student/04_random_forest.py --trees 100 --out results/forest100
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Run two provided commands and record clean accuracy.
- **Independent:** Try 10, 50 and 100 trees; describe pattern and tradeoff.
- **Stretch:** Vary max depth while holding tree count fixed; justify a choice for future tests.

## Exit question

Is more complexity always better? How can we make experiments fair?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
