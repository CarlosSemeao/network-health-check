from typing import List, Dict


def generate_linux_report(results: List[Dict[str, str]]) -> str:
    """
    Generate a readable Linux interface health report.
    """
    lines = []
    lines.append("LINUX NETWORK HEALTH CHECK REPORT")
    lines.append("=" * 50)

    for item in results:
        lines.append(f"Interface : {item['interface']}")
        lines.append(f"Type      : {item['type']}")
        lines.append(f"State     : {item['state']}")
        lines.append(f"IPv4      : {item['ipv4']}")
        lines.append(f"Health    : {item['health']}")
        lines.append(f"Reason    : {item['reason']}")
        lines.append("-" * 50)

    return "\n".join(lines)


def save_linux_report(report: str, output_path: str = "linux_report.txt") -> None:
    """
    Save the Linux network health report to a file.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)