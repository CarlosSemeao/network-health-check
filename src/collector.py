import socket
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError


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
            timeout=5,
        )
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")

        if error:
            raise RuntimeError(error.strip())

        return output

    except paramiko.AuthenticationException:
        raise RuntimeError("Authentication failed")
    except NoValidConnectionsError:
        raise RuntimeError("Connection failed: unable to reach port 22")
    except socket.timeout:
        raise RuntimeError("Connection timeout")
    except paramiko.SSHException as error:
        raise RuntimeError(f"SSH error: {error}")
    except Exception as error:
        raise RuntimeError(f"Unexpected error: {error}")
    finally:
        client.close()