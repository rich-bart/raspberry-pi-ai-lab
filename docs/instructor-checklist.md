# Print-friendly instructor checklist

- [ ] Obtain venue approval for an isolated switch and teacher-side DHCP/SSH.
- [ ] Verify one purchased Pi/monitor/power setup and full offline flow.
- [ ] Preimage student SD cards and label computers, cables and power supplies.
- [ ] Preinstall Python system packages; preload `student/`, `lessons/`, `docs/` on every Pi.
- [ ] Disable / leave unconfigured Wi-Fi as required; never uplink switch to other LAN.
- [ ] Configure teacher `192.168.50.1`, dnsmasq and non-admin SSH account.
- [ ] Generate the public datasets and copy only public CSVs to `/srv/ai-lab`.
- [ ] Keep private challenge key outside shared folder and outside Git.
- [ ] Test one student's DHCP, SSH, SCP, tree, forest, and images while fully offline.
- [ ] Prepare student seats, printed starter commands, USB backups, power strips and mentor assignments.
- [ ] During capstone release **only** challenge features and score submitted CSVs on instructor Pi.
