# Raspberry Pi AI Lab

**Build a computer → connect to a private wired network → collect datasets → train AI → test it → improve it.**

An **8-session, offline-first high-school STEM curriculum** for a classroom of approximately 10–20 students with mixed coding experience. Each meeting lasts two hours; the plan assumes **30–40 minutes for arrivals** and about **80–90 usable minutes**. There are **2 optional extension sessions**.

> **No router, Wi-Fi, or classroom Internet required.** One teacher Raspberry Pi and all student Pis connect to an **unmanaged Ethernet switch**. The teacher Pi assigns local IPs, serves datasets over SSH, and keeps challenge answers private. All training runs on each student's own Pi.

## Start here

- **Instructor:** [Preflight and preparation](docs/instructor-setup.md) → [Wired switch networking](docs/wired-network.md) → [teacher checklist](docs/instructor-checklist.md).
- **Student:** [Quick start](docs/student-quickstart.md) → [Session 1](lessons/01-build-your-computer.md).
- **Purchasing:** [Hardware list](docs/hardware.md).
- **If something breaks:** [Offline troubleshooting](docs/troubleshooting.md).
- **Publish on GitHub:** [Publishing guide](docs/publishing-to-github.md).
- **Final challenge:** [Capstone and grading](docs/capstone.md).

## Schedule

| Session | Topic | Take-home checkpoint |
|---|---|---|
| [01](lessons/01-build-your-computer.md) | Assemble and boot a Raspberry Pi | Working computer |
| [02](lessons/02-linux-python.md) | Navigate Linux and run Python | First working script |
| [03](lessons/03-ethernet-ssh-scp.md) | Ethernet, IP, SSH, SCP | Data copied from instructor Pi |
| [04](lessons/04-understand-data.md) | Pixels, labels and train/test sets | Saved digit image |
| [05](lessons/05-decision-tree.md) | Decision tree classification | Baseline model and matrix |
| [06](lessons/06-random-forest.md) | Random forests and tuning | Comparison of settings |
| [07](lessons/07-break-the-ai.md) | Noise, shift and generalization | Three confusion matrices |
| [08](lessons/08-capstone.md) | Team capstone | Predictions, results and presentation |
| [Optional 09](lessons/09-python-bridge.md) | Python skills bridge | Edited working Python code |
| [Optional 10](lessons/10-augmentation-ethics.md) | Training data and responsible AI | Augmentation experiment |

**Session rhythm:** 35 min arrivals / 10 min review / 15 min new concept / 45 min guided lab / 10 min reflection / 5 min save and cleanup. The lab supports **Guided / Independent / Stretch** paths so the pace is not dictated by the most advanced students.

## Example code workflow

Scripts require Python 3 and Raspberry Pi OS versions of `numpy`, `pandas`, `scikit-learn`, and `matplotlib` installed **before** going offline.

```bash
# TEACHER: run once, with scikit-learn already installed
python3 teacher/prepare_datasets.py
# TEACHER: copy generated public CSVs to read-only /srv/ai-lab

# STUDENT: after copying the datasets into ./data from the teacher Pi
python3 student/02_view_digits.py --data data/test_clean.csv
python3 student/03_decision_tree.py --max-depth 6
python3 student/04_random_forest.py --trees 100
python3 student/04_random_forest.py --trees 10 --out results/forest10
python3 student/04_random_forest.py --train data/train_augmented.csv --out results/augmented
```

The student scripts produce accuracy summaries, confusion matrices and CSV metrics in `results/` (ignored by Git). Never train on `test_*.csv`—they are held-out evaluations.

## Repo map

```text
raspberry-pi-ai-lab/
├── docs/            Instructor/student setup, network, troubleshooting, grading
├── lessons/         Eight full sessions and two optional sessions
├── teacher/         Dataset generator and private-answer scoring tool
├── student/         Graduated Python experiments and helper functions
├── tests/           Offline pipeline integrity checks
├── data/            Generated locally, ignored by Git
├── .github/workflows/ci.yml
└── requirements.txt
```

## Classroom preparation (important)

1. Assemble and pre-image **all** SD cards with Raspberry Pi OS Desktop 64-bit, unique student accounts, SSH client, and the Python packages; copy `student/` scripts and lesson docs onto every student Pi.
2. On the master Pi, configure **static Ethernet IP `192.168.50.1`**, an isolated DHCP service, and a dedicated **non-admin** `classroom` account with read-only access to public data.
3. Run `teacher/prepare_datasets.py`; share `data/public/` files only. Keep `data/private/` on the instructor Pi. Release `challenge_features.csv` only at the capstone.
4. Verify the entire exercise with **one student Pi before students arrive**. Never connect the switch to the school LAN.

No cloud model, GPU, API key, GitHub login, or Internet connection is needed during class. A GitHub repository is for **pre-class preparation**; the students use local copies when offline.

## Privacy, safety and scientific integrity

- Use a dedicated SSH account, never the teacher's administrator login. Prefer per-student credentials or individual keys if required by school policy; the shared demonstration account is for an **isolated, supervised** switch only.
- The dataset is from `sklearn.datasets.load_digits`: **1,797** 8×8 grayscale digits. This is educational supervised learning, **not** a ChatGPT-like language model.
- Only training data is used for training and augmentation; clean/noisy/shifted test versions derive from held-out identities, and final challenge identities are separated before any training.
- A hidden challenge assembled from a public dataset and reproducible code is a useful classroom exercise, **not a secure high-stakes exam**.
- Student predictions should be stored under pseudonymous team IDs; avoid collecting personal information.

Code and educational materials: [MIT license](LICENSE). Documentation is supplied as classroom teaching material and is adaptable.
