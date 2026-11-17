# Student quick start

Welcome! You will make a computer, connect it by Ethernet to your instructor's computer, train a number-recognizing AI, then try to break it.

**After the teacher has preloaded the code** and you have connected your Ethernet cable:

```bash
cd ~/ai-lab
ip -4 addr show eth0
ping -c 3 192.168.50.1
ssh classroom@192.168.50.1
ls /srv/ai-lab
exit
mkdir -p data
scp classroom@192.168.50.1:'/srv/ai-lab/*.csv' data/
ls data
```

The teacher will provide the SSH password. **Type it carefully:** terminals typically do not display password characters. Never type the instructor's own login password.

**Try the AI:**

```bash
python3 student/02_view_digits.py --data data/test_clean.csv
python3 student/03_decision_tree.py
python3 student/04_random_forest.py
```

Look in `results/`: `summary.csv` and `confusion_*.png` show accuracy and mistakes. If the scripts aren't installed or the CSV files aren't found, ask your instructor for the preloaded folder or see [Troubleshooting](troubleshooting.md).

**Two rules:** training files teach the AI; testing files examine the AI. Never let a testing file leak into training. Don't share accounts, passwords, or classmate information.

**Vocabulary:** `ssh` = remote terminal; `scp` = secure copy between computers; feature = measurement; label = answer; classifier = predicts labels; confusion matrix = table of predicted vs actual labels.
