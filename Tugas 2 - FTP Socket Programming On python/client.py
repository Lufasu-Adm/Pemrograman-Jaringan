import socket
import os

SERVER_ADDRESS = ("localhost", 5002)
BUFFER_SIZE = 4096

client_directory = 'client'
if not os.path.exists(client_directory):
    os.makedirs(client_directory)

def receive_file(s, filename):
    try:
        file_size = int.from_bytes(s.recv(4), byteorder='big')
        file_data = s.recv(file_size)
        file_path = os.path.join(client_directory, filename)

        if not os.path.exists(client_directory):
            os.makedirs(client_directory)

        with open(file_path, "wb") as f:
            f.write(file_data)
        print(f"File {filename} berhasil diterima.")
    except FileNotFoundError:
        print("Direktori untuk penyimpanan file tidak ada.")
    except Exception as e:
        print(f"Gagal menerima file: {str(e)}")
        
def sent_file(conn, filename):
    file_path = os.path.join(client_directory, filename)
    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_length = len(file_data)
                conn.sendall(file_length.to_bytes(4, byteorder='big'))
                conn.sendall(file_data)
            print(f"File {filename} berhasil dikirim.")
        except Exception as e:
            print(f"Gagal mengirim file: {str(e)}")
    else:
        print("File tidak ditemukan pada client.")
            
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("[*] Client sedang berjalan.")
    connected = False  
    while True:
        command = input("Masukkan perintah: ").strip()
        if not command:
            continue
        
        if command.lower() == 'connme':
            s.connect(SERVER_ADDRESS)
            
            s.send(command.encode())  
            response = s.recv(BUFFER_SIZE).decode()
            print(response)
            connected = True  
        elif connected:
            if command.lower() == 'ls':
                s.send(command.encode())  
                response = s.recv(BUFFER_SIZE).decode()
                print(response)  
            elif command.lower().startswith("rm"):
                s.send(command.encode())
                response = s.recv(BUFFER_SIZE).decode()
                print(response)
            elif command.lower().startswith("size"):
                s.send(command.encode())
                response = s.recv(BUFFER_SIZE).decode()
                print(response)
            elif command.lower().startswith("download"):
                s.send(command.encode()) 
                _, filename = command.split(maxsplit=1)
                receive_file(s, filename)
            elif command.lower().startswith("upload"):
                s.send(command.encode())
                _, filename = command.split(maxsplit=1)
                sent_file(s, filename)
            elif command.lower() == 'byebye':
                s.send(command.encode())
                response = s.recv(BUFFER_SIZE).decode()
                print(response)
                s.close()  
                break
            else:
                response = "Invalid command."
                print(response)

        else:
            print("Client belum terhubung ke server.")
            