# Connect Computers: Ethernet, SSH and SCP

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** Own local copy of shared data.  
**Learning goals:** Identify the roles of a switch, IP address, server and client; use ping, SSH and SCP.

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

Instructor connects the switch to the master Pi and all student Ethernet cables. Students run `ip -4 addr show eth0` to read their DHCP address and `ping -c 3 192.168.50.1`. Instructor explains private switch and IP addresses, then demonstrates SSH login and `ls /srv/ai-lab`. Students exit and copy five CSV datasets with SCP.

## Command(s) to practice

```bash
ssh classroom@192.168.50.1
ls /srv/ai-lab
exit
mkdir -p data
scp classroom@192.168.50.1:'/srv/ai-lab/*.csv' data/
ls data
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Work from a printed command reference with explanations and teacher-provided account credentials.
- **Independent:** Explain the difference between `cp`, `scp` and `ssh`, and find your Pi IPv4 address.
- **Stretch:** Draw the physical network and explain who assigns addresses with no router.

## Exit question

Did the data actually move to your Pi? How could you prove it?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
