from socket import *
import threading
import sys # program termination




# function to handle each thread
def handle_client(connection_socket, addr):
    try:
        print(f"connection established by {addr}")

        # Receive requested message from the client
        message =  connection_socket.recv(1024).decode("utf-8",  errors='replace')
        print(f"message received from {addr}: {message}")



        # Extract the file content from the message
        if len(message) > 0:
            filename = message.split()[1]
            try:
                # open requested file
                with open(filename[1:], "r", encoding="utf-8", errors="replace") as f:
                    output_data = f.read()

                # send the http header
                connection_socket.send("HTTP/1.1 200 ok\r\n\r\n".encode("utf-8"))

                # send the contents of the requested file to the client
                connection_socket.sendall(output_data.encode("utf-8"))

            except FileNotFoundError:
                # send error message for file not found

                error_message = ("HTTP/1.1 404 Not Found\r\n\r\n"
                    "<html><head></head><body><h1>404 Not Found</h1></body></html>")

                connection_socket.send(error_message.encode("utf-8"))
        connection_socket.close() # close socket after serving the client


    except UnicodeDecodeError as e:
        print(f"Error handling client {addr}: {e}")

    except Exception as e:
        print(f"Error handling client {addr}: {e}")



    finally:
        connection_socket.close()

#Main function
def start_server():
    server_port= 6789
    server_socket=socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("0.0.0.0", server_port))
    server_socket.listen(5)

    print(f"Server is ready to receive")

    try:
        while True:
            print("Waiting for connection...")

           # Accept new connection
            connection_socket, addr = server_socket.accept()

           # New thread to handle each client
            client_thread = threading.Thread(
               target=handle_client, args=(connection_socket, addr)
                )
            client_thread.start() #start the thread

    except KeyboardInterrupt:
       print("\nshutting down the server.")
       server_socket.close()
       sys.exit()

    except Exception as e:
        print(f"server error: {e}")
        server_socket.close()
        sys.exit()

if __name__ == "__main__":
    start_server()












