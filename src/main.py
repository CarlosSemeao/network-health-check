from parser import parse_show_ip_interface_brief
from checker import assess_interface_health
from reporter import generate_report, save_report_to_file


def main() -> None:
    file_path = "data/sample_show_ip_interface_brief.txt"

    interfaces = parse_show_ip_interface_brief(file_path)
    results = assess_interface_health(interfaces)
    report = generate_report(results)

    print(report)
    save_report_to_file(report)


if __name__ == "__main__":
    main()