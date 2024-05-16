# Document-word-counter
Year1, Semester 2 CMP109 Portfolio project TCPDoc_WordCount.py

## Description

This Python script allows users to read the contents of a text file (.txt) and upload the content to a server using TCP (Transmission Control Protocol). The server then calculates the word count of the text file and sends the result back to the client.

## Author

- **Name**: Kundai Mukarakate

## Date

- **Date**: 29/03/24

## Functionality

The script performs the following tasks:

1. **Define Server Details**: Specifies the server's host address, port number, and buffer size for communication.

2. **Send File Chunks**: Defines a function `send_file_chunks` to send the file content to the server in chunks. It splits the file content into chunks of a specified buffer size and sends each chunk to the server using a TCP socket connection.

3. **Establish Connection**: Creates a TCP client socket and connects to the server using the defined server details.

4. **Input File Path**: Prompts the user to enter the path to the text file they want to upload.

5. **Read File Content**: Reads the content of the specified text file.

6. **Send File Content**: Sends the file content to the server in chunks using the `send_file_chunks` function.

7. **Receive Word Count**: Receives the word count response from the server and prints the result.

8. **Close Connection**: Closes the client socket connection after completing the communication with the server.

## Usage

1. Run the script in a Python environment.
2. Enter the path to the text file (.txt) when prompted.
3. The script will upload the file content to the server.
4. The server will calculate the word count and send the result back to the client.
5. The client will display the word count received from the server.
6. The connection will be closed automatically after the communication.

## Additional Notes

- Users can customize the server details (host address, port number) and buffer size according to their requirements.
- The script assumes that the server is running and ready to accept connections on the specified host and port.
- Ensure that the specified text file exists and is accessible to the script for reading.

