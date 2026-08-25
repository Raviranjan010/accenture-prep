import os

net_content = """# Core CS Fundamentals: Computer Networks Basics

## 1. What is it?
A **Computer Network** is an interconnected collection of computers, servers, and devices that communicate and exchange data with one another using standardized digital rules called **Protocols**.

### Beginner Vocabulary Glossary
Before exploring network layers, let's define essential networking terms in plain language:
- **Client**: A device or software application that requests data (e.g., your web browser on a phone).
- **Server**: A powerful computer that stores website data/APIs and serves requests back to clients.
- **IP Address (Internet Protocol Address)**: A unique logical digital address assigned to every device on a network (e.g., `192.168.1.1` or `142.250.190.46`). Like a home postal street address.
- **MAC Address (Media Access Control)**: A permanent hardware physical address burned into your device's network card at the factory (e.g., `00:1A:2B:3C:4D:5E`). Like a fingerprint.
- **Port**: A specific digital doorway/channel on a server used by a specific service (e.g., Port 80 for HTTP, Port 443 for HTTPS, Port 22 for SSH).
- **Packet**: A small chunk of data formatted with source/destination headers sent across the internet.
- **Socket**: The combination of an IP Address + Port Number (e.g., `192.168.1.1:8080`) creating an active communication endpoint.

---

## 2. Why does it matter?
1. **Essential Assessment Topic**: OSI layers, TCP vs UDP, HTTP status codes, and DNS flows appear in technical tests and interviews.
2. **Web & App Development**: Every modern full-stack web application relies on API communication across computer networks.
3. **Network Security & Cloud**: Understanding firewalls, SSL/TLS certificates, and load balancing requires core networking fundamentals.

---

## 3. When to use it?
- **Choose TCP when**: You need 100% reliable, error-free data transfer where no packet can be lost (e.g., Banking, Web Pages, Email, File Transfers).
- **Choose UDP when**: You need maximum transmission speed and low latency, and missing a few packets is acceptable (e.g., Video Streaming, Live Gaming, VoIP Voice Calls).

---

## 4. How it works
1. **Data Segmentation**: Application data is split into small packets.
2. **Encapsulation**: As data moves down network layers, each layer adds its own header (Application $\rightarrow$ Transport $\rightarrow$ Network $\rightarrow$ Data Link $\rightarrow$ Physical).
3. **Routing**: Routers inspect IP headers and forward packets across nodes on the internet.
4. **Decapsulation & Assembly**: Receiver strips headers and reassembles packets into original data.

---

## 5. Key rules or syntax

### Standard Protocol Port Numbers
- **HTTP**: Port 80 (Unencrypted Web Traffic)
- **HTTPS**: Port 443 (Encrypted Secure Web Traffic)
- **FTP**: Port 20 / 21 (File Transfer)
- **SSH**: Port 22 (Secure Shell Remote Access)
- **DNS**: Port 53 (Domain Name Resolution)

### TCP 3-Way Handshake
```
Client                              Server
  |                                   |
  | -------- 1. SYN ----------------> | (Proposes connection)
  |                                   |
  | <------- 2. SYN-ACK ------------- | (Acknowledges & proposes back)
  |                                   |
  | -------- 3. ACK ----------------> | (Connection Established!)
  |                                   |
```
*Why 3-Way Handshake works*: Ensures both Client and Server are online, ready, and agree on initial sequence numbers before sending payload data.

---

## 6. Simple example

### Level 1 (Easy): Sending a Web Request
- **Client**: You type `https://google.com` in Chrome.
- **DNS**: System translates name `google.com` to IP `142.250.190.46`.
- **Port**: Request connects to IP `142.250.190.46` on **Port 443** (HTTPS).
- **Response**: Server sends back HTML data packets displaying the search engine.

---

## 7. Detailed example

### Part A: The OSI 7-Layer Model vs. TCP/IP Model

| OSI Layer # | Layer Name | Primary Function | Key Protocols / Devices |
| :--- | :--- | :--- | :--- |
| **7** | Application | Interface for end-user applications | HTTP, HTTPS, FTP, DNS, SMTP |
| **6** | Presentation | Encryption, Compression, Syntax formatting | SSL/TLS, JPEG, ASCII |
| **5** | Session | Manages session setup & termination | NetBIOS, RPC |
| **4** | Transport | End-to-end reliability, segmentation | TCP, UDP (Ports) |
| **3** | Network | Routing & logical IP addressing | IP (IPv4/v6), ICMP, Routers |
| **2** | Data Link | Physical MAC addressing, error checking | Ethernet, Wi-Fi, Switches |
| **1** | Physical | Raw bits transmission over wires | Fiber, Cables, Hubs |

- **Simple Mnemonic**: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (*Application, Presentation, Session, Transport, Network, Data Link, Physical*).
- **Realistic Enterprise Example**: When you submit a credit card payment:
  1. Application Layer (HTTP POST request created)
  2. Presentation Layer (SSL/TLS encrypts payload)
  3. Transport Layer (TCP attaches Port 443)
  4. Network Layer (IP attaches source/dest IP)
  5. Data Link Layer (Ethernet frame attaches MAC addresses)
  6. Physical Layer (Transmitted as light pulses through fiber optics).

---

### Part B: TCP vs. UDP Comparison

| Feature | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Connection Type** | Connection-oriented (Handshake required). | Connectionless (Fire and forget). |
| **Reliability** | Guaranteed delivery (retransmits lost packets). | Unreliable (no retransmission). |
| **Packet Order** | Guaranteed in-order arrival via Sequence Numbers. | No order guarantee (packets can arrive out of order). |
| **Speed** | Slower (overhead of headers & acknowledgments). | Ultra-fast (minimal header overhead). |

- **Realistic Enterprise Example**: Zoom Video Call: Audio/video frames use **UDP** for real-time speed. Chat text messages inside Zoom use **TCP** so no text is lost.

---

### Part C: What Happens When You Type a URL in a Browser?

When you type `https://www.accenture.com` and press Enter:

1. **URL Parsing**: Browser checks protocol (`https`), domain (`www.accenture.com`), and default port (`443`).
2. **DNS Resolution**:
   - Browser checks local DNS cache.
   - Checks OS hosts file cache.
   - Queries ISP Recursive DNS Server $\rightarrow$ Root DNS $\rightarrow$ TLD Server $\rightarrow$ Authoritative Server $\rightarrow$ Returns IP Address.
3. **TCP 3-Way Handshake**: Client sends `SYN`, Server replies `SYN-ACK`, Client sends `ACK`.
4. **TLS Handshake**: Secure key exchange for HTTPS encryption.
5. **HTTP GET Request**: Browser sends request headers to server.
6. **Server Response**: Web server processes request and returns `200 OK` with HTML/CSS/JS payload.
7. **Browser Rendering**: Browser parses HTML, constructs DOM, renders page.

---

## 8. Practical use case
**Building an E-Commerce Payment Integration over HTTPS**:
1. Uses **HTTPS (Port 443)** to encrypt credit card tokens via TLS at Presentation Layer.
2. Uses **TCP** at Transport Layer so transaction payloads are never corrupted or lost.
3. Uses **DNS** so the mobile app hits `api.payment.com` securely without hardcoding static IP addresses.

---

## 9. Common mistakes

### Concept 1: IP vs MAC Address Mistakes
- *Mistake*: Thinking an IP address is fixed permanently to a laptop.
- *Why it happens*: IP addresses are **logical** (change depending on the network you join). MAC addresses are **physical** (burned into network hardware).

### Concept 2: Protocol Selection Mistakes
- *Mistake*: Attempting to use UDP for file downloads or banking APIs.
- *Why it happens*: UDP drops lost packets silently, which would result in corrupted file downloads or missing financial transaction data!

### Concept 3: HTTP vs HTTPS Mistakes
- *Mistake*: Assuming HTTP (Port 80) is secure on private Wi-Fi.
- *Why it happens*: HTTP sends raw plain text over the air. Anyone running Wireshark packet sniffer can read passwords. HTTPS encrypts payload using SSL/TLS.

---

## 10. Tips & tricks

### Shortcut 1: OSI Layer 7 Mnemonic
- **Mnemonic (Top to Bottom)**: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing (*Application $\rightarrow$ Presentation $\rightarrow$ Session $\rightarrow$ Transport $\rightarrow$ Network $\rightarrow$ Data Link $\rightarrow$ Physical*).

### Shortcut 2: The Port Number Anchor List
- **22**: SSH (Secure Shell)
- **53**: DNS (Domain Name System)
- **80**: HTTP (Unencrypted Web)
- **443**: HTTPS (Encrypted Web)

### Shortcut 3: TCP Handshake Formula
- Remember: **SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK** (3 steps total).

---

## 11. Practice exercises

1. **(Easy - Recall)** What is the default port number for secure HTTPS traffic?
2. **(Easy - Recall)** Which address is permanently burned into a network card: IP or MAC address?
3. **(Easy - Concept)** Is DNS responsible for translating domain names to IP addresses or MAC addresses?
4. **(Medium - Why)** Why is TCP preferred over UDP for sending emails and downloading files?
5. **(Medium - Scenario)** Which OSI layer is responsible for SSL/TLS encryption and decryption?
6. **(Medium - Applied)** List the 3 steps of the TCP 3-Way Handshake in correct sequential order.
7. **(Medium - Scenario)** A user cannot open websites by typing `google.com`, but can open them by typing IP `142.250.190.46`. Which network service is failing?
8. **(Hard - Applied)** What HTTP status code range represents Client Errors vs. Server Errors?
9. **(Hard - Scenario)** Explain how a Router uses the Network Layer (Layer 3) to forward packets across different subnets.
10. **(Hard - Architecture)** Why does HTTPS require both Asymmetric Encryption (for TLS Handshake) and Symmetric Encryption (for session data transfer)?

---

## 12. Q&A with explanations

1. **Answer**: **Port 443**.
2. **Answer**: **MAC Address**.
3. **Answer**: Domain names to **IP addresses**.
4. **Answer**: TCP guarantees 100% reliable, in-order packet delivery with error checking and retransmission of lost packets. Missing a single byte in a file or email corrupts the content.
5. **Answer**: **Presentation Layer (Layer 6)**.
6. **Answer**: 1. `SYN` $\rightarrow$ 2. `SYN-ACK` $\rightarrow$ 3. `ACK`.
7. **Answer**: **DNS (Domain Name System)** service is failing or misconfigured.
8. **Answer**: **4xx** = Client Errors (e.g., `404 Not Found`, `401 Unauthorized`); **5xx** = Server Errors (e.g., `500 Internal Server Error`, `502 Bad Gateway`).
9. **Answer**: Routers examine destination IP addresses in Network Layer headers, consult Routing Tables, and forward packets to the next hop IP address across different subnets.
10. **Answer**: Asymmetric encryption (Public/Private key pair) is mathematically slow but secure for initial key exchange during TLS Handshake. Once a shared secret key is safely exchanged, fast Symmetric encryption is used for session data payload transfer.

---

## 13. Quick revision

> [!TIP]
> ### 🚀 Computer Networks Cheat-Sheet
> - **OSI 7 Layers**: Application, Presentation, Session, Transport, Network, Data Link, Physical.
> - **IP Address**: Logical network address (IPv4 32-bit / IPv6 128-bit).
> - **MAC Address**: Physical hardware address (48-bit).
> - **Ports**: 80 (HTTP), 443 (HTTPS), 53 (DNS), 22 (SSH).
> - **TCP**: Reliable, connection-oriented (3-Way Handshake: SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK).
> - **UDP**: Fast, connectionless, unreliable (Streaming, Gaming).
> - **DNS**: Converts Domain Names $\rightarrow$ IP Addresses.

---

## 14. Connection to next topic
Congratulations on mastering Core Computer Science Fundamentals (OOPs, DBMS, OS, Networks)! You are now fully prepared to write high-performance algorithms. Continue to Track 2 DSA practice starting with **[dsa-practice/arrays-strings.md](../dsa-practice/arrays-strings.md)**!
"""

with open('02-technical-coding/cs-fundamentals/networking-basics.md', 'w', encoding='utf-8') as f:
    f.write(net_content)

print("networking-basics.md updated.")
