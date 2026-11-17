# Isolated wired networking — **no router or Wi-Fi**

```text
TEACHER Pi (192.168.50.1; eth0; SSH + DHCP + CSV files)
                         |
                Cat5e/Cat6 Ethernet
                         |
             [24-port unmanaged switch]
              /     |      |       \
         student01 student02  ...  student15
```

The switch **does not assign IP addresses**. The master Pi runs `dnsmasq` as a small **DHCP-only** server. No default gateway or DNS service is advertised. Do not uplink the switch to the school LAN. Confirm the arrangement meets the site's IT policy.

## Instructor setup (Raspberry Pi OS Bookworm/Trixie with NetworkManager)

Perform while you can install packages, **before the network is isolated**. Use the Pi's **wired physical `eth0` only**. The desktop may be reached through a keyboard and monitor while changing network settings.

```bash
sudo apt update
sudo apt install -y dnsmasq openssh-server
nmcli -f GENERAL.CONNECTION device show eth0
```

Use the displayed profile name below in place of `Wired connection 1`. Configure a static IP but **no gateway or DNS**. Be careful not to alter the wrong interface.

```bash
sudo nmcli connection modify 'Wired connection 1' \
  ipv4.method manual ipv4.addresses 192.168.50.1/24 \
  ipv4.gateway '' ipv4.dns '' ipv4.never-default yes \
  ipv6.method disabled
sudo nmcli connection up 'Wired connection 1'
ip -4 addr show eth0
```

Create `/etc/dnsmasq.d/ai-lab.conf` as root:

```ini
interface=eth0
bind-interfaces
port=0
# This segment is *not* connected to any other DHCP server:
dhcp-authoritative
dhcp-range=192.168.50.100,192.168.50.199,255.255.255.0,12h
# Empty options: do not advertise a default router or DNS server.
dhcp-option=option:router
dhcp-option=option:dns-server
```

Apply and check errors:

```bash
sudo dnsmasq --test
sudo systemctl enable --now dnsmasq ssh
sudo systemctl restart dnsmasq
sudo systemctl status dnsmasq --no-pager
```

If restarting fails, see [Troubleshooting](troubleshooting.md) for port conflicts. Avoid enabling network sharing/NAT: **no IP forwarding, Wi-Fi hotspot, or bridge to school infrastructure** is required.

## Teacher SSH dataset account

```bash
sudo adduser classroom
sudo install -d -o root -g root -m 755 /srv/ai-lab
# From the repo root, after teacher/prepare_datasets.py runs:
sudo cp data/public/*.csv /srv/ai-lab/
sudo chown root:root /srv/ai-lab/*.csv
sudo chmod 644 /srv/ai-lab/*.csv
sudo systemctl enable --now ssh
```

Use a **unique workshop password** stored privately, not in Git. For stronger access control, give students separate accounts or SSH keys. Do not grant `sudo` to `classroom`. Keep `data/private/` and its answer file out of `/srv/ai-lab`.

## Student connection test

Student Ethernet should be set to **Automatic (DHCP)** (default on Raspberry Pi OS). On student Pi:

```bash
ip -4 addr show eth0
ping -c 3 192.168.50.1
ssh classroom@192.168.50.1
ls /srv/ai-lab
exit
mkdir -p ~/ai-lab/data
scp classroom@192.168.50.1:'/srv/ai-lab/*.csv' ~/ai-lab/data/
```

If hostname resolution is uncertain, use the **fixed IP** `192.168.50.1`, not `teacherpi.local`. Do **not** use `cp` to download files across machines; use `scp`.

**Preflight:** On one student Pi confirm a `192.168.50.100–199` lease, a ping reply, successful SSH, and SCP. Then physically disconnect any outside network and repeat the test. For a truly offline classroom, disable radios on teacher and student Pis or follow the school's required wireless policy.
