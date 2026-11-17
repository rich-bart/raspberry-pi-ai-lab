# Capstone: The Sealed Test

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** Predictions CSV, score and short team presentation.  
**Learning goals:** Build a defensible model, predict withheld examples, interpret results and communicate findings.

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

Teacher first releases `challenge_features.csv` (no labels) from master. Student teams select training data and forest parameters based on their public experiments; submit prediction CSVs by the approved offline method. Instructor scores against private labels. Each team presents its hypothesis, experiment(s), one improvement and one limitation.

## Command(s) to practice

```bash
scp classroom@192.168.50.1:/srv/ai-lab/challenge_features.csv data/
python3 student/06_make_predictions.py --features data/challenge_features.csv --output submissions/team01.csv
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Use the given 100-tree script and explain what `prediction` means.
- **Independent:** Use augmented training data and compare to the clean model before choosing.
- **Stretch:** Design an evidence-based strategy while avoiding the hidden answers; explain possible failure modes.

## Exit question

Why is a score not enough to prove an AI is safe or reliable?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
