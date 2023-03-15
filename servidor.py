import socket
import threading

HOST = '127.0.0.1'
PORT = 12345


def handle_client(client_socket, client_address):
    print(f'Conexão estabelecida com {client_address}')

    username = client_socket.recv(1024).decode()
    print(f'{client_address} se conectou como {username}')

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print(f'{client_address} se desconectou')
                break

            print(f'{username}: {message}')
            for client in clients:
                if client != client_socket:
                    client.send(f'{username}: {message}'.encode())

        except Exception as e:
            print(f'Erro: {str(e)}')
            break

    clients.remove(client_socket)
    client_socket.close()


clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'Servidor iniciado em {HOST}:{PORT}')

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))
    client_thread.start()
