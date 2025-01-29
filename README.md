# Multithreaded-HTTP-Protocol
A simple project that highlights how a server accepts and maintains multiple connections. 
A multithread server handles multiple client request by simultaneously handling multiple threads on the same process.

## ✨OPERATION:<br>
When the server receives a TCP connection
request from a client, it will set up the TCP connection through another port and services the client
request in a separate thread. There will be a separate TCP connection in a separate thread for each
request/response pair.

## 🚀Features:
- Handles multiple client connections using threads.
- Sends a simple HTML response to each client.
- Easy to set up and run


## 😡Problem encountered:
1. Encoding
   The server could not encode the html file created, since it was not set in the "utf-8" format(string format)<br>
   soln:- adding the format to the file encoding send method. `connection_socket.send("HTTP/1.1 200 ok\r\n\r\n".encode("utf-8"))`
   @ensure the encoding style is uniform across the entire code

## Run the server<br>
  `python web2_server.py 6789`

  
## Accessing the server contents:<br>
  on your browser url, type:  `http://<server_IP_addr>:6789/filename.html`

  
 
 ## PROOF OF CONCEPT:
 Powershell:<br>
 - Checking incoming connections
    ![Image](https://github.com/user-attachments/assets/372a2427-c64d-45da-a80e-29bdff939154)

 Web Browsers:<br>
 - Checking the cute.html file created on the same directory as Multithreaded web server.
  1. Chrome<br>
  
      ![Image](https://github.com/user-attachments/assets/a6168cea-b18a-4557-a9ca-3941c6411552)
    
 2. Internet Explorer
    
    ![Image](https://github.com/user-attachments/assets/58167d58-e38c-4a09-8b55-b665f40567eb)
    
 3. Firefox
    ![Image](https://github.com/user-attachments/assets/2bbadd2b-d69b-49fa-9544-13293add5666)



copyright: ComputerNetworks: A Top Down Approach. Programming Assignments: Web Server Lab1
