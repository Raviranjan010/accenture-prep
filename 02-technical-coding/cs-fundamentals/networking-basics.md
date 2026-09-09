# CS Fundamentals: Computer Networks & Protocol Suites

## What this is
Computer Networking defines the communication models, protocol layers, routing mechanisms, and data transmission rules enabling devices to communicate across local (LAN) and global (Internet) networks. In Accenture CS technical tests, OSI layers, TCP vs UDP, DNS resolution, and common protocol ports are tested.

---

## Formula / Rule / Pattern

| OSI Layer Number | Layer Name | Primary Function | Common Protocols / Devices |
| :--- | :--- | :--- | :--- |
| **Layer 7** | Application | Network service interface for applications | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| **Layer 6** | Presentation | Data formatting, encryption, compression | SSL/TLS, JPEG, ASCII |
| **Layer 5** | Session | Inter-host session establishment & management | NetBIOS, PPTP |
| **Layer 4** | Transport | End-to-end delivery, segmentation, flow control | TCP (Connection-oriented), UDP (Connectionless) |
| **Layer 3** | Network | Logical IP addressing & path routing | IP, ICMP, ARP, Routers |
| **Layer 2** | Data Link | Physical MAC addressing, frame framing, error detection | Ethernet, Wi-Fi, Switches, Bridges |
| **Layer 1** | Physical | Binary bit transmission over electrical/optical medium | Cables, Repeaters, Hubs |

---

## Shortcut: The Common Protocol Port Cheat Sheet

> [!TIP]
> ### The Top 10 Port Anchors
> Memorize these high-frequency network ports tested in corporate MCQs:
> - **Port 20/21**: FTP (File Transfer)
> - **Port 22**: SSH (Secure Shell)
> - **Port 23**: Telnet (Unencrypted Remote Shell)
> - **Port 25**: SMTP (Email Sending)
> - **Port 53**: DNS (Domain Name System)
> - **Port 80**: HTTP (Web unencrypted)
> - **Port 443**: HTTPS (Web encrypted via SSL/TLS)
> - **Port 3306**: MySQL Database
> 
> *Why it works*: Port numbers account for 30% of networking assessment MCQs. Memorizing 8 ports locks in instant answers.

---

## Worked Examples

### Example 1: TCP vs UDP Protocol Selection (Easy)
- **Question**: Why does video live streaming or online gaming prefer UDP over TCP?
- **Step-by-step Solution**:
  1. TCP enforces 3-way handshakes, sequence acknowledgments (ACK), and packet retransmissions, creating latency overhead.
  2. UDP is connectionless and lightweight without retransmissions, prioritizing low latency and real-time delivery over 100% loss-free transmission.
  3. **Choice**: UDP.

### Example 2: Subnetting IP Mask Calculation (Medium)
- **Question**: Given IP `192.168.1.0/24`, how many usable host addresses exist in this subnet?
- **Step-by-step Solution**:
  1. Prefix length `/24` leaves $32 - 24 = 8$ host bits.
  2. Total IP addresses $= 2^8 = 256$.
  3. Usable hosts $= 2^8 - 2 = 254$ (subtracting Network ID `.0` and Broadcast IP `.255`).

---

## Practice Questions (PYQ Bank)

Q1. Which layer of the OSI model is responsible for routing packets across logical IP networks?  
a) Data Link Layer  
b) Network Layer  
c) Transport Layer  
d) Session Layer  

Q2. What is the standard port number for HTTPS (HTTP Secure)?  
a) 80  
b) 8080  
c) 443  
d) 22  

Q3. What protocol translates human-readable domain names (e.g. `google.com`) into IP addresses?  
a) DHCP  
b) ARP  
c) DNS  
d) ICMP  

Q4. Which transport layer protocol provides reliable, connection-oriented data delivery with error checking and flow control?  
a) UDP  
b) TCP  
c) IP  
d) ICMP  

Q5. What protocol maps an IP address to a physical hardware MAC address on a local area network?  
a) RARP  
b) ARP (Address Resolution Protocol)  
c) DNS  
d) NAT  

Q6. How many bits make up an IPv4 address versus an IPv6 address?  
a) IPv4 = 32 bits, IPv6 = 128 bits  
b) IPv4 = 64 bits, IPv6 = 128 bits  
c) IPv4 = 32 bits, IPv6 = 64 bits  
d) IPv4 = 16 bits, IPv6 = 32 bits  

Q7. What is the 3-way handshake sequence used to establish a TCP connection?  
a) SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK  
b) ACK $\rightarrow$ SYN $\rightarrow$ FIN  
c) HELLO $\rightarrow$ WAIT $\rightarrow$ CONNECT  
d) SYN $\rightarrow$ DATA $\rightarrow$ CLOSE  

Q8. Which device operates primarily at Layer 2 (Data Link Layer) of the OSI model?  
a) Hub  
b) Switch  
c) Router  
d) Repeater  

Q9. What protocol automatically assigns IP addresses to devices joining a network?  
a) DNS  
b) DHCP (Dynamic Host Configuration Protocol)  
c) SMTP  
d) SNMP  

Q10. What is the loopback IPv4 address reserved for testing local machine services?  
a) `192.168.1.1`  
b) `127.0.0.1`  
c) `10.0.0.1`  
d) `255.255.255.255`  

Q11. Which layer of the OSI model handles data encryption and formatting (e.g. SSL/TLS, ASCII)?  
a) Application Layer  
b) Presentation Layer  
c) Transport Layer  
d) Session Layer  

Q12. What does ICMP protocol power?  
a) Web browsing  
b) `ping` and `traceroute` diagnostic commands  
c) File downloads  
d) Email transmission  

Q13. How many total layers exist in the standard TCP/IP model?  
a) 4 layers  
b) 7 layers  
c) 5 layers  
d) 3 layers  

Q14. What is MAC address length?  
a) 32 bits  
b) 48 bits (6 bytes)  
c) 64 bits  
d) 128 bits  

Q15. Why must 2 IP addresses be subtracted when calculating usable hosts in a subnet?  
a) Reserved for Network Address (all zeros) and Broadcast Address (all ones)  
b) Reserved for router and firewall  
c) Hardware limitation  
d) Speed optimization  

---

## Answers

1. **b) Network Layer** — Layer 3 handles logical routing.
2. **c) 443** — HTTPS encrypted port.
3. **c) DNS** — Domain Name System.
4. **b) TCP** — Connection-oriented transport protocol.
5. **b) ARP (Address Resolution Protocol)** — Resolves IP $\rightarrow$ MAC.
6. **a) IPv4 = 32 bits, IPv6 = 128 bits** — Standard IP lengths.
7. **a) SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK** — TCP connection establishment.
8. **b) Switch** — Layer 2 MAC-based forwarding device.
9. **b) DHCP** — Dynamic IP allocation.
10. **b) `127.0.0.1`** — Localhost loopback IP.
11. **b) Presentation Layer** — Layer 6 formatting and encryption.
12. **b) `ping` and `traceroute` diagnostic commands** — ICMP control messaging.
13. **a) 4 layers** — Application, Transport, Internet, Network Access.
14. **b) 48 bits (6 bytes)** — Hexadecimal hardware address.
15. **a) Reserved for Network Address... and Broadcast Address...** — Subnetting rule.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Core CS Fundamentals Technical MCQ section.

---

## Recommended videos
- [Accenture Technical Assessment Networking & Coding Video](https://www.youtube.com/watch?v=DwZZNJxBAn0) — Networking MCQs.
- [Accenture Technical Practice Walkthrough](https://www.youtube.com/watch?v=1pW3xrNu1z8) — Protocol suite review.
