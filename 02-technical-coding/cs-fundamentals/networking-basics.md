# Core CS Fundamentals: Computer Networks Basics

## 1. OSI 7-Layer Model vs. TCP/IP Model

| OSI Layer | Name | Function / Protocol | TCP/IP Layer |
| :--- | :--- | :--- | :--- |
| **7** | Application | HTTP, HTTPS, FTP, DNS, SMTP | Application |
| **6** | Presentation | Encryption, Data formatting (SSL/TLS) | Application |
| **5** | Session | Session establishment & maintenance | Application |
| **4** | Transport | End-to-end connection, reliability (TCP, UDP) | Transport |
| **3** | Network | Routing, IP Addressing (IP, ICMP) | Internet |
| **2** | Data Link | MAC Addressing, framing (Ethernet, Wi-Fi) | Network Access |
| **1** | Physical | Bits transmission over cables/fiber | Network Access |

---

## 2. TCP vs. UDP

- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, guarantees packet order via 3-Way Handshake (`SYN` $ightarrow$ `SYN-ACK` $ightarrow$ `ACK`), error checking, flow control. Used for HTTP/HTTPS, Web, Email.
- **UDP (User Datagram Protocol)**: Connectionless, fast, unreliable, no order guarantee. Used for Video streaming, Gaming, VoIP, DNS queries.

---

## 3. What Happens When You Type a URL in a Browser?

1. **DNS Lookup**: Browser checks local cache $ightarrow$ OS cache $ightarrow$ Resolver $ightarrow$ Root/TLD DNS server to resolve `google.com` to IP `142.250.190.46`.
2. **TCP 3-Way Handshake**: Client sends `SYN`, server returns `SYN-ACK`, client confirms with `ACK`.
3. **TLS Handshake (HTTPS)**: Cipher suite negotiation and certificate verification.
4. **HTTP GET Request**: Browser sends request headers.
5. **Server Processing & Response**: Server returns HTML/CSS/JS payload.
6. **DOM Rendering**: Browser parses HTML and renders page.
