import socket
import threading
import logging
import sys
import requests

logging.basicConfig(filename='lime_ftp.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class LimeFTPServer:
    def __init__(self, host='127.0.0.1', port=21) -> None:
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.client_address = None
        self.running = False
        self.valid_users = {
            "root": "root",
            "admin": "admin"
            }

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(8)
        self.running = True

        print(f'\nLime FTP server running: {self.host}:{self.port}')
        logging.info(f'\nLime Server init {self.host}:{self.port}\n')

        while self.running:
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f'New connection from {self.client_address}')
            logging.info(f'New connection from: {self.client_address}')
            client_thread = threading.Thread(target=self.handle_client, args=(self.client_socket, self.client_address))
            client_thread.daemon = True
            client_thread.start()

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
            print("Lime FTP server has been closed.")
            logging.info("Lime FTP server has been closed.")

    def handle_client(self, client_socket, client_address):
        try:

            client_socket.send(b"220 ProFTPD 1.3.5 Server (Debian) Ready.\r\n")
            logging.info(f'Response sent to {client_address} -> 220 ProFTPD 1.3.5 Server (Debian) Ready.')

            logged_in = False
            username = None

            while self.running:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break

                logging.info(f"Command recieve from {client_address} -> {data}")

                if data.startswith('USER'):
                    username = data.split(' ')[1]
                    client_socket.send(b"331 User name okay, need password.\r\n")
                    logging.info(f"Sent to {client_address} -> 331 User name okay")

                elif data.startswith('PASS'):
                    password = data.split(' ')[1]
                    if username in self.valid_users and self.valid_users[username] == password:
                        logged_in = True
                        client_socket.send(b"230 User logged in, proceed.\r\n")
                        logging.info(f"Sent to {client_address} -> 230 User logged in")
                    else:
                        client_socket.send(b"530 Not logged in.\r\n")
                        logging.info(f"Response sent to {client_address} -> 530 Not Logged in.")

                elif data.startswith('QUIT'):
                    client_socket.send(b"221 Goodbye.\r\n")
                    logging.info(f"Sent to {client_address} -> 221 Goodbye")

                else:
                    client_socket.send(b"502 Command not implemented.\r\n")
                    logging.info(f"Resposta para {client_address} -> 502 Command not implemented")

        except Exception as e:
            logging.error(f"Error trying to treat {client_address}: {e}")
        finally:
            client_socket.close()
            logging.info(f"\nConnection from {client_address} as been closed.")

    def restart(self):
        """Reinicia o servidor FTP."""
        if self.running:
            self.stop()
        self.start()

def lime_server():
    lime = LimeFTPServer()
    try:
        server_thread = threading.Thread(target=lime.start)
        server_thread.daemon = True
        server_thread.start()

        input("Press ENTER to close server...\n")
        lime.stop()

    except KeyboardInterrupt:
        lime.stop()

if __name__ == "__main__":
    lime_server()
