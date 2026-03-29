# network-health-check

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