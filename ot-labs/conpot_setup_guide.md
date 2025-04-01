# 🏭 Getting Started with Conpot

**Conpot** is an open-source ICS honeypot designed to simulate industrial systems.

## Installation
```bash
sudo apt update
sudo apt install conpot
```

## Run the honeypot
```bash
conpot
```

## Simulate a scan from another terminal
```bash
nmap -sV -p 1024 localhost
```

Conpot will log the interaction and emulate responses from industrial protocols.
