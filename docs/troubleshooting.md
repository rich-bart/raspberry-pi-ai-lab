# Offline-first troubleshooting

| Symptom | First check | Backup plan |
|---|---|---|
| Monitor blank | Pi USB-C power supply, monitor independent power, **micro-HDMI** cable/HDMI input selection | Try known-good screen and cable |
| No student IP | `ip -4 addr show eth0`; cable/switch lights; teacher `sudo systemctl status dnsmasq` | Use student static `192.168.50.101/24` temporarily; ensure IP unique |
| Cannot ping teacher | Teacher `ip -4 addr show eth0` shows `192.168.50.1/24`; cables/switch | Direct Ethernet teacher↔student for single-device diagnosis |
| `dnsmasq` fails to start | `sudo dnsmasq --test`; `sudo journalctl -u dnsmasq -n 40` | Check whether another DHCP service is using UDP 67, fix before class |
| SSH refused | `sudo systemctl status ssh` on master | Start SSH server with `sudo systemctl enable --now ssh` |
| SSH unknown host prompt | Instructor confirms teacher IP / fingerprint | Accept only the teacher host confirmed in class |
| SSH authentication fails | `classroom` account and teacher-provided credential | Instructor resets classroom password; **don't use sudo credentials** |
| `scp` cannot find CSV | `ls /srv/ai-lab/*.csv` on master | Teacher copies `/srv/ai-lab/*.csv` to a USB drive |
| Python import error | `python3 -c 'import sklearn,pandas,matplotlib,numpy'` | Use pre-imaged spare SD card; don't attempt online installs |
| No images generated | Look in `results/` and check script stdout | Open PNG from file manager; scripts use headless `Agg` backend |
| One station very slow | Check power throttling, heat, `--trees`, free storage | Retry with `--trees 10` |
| `test_*.csv` absent | Verify `ls data/` after SCP | Repeat SCP, or use instructor USB backup |

## DHCP fallback — ONLY for troubleshooting one isolated student

If the switch and teacher DHCP are temporarily unavailable, student can set Ethernet manually using Raspberry Pi OS GUI / NetworkManager, e.g. `192.168.50.101/24`, no gateway, and test ping to `192.168.50.1`. Do **not** assign the same address to two computers. Restore automatic DHCP afterward. Do not put the classroom switch on the school LAN.

## Using class time well

If a student is stuck for longer than ~5 minutes, move them to the pre-imaged spare Pi and continue the science lesson; diagnose their original machine later. Students can still run the lesson using prepared data from a USB drive if the switch fails. If the whole class has trouble, use the paper worksheets and decision-tree guessing demonstration.
