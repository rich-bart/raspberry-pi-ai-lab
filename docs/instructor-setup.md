# Instructor preflight: 8-session course

**Before the program:** test one complete CanaKit, monitor, Ethernet cable and Pi power supply; install 64-bit Raspberry Pi OS Desktop; set unique hostnames; give each student their own login. Have spares and a locally stored image of a known-good SD card. Label stations 01–20.

**At a location with Internet (prior to class), on every Pi:**

```bash
sudo apt update
sudo apt install -y python3-numpy python3-pandas python3-sklearn python3-matplotlib \
  openssh-client
python3 -c 'import numpy, pandas, sklearn, matplotlib; print("Python AI packages ready")'
```

On teacher Pi, also install `openssh-server dnsmasq`. Packages from Raspberry Pi OS's distro repositories avoid virtualenv requirements for a beginner workshop. Copy this repo's **student/**, **lessons/** and **docs/** directories onto each student SD card at `~/ai-lab/` beforehand (USB drive, cloned SD-card image, or temporary Internet before the workshop). Leave `~/ai-lab/data/` empty for the SSH lesson. No Internet is used in class. Do not assume students can `git clone` when offline.

1. Follow [isolated switch setup](wired-network.md).
2. On the teacher Pi, from the root of this repo: `python3 teacher/prepare_datasets.py`. It produces `data/public/*.csv` and `data/private/` instructor-only files.
3. Share **only public** CSVs: `sudo cp data/public/*.csv /srv/ai-lab/`; set `root:root`, directory `755`, files `644`.
4. Keep the teacher-only `data/private/challenge_answers.csv` completely private. Do not share or commit it. On capstone day, publish only `data/private/challenge_features.csv` by copying it to `/srv/ai-lab/challenge_features.csv`.
5. Run `python3 -m unittest discover -s tests -v` on the teacher Pi after generating data.
6. From a student Pi, test SSH, SCP, the sample visualizer, a tree model and random forest. See [student quick start](student-quickstart.md).
7. Set up a projector/printed handouts, USB fallback data copies, optional mentor roles, and a paper attendance checklist.

**Classroom day:** 35 min admission/setup, 10 min review, 15 min concept, 45 min labs, 10 min reflection, 5 min save and cleanup. Leave time for troubleshooting; don't reset the entire class to help one station.

**Mixed skills:** each lesson has Guided (working provided commands), Independent (change variables and explain behavior), and Stretch (deeper extension). A confident partner can assist but each student should run their own code. Assign numbered stations for logistics. See [assessment rubric](assessment.md).

## Main gotchas

- Switch ≠ router: without master Pi DHCP, students may have no useful IP addresses.
- Pi 5 uses **micro-HDMI for video**, not the USB-C power input.
- Offline devices need Python libraries installed **before** arrival.
- Reproducible training/testing data should **never be mixed**. The final challenge uses **separate held-out examples**.
- Training a Random Forest on a Pi is fast enough at this dataset size; no cloud or GPU.
- `joblib`/pickle model files are **not** submitted or loaded by the teacher; students submit **prediction CSVs**. Never load serialized models from untrusted participants.
