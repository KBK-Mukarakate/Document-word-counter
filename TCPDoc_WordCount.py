# Name: TCPDoc_WordCount.py
# Desc: application should be able to read the contents of a text file (.txt) and upload the
# content to the server
# Auth: Kundai Mukarakate
# Date: 29/03/24

import socket

# Define server details and buffer size
server_host = '127.0.0.1'
server_port = 11000
buffer_size = 512

# Function to send file content to the server in chunks
def send_file_chunks(file_content, client_socket):
    # Split the file content into chunks of size buffer_size
    chunks = [file_content[i:i+buffer_size] for i in range(0, len(file_content), buffer_size)]
    
    # Iterate through each chunk and send it to the server
    for chunk in chunks:
        client_socket.sendall(chunk.encode('utf-8')) 
    # Signal end of file by sending an empty chunk
    client_socket.sendall(b'')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

user_file = input("Enter the path to the text file: ")
    
# Read the content of the text file
with open(user_file, 'r') as file:
    file_content = file.read()

# Send the file content to the server in chunks
send_file_chunks(file_content, client_socket)

# Receive the word count response from the server
answer = client_socket.recv(4096).decode() 
print("Word count:", answer)
client_socket.close()