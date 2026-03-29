
A Python based network operations project that connects to a remote Linux host over SSH, collects live interface data, parses the output and generates a structured network health report.

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

docs/sample_linux_report.txt# network-health-check

A Python based network operations project that connects to a remote Linux host over SSH, collects live interface data, parses the output and generates a structured network health report.

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

docs/sample_linux_report.txt# network-health-check

A Python based network operations project that parses Cisco style `show ip interface brief` output and generates a health report for network interfaces.

## Objective

This project simulates a real world network monitoring task performed by junior network engineers and network operations teams.

The script reads interface data, detects unhealthy conditions and produces a readable report that highlights operational issues such as:

- interface down states
- line protocol failures
- administratively down interfaces
- missing IP addresses

## Why this project matters

In network operations, engineers need to identify faults quickly and understand interface state changes clearly. This project demonstrates:

- Python scripting for network operations
- parsing command line network device output
- operational health checking logic
- clear reporting for troubleshooting
- generating and saving a structured network health report to a text file

## Project Structure

```text
network-health-check/
├── .gitignore
├── README.md
├── requirements.txt
├── report.txt
├── data/
│   └── sample_show_ip_interface_brief.txt
└── src/
    ├── main.py
    ├── parser.py
    ├── checker.py
    └── reporter.py
