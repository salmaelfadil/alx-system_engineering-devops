* For every additional element, why you are adding it
Load Balancer:
Distributes incoming traffic evenly among the servers for load balancing and redundancy.

Web Servers:
Host the www.foobar.com website.
Multiple servers provide redundancy and improve website performance. If one server fails, the others can continue serving traffic.

SSL Certificate:
Enables HTTPS to encrypt traffic between clients and the web servers to ensure data security.

Three Firewalls :
Firewall 1 acts as a perimeter firewall while Firewalls 2 and 3 are placed between each web server and the load balancer.

Monitoring clients:
Collect and send server performance and application metrics to a monitoring service.

* What are firewalls for?
provide network security by filtering incoming and outgoing traffic, protecting against unauthorized access

* Why is the traffic served over HTTPS?
to ensure data privacy, integrity, and authenticity. 

* What monitoring is used for?
for Monitoring clients collect data on various aspects.

* How the monitoring tool is collecting data?
Monitoring clients collect data on various aspects, such as server CPU and memory usage, response times,
 error rates, and network traffic. This data is sent to the monitoring service over secure channels for analysis.

* Explain what to do if you want to monitor your web server QPS
 To monitor web server QPS, you can track metrics related to incoming requests and server response times.
 if there is an increase in QPS it indicate increased user traffic.

* Why terminating SSL at the load balancer level is an issue?
Terminating SSL at the load balancer exposes decrypted traffic between the load balancer and web servers,
potentially compromising security.

* Why having only one MySQL server capable of accepting writes is an issue?
Because If the MySQL server fails, write operations will be disrupted.

*Why having servers with all the same components (database, web server and application server) might be a problem?
Because it can lead to a lack of diversity and increased vulnerability to common software vulnerabilities.


