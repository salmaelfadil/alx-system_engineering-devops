For every additional element, why you are adding it?
Additional element: Web Server:
- It is used to address SPOF issue by adding another server.

Additional element: Load Balancer (HAproxy):
- It is added to distribute traffic among two servers for efficiency

What distribution algorithm your load balancer is configured with and how it works
- HAProxy Load Balancer is configured with Round Robin distribution algorithm.
- Clients are distributed in simple rotation between servers.

Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- Load-balancer is enabling on an Active-Active setup as both servers recieve requests.
In active-passive setup one of the servers is passive and only becomes active if the primary server fails.

How a database Primary-Replica (Master-Slave) cluster works
- Primary-Replica database cluster, the primary node(Master) handels wrtie operations (INSERT, UPDATE, DELETE)
while replica node (Slave) handels the read operations(SELECT)

What is the difference between the Primary node and the Replica node in regard to the application
- The Primary node is responsible for handling write operations and maintaining the authoritative copy of the data.
Replica nodes serve read operations and replicate data from the Primary to ensure data consistency.

Issues with this Infrastructure:

SPOF:

While the addition of a second server mitigates some SPOF concerns, there may still be single points of failure in individual components. 
For Example, if the database becomes a single point of failure, the entire system could still experience downtime.

Security Issues (No Firewall, No HTTPS):

The infrastructure lacks security measures like firewalls to protect against unauthorized access.
HTTPS should be implemented to encrypt data in transit. Currently, the system is susceptible to data interception.

No Monitoring:
Monitoring is used to know the status of each server. This infrastructure has no monitoring.

