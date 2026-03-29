import paramiko


def collect_ssh_output(host: str, username: str, command: str, key_filename: str) -> str:
    """
    Connect to a remote host over SSH using a private key
    and return command output as a string.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            username=username,
            key_filename=key_filename,
            look_for_keys=False,
            allow_agent=False,
        )
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")

        if error:
            return f"ERROR:\n{error}"

        return output

    finally:
        client.close()
