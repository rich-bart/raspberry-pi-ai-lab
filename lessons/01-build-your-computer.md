# Build Your Computer

**Duration:** 120-minute meeting; approximately **85 minutes of instruction** after arrival and check-in.  
**Checkpoint:** A working Raspberry Pi desktop.  
**Learning goals:** Identify a Pi, storage, power, cooling and peripherals; safely assemble the CanaKit; power on a desktop.

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

Make a hardware scavenger hunt: CPU, RAM, microSD, USB ports, Ethernet, two micro-HDMI ports. Demonstrate static safety and handling before power. Pair students for an initial parts check. Assemble case/cooler as the kit instructs; attach keyboard, mouse, micro-HDMI monitor and independent monitor power if needed; insert pre-imaged microSD; connect Pi power last. Boot and find the terminal. Label the station.

## Command(s) to practice

```bash
hostname
python3 --version
```

Run commands from `~/ai-lab/`. Where a command contains quotation marks, type/copy them as shown. Student Pis must already contain the `student/` scripts; Session 3 downloads the dataset into `data/` from the teacher Pi.

## Three paths to success

- **Guided:** Students with no experience follow a picture-based parts checklist.
- **Independent:** Students explain the difference between RAM and the microSD card, and find their hostname.
- **Stretch:** Students investigate what a GPU is and why our later Random Forest does not need one.

## Exit question

Which component stores files while the power is off? Why should you shut down before removing power?

**If an individual workstation fails:** use a spare pre-imaged Pi or instructor-supplied USB copy so the lesson can continue offline. Refer to [troubleshooting](../docs/troubleshooting.md).
