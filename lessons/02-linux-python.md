# Learn Linux and Python

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** A Python program that runs locally.  
**Learning goals:** Understand folder navigation, terminal commands and how Python scripts run.

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

Demonstrate opening a terminal. Explore `pwd`, `ls`, `mkdir`, and `cd`; explain the home folder and a file path. Run `python3 student/01_hello.py` from the preloaded `~/ai-lab` folder. Each student changes the greeting or prints another line; no network required.

## Command(s) to practice

```bash
cd ~/ai-lab && python3 student/01_hello.py
~/ai-lab/notes
mkdir -p
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Copy provided commands and change a string.
- **Independent:** Use a `for` loop to print five steps and explain what `range` means.
- **Stretch:** Add a safe input prompt that branches on a student-selected number.

## Exit question

Why is a precise file path important? What happens when Python cannot find the script?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
