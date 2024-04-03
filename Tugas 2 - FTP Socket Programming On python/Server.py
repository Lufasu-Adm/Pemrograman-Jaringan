import socket
import os

SERVER_ADDRESS = ("localhost", 5002)
BUFFER_SIZE = 4096

server_directory = 'server'
if not os.path.exists(server_directory):
    os.makedirs(server_directory)
    
def list_files():
    files = os.listdir(server_directory)
    return "\n".join(files)

def delete_file(filename):
    path = os.path.join(server_directory, filename)
    try:
        os.remove(path)
        return f"File {filename} berhasil dihapus."
    except FileNotFoundError:
        return "File tidak ditemukan."

def get_file_size(filename):
    try:
        path = os.path.join(server_directory, filename)
        filesize = os.path.getsize(path)
        return f"Size: {filesize / 1024:.2f} KB"
    except FileNotFoundError:
        return "File tidak ditemukan."
      
def handle_command(conn, command):
    response = None
    if command.lower().startswith("ls"):
        response = list_files()
    elif command.startswith("rm"):
        _, filename = command.split(maxsplit=1)
        response = delete_file(filename)
    elif command.startswith("size"):
        _, filename = command.split(maxsplit=1)
        response = get_file_size(filename)
    elif command.startswith("download"):
        _, filename = command.split(maxsplit=1)
        file_path = os.path.join(server_directory, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    file_length = len(file_data)
                    conn.sendall(file_length.to_bytes(4, byteorder='big'))
                    conn.sendall(file_data)
                    # conn.sendall(f.read())
            except Exception as e:
                print(f"Gagal menerima file: {str(e)}")
        else:
            print("File tidak ditemukan pada server.")
    elif command.startswith("upload"):
        _, filename = command.split(maxsplit=1)
        try:
            file_size = int.from_bytes(conn.recv(4), byteorder='big')
            file_data = conn.recv(file_size)
            file_path = os.path.join(server_directory, filename)

            if not os.path.exists(server_directory):
                os.makedirs(server_directory)

            with open(file_path, "wb") as f:
                f.write(file_data)
            print(f"File {filename} berhasil diterima dan disimpan.")
        except Exception as e:
            print(f"Gagal menerima file: {str(e)}")
    elif command == "connme":
        response = "[+] Berhasil Terkoneksi."
    else:
        response = "Perintah tidak valid."
    
    if response:
        conn.send(response.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(SERVER_ADDRESS)
    s.listen()
    print("[*] Menunggu Koneksi")
    conn, addr = s.accept()
    print("[+] Berhasil Terkoneksi.")
    with conn:
        while True:
            command = conn.recv(BUFFER_SIZE).decode()
            if not command:
                break
            print(f"Menerima perintah: {command}")
            if command.lower() == "byebye":
                conn.send("Koneksi terputus dengan server.".encode())
                break
            if handle_command(conn, command):
                break
    conn.close()
