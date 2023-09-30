What is a server:
- It is a hardware or a software system that provides services to clients(users).
it hosts a website and responds to requests frrom clients(users).

What is the role of the domain name
- The Domain name is a human-readable address that maps the name to the IP address using the DNS.

What type of DNS record www is in www.foobar.com
- The type of DNS record is an A record which maps the human readable address to the IP address.
host name and its IPv4 address.
can be found by running dig www.foobar.com

What is the role of the web server
- The role of the web server (Nginx) is to accept requests via HTTP / HTTPS and respond 
with the static contents of the website. (HTML, CSS, etc.) 
and forwards dynamic requests to application server.

What is the role of the application server
- The role of the application server is to accept requests from the web server and provide dynamic contents 
contents by interacting with the codebase and database. 

What is the role of the database
- The role of the database (MySQL) is to store and manage data efficiently and respond to
requests from application server.

What is the server using to communicate with the computer of the user requesting the website:
- Communcation between the computer of user and website is done using the TCP/IP protocol.

You must be able to explain what the issues are with this infrastructure:

SPOF: Single Point of Faliure:
- There are multiple SPOF in this infrastructure.
-  Example: This infrastructure relies on one server (8.8.8.8). This causes problems as if the server 
experiences issues, the website becomes inaccessible. 

Downtime when maintenance needed
- When maintenance is required (such as deploying new code) the server has to be turned off which wuld 
make the website down. 

Cannot scale if too much incoming traffic
- This infrastructure cannot handle traffic, it would need load balancing as it can run out of reources
and slow down when getting a lot of requests / traffic
