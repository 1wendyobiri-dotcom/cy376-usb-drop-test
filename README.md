# CY376 USB Drop Test - Wendy Obiri

## Summary
This project designs and executes a controlled, non-destructive USB drop test
inside an isolated VMware lab (VMnet1, Host-Only). A Kali Linux machine acts
as the attacker/listener; an Ubuntu machine acts as the victim endpoint. A
physical USB drive carries two HTML beacon payloads (a labelled variant and a
neutral control variant) that log a timestamped HTTP request when opened,
with no destructive code or data exfiltration.

## Tools Used
- VMware Workstation (Host-Only networking, VMnet1)
- Kali Linux (attacker / listener)
- Ubuntu 64-bit (victim endpoint)
- Python 3 (custom HTTP beacon listener)

## How to Run
1. Start the listener on Kali: `python3 src/beacon_listener.py`
2. Open either payload file (`src/Payroll_2026.html` or
   `src/New_Document.html`) on the victim machine.
3. Check the listener terminal / `evidence/beacon_log.txt` for the logged
   trigger event.

## Folder Structure
- `src/` - listener script and payload files
- `configs/` - lab network setup notes
- `docs/` - final report (PDF)
- `evidence/` - screenshots and beacon log

## Screenshots
See the `evidence/` folder for lab topology, connectivity tests, listener
output, and beacon log captures.
