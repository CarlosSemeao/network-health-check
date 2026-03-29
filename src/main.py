from collector import collect_ssh_output


def main() -> None:
    host = "10.211.55.8"
    username = "carlossemeao"
    command = "ip a"
    key_filename = "/home/carlossemeao/.ssh/id_ed25519"

    output = collect_ssh_output(host, username, command, key_filename)
    print(output)

    with open("data/ssh_output.txt", "w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
