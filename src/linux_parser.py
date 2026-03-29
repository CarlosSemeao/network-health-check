from typing import List, Dict


def parse_ip_a_output(file_path: str) -> List[Dict[str, str]]:
    """
    Parse Linux 'ip a' output into a list of interface dictionaries.
    """
    interfaces = []
    current_interface = None

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        if line[0].isdigit():
            if current_interface:
                interfaces.append(current_interface)

            parts = stripped.split(": ", 2)
            if len(parts) < 2:
                continue

            name_part = parts[1]
            interface_name = name_part.split("@")[0]

            state = "UNKNOWN"
            if " state " in stripped:
                state = stripped.split(" state ")[1].split()[0]

            current_interface = {
                "interface": interface_name,
                "state": state,
                "ipv4": "unassigned",
                "type": "loopback" if interface_name == "lo" else "ethernet",
            }

        elif stripped.startswith("inet ") and current_interface:
            ipv4 = stripped.split()[1].split("/")[0]
            current_interface["ipv4"] = ipv4

    if current_interface:
        interfaces.append(current_interface)

    return interfaces