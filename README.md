# Multithreaded--HTTP-Protocol
A simple project that highlights how a server accepts and maintains multiple connections. 
A multithread server handle multiple client request by simultaneously handling multiple threads on the same process.

OPERATION
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

 Web Browsers:
 1. Chrome
 2. Internet Explorer
 3. Firefox
