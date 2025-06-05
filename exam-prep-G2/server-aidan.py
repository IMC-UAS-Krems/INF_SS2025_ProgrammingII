import socket
import threading
import json

# * Function to handling client
def handle_client(address: str, socket) -> None:
    print(f"Connection established with {address}")
    try:
        while True:
            message_from_client = socket.recv(1024)

            if not message_from_client:
                break
            decoded_message = message_from_client.decode('utf-8')
            print("Recieved from client: ", decoded_message)

            message_to_send = f"Server echoed: {decoded_message}"
            socket.send(message_to_send.encode("utf8"))
    except Exception as e:
        print("Error", e)
    finally:
        socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9000))
s.listen()
s.settimeout(1)

try:
    while True:
        try:
            client_socket, address = s.accept()
            t1 = threading.Thread(target=handle_client, args=(address, client_socket))
            t1.start()

        except socket.timeout:
            pass

except KeyboardInterrupt:
    print("\nServer shutting down.")

