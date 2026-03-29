# network-health-check

A Python based network operations tool that connects to a remote Linux host over SSH, collects live interface data, parses the output and generates a structured network health report.

## Objective

This project simulates a real world network monitoring and interface inspection task performed by junior network engineers, Linux administrators and network operations teams.

The tool connects to a live Linux host using SSH with key based authentication, runs the `ip a` command, captures the output and evaluates interface health based on operational state and IPv4 assignment.

## Why this project matters

In network operations and infrastructure support, engineers need to collect live data, inspect interfaces quickly and identify unhealthy conditions clearly.

This project demonstrates:

- Python scripting for network operations
- SSH based remote command execution with Paramiko
- key based authentication
- Linux network interface parsing
- operational health checking logic
- structured report generation for troubleshooting
- clean modular project design

## Project Structure

```text
network-health-check/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/
│   └── sample_linux_report.txt
├── data/
│   ├── sample_show_ip_interface_brief.txt
│   └── ssh_output.txt
└── src/
    ├── checker.py
    ├── collector.py
    ├── linux_checker.py
    ├── linux_parser.py
    ├── linux_reporter.py
    ├── main.py
    ├── parser.py
    └── reporter.py
```

## Live SSH Data Collection

This project connects to a remote Linux host using SSH with key-based authentication and collects live network interface data using the `ip a` command.

The output is saved locally and processed to generate a structured health report.

## Linux Interface Health Analysis

The tool parses Linux interface data and evaluates:

- interface operational state (UP/DOWN)
- presence of IPv4 addresses
- loopback interfaces
- potential misconfigurations

## Example Output

See sample output here:

docs/sample_linux_report.txt

## How it works
1. Establish SSH connection to remote Linux host
2. Execute `ip a` command
3. Capture raw interface output
4. Save output locally to data/ssh_output.txt
5. Parse interface data into structured format
6. Evaluate interface health conditions
7. Generate readable health report

## How to run
pip install -r requirements.txt
python src/main.py

## Output
The script generates:

- raw SSH output:
  data/ssh_output.txt

- structured health report:
  docs/sample_linux_report.txt

## Skills Demonstrated

- Python scripting for infrastructure operations
- SSH automation using Paramiko
- Linux networking fundamentals
- Parsing CLI output into structured data
- Interface health evaluation logic
- File handling and reporting
- Modular code design
- Git version control workflow

## Real World Context

This project mirrors operational tasks performed in:

- Network Operations Center (NOC) environments
- Linux system administration
- DevOps and infrastructure teams

Engineers routinely:

- connect to remote systems over SSH
- collect live interface and system data
- analyse interface states and misconfigurations
- produce clear outputs for troubleshooting and escalation

The same pattern is used in production systems for:

- interface and host monitoring
- automated diagnostics
- incident triage and root cause investigation