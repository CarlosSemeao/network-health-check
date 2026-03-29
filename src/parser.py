from typing import List, Dict


def parse_show_ip_interface_brief(file_path: str) -> List[Dict[str, str]]:
    """
    Parse Cisco-like 'show ip interface brief' output into a list of dictionaries.
    """
    interfaces = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.split()

        if len(parts) < 6:
            continue

        interface_data = {
            "interface": parts[0],
            "ip_address": parts[1],
            "ok": parts[2],
            "method": parts[3],
            "status": parts[4],
            "protocol": parts[5],
        }

        if len(parts) > 6:
            interface_data["protocol"] = " ".join(parts[5:])

        interfaces.append(interface_data)

    return interfaces