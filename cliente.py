import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

username = input('Digite seu nome de usuário: ')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(username.encode())


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f'Erro: {str(e)}')
            client_socket.close()
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client_socket.send(message.encode())
