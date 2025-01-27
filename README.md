# Multithreaded-HTTP-Protocol
A simple project that highlights how a server accepts and maintains multiple connections. 
A multithread server handles multiple client request by simultaneously handling multiple threads on the same process.

OPERATION:
When the server receives a TCP connection
request from a client, it will set up the TCP connection through another port and services the client
request in a separate thread. There will be a separate TCP connection in a separate thread for each
request/response pair.


Problem encountered:
1. Encoding
   The server could not encode the html file created, since it was not set in the "utf-8" format(string format)
 soln:- adding the format to the file encoding send method.

 PROOF OF CONCEPT:
 
 Powershell- checking incoming connections
    ![Image](https://github.com/user-attachments/assets/372a2427-c64d-45da-a80e-29bdff939154)

 Web Browsers:- checking the cute.html file created on the same directory as Multithreaded web server.
 
 1. Chrome
    ![Image](https://github.com/user-attachments/assets/a6168cea-b18a-4557-a9ca-3941c6411552)
    
 3. Internet Explorer
    ![Image](https://github.com/user-attachments/assets/58167d58-e38c-4a09-8b55-b665f40567eb)
    
 5. Firefox
    ![Image](https://github.com/user-attachments/assets/2bbadd2b-d69b-49fa-9544-13293add5666)
