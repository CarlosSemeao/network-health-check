from typing import List, Dict


def parse_show_ip_interface_brief(file_path: str) -> List[Dict[str, str]]:
    """
    Parse Cisco-like 'show ip interface brief' output into a list of dictionaries.
    Handles multi-word interface status such as 'administratively down'.
    """
    interfaces = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.split()

        if len(parts) < 6:
            continue

        interface_name = parts[0]
        ip_address = parts[1]
        ok = parts[2]
        method = parts[3]

        remaining = parts[4:]

        if remaining[0] == "administratively" and len(remaining) >= 3:
            status = "administratively down"
            protocol = remaining[2]
        else:
            status = remaining[0]
            protocol = remaining[1]

        interface_data = {
            "interface": interface_name,
            "ip_address": ip_address,
            "ok": ok,
            "method": method,
            "status": status,
            "protocol": protocol,
        }

        interfaces.append(interface_data)

    return interfaces