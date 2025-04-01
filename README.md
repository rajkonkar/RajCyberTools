# 🛡️ Raj's Cybersecurity Tools & Labs

Welcome to my personal cybersecurity toolkit — a collection of hands-on projects, scripts, and research built during my MSc in Cybersecurity at the University of York (NCSC Certified). This repo showcases practical skills in **incident response**, **threat detection**, and **OT/ICS security** through real tools and learning resources.

---

## 📁 Repository Structure

### 🔍 Detection Scripts

| Tool                  | Description                                                    |
|-----------------------|----------------------------------------------------------------|
| `ssh_log_monitor.py` | Detects brute-force SSH attempts from `/var/log/auth.log`.     |

---

### 🧪 Simulated OT Labs

| File                   | Description                                |
|------------------------|--------------------------------------------|
| `conpot_setup_guide.md` | How to deploy a Conpot ICS honeypot locally |

---

### 📚 Threat Analysis Writeups

| Topic                | Description                                               |
|----------------------|-----------------------------------------------------------|
| `stuxnet_summary.md` | Breakdown of the Stuxnet malware + MITRE mapping + lessons learned |

---

## 🔧 ICS Log Analyzer (`ics_log_analyzer.py`)

A Python-based CLI tool that simulates log detection for ICS/OT environments. It scans logs for **suspicious control commands** (e.g., `STOP_PROCESS`, `WRITE_REGISTER`) and alerts in real time, with options to filter, save, or continuously monitor new entries.

---

## 🚀 How to Use

### 🔍 Basic Scan
```bash
python3 ics_log_analyzer.py --file test_log.txt

🎯 Filter by Command
python3 ics_log_analyzer.py --file test_log.txt --keyword STOP_PROCESS

📁 Save Suspicious Output

python3 ics_log_analyzer.py --file test_log.txt --output suspicious.txt

🔁 Real-Time Monitoring (like tail -f)

python3 ics_log_analyzer.py --file test_log.txt --watch

🧪 Generate Sample Log for Testing

echo "CMD=STOP_PROCESS SRC=192.168.1.100" > test_log.txt
echo "CMD=WRITE_REGISTER SRC=192.168.1.200" >> test_log.txt
echo "CMD=READ_SENSOR SRC=192.168.1.150" >> test_log.txt

Use this file to test all flags and behaviors of the tool.

💡 Skills Demonstrated

    Threat detection logic in Python

    Real-time log monitoring

    CLI design with argparse

    OT/ICS security concepts

    File I/O and output formatting

    Error handling and log simulation

🛠️ Future Additions

Support monitoring multiple files concurrently

YAML-based config for keyword rules and alert behavior

Regex rule engine for advanced detections

Integration with honeypots like Conpot

Log rotation support + alert throttling

GUI frontend or web-based visualizer

👋 About Me

👨‍💻 MSc in Cybersecurity | University of York (NCSC Certified)
🔐 Focus: Incident Response, Threat Detection, ICS/OT Security
🛠️ Always learning, building, and open to collaborations

📫 Connect with me on LinkedIn -- https://www.linkedin.com/in/raj-konkar-b70b512a0/
