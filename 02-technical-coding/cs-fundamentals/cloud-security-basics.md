# CS Fundamentals: Cloud Computing & Information Security Basics

## What this is
Cloud Computing provides on-demand access to shared computing resources (servers, storage, databases, networking) over the Internet, replacing physical on-premise infrastructure. Information Security establishes defensive concepts—such as symmetric/asymmetric encryption, authentication vs. authorization, and attack awareness (phishing, DDoS)—to protect digital assets and enterprise data integrity.

---

## Formula / Rule / Pattern

| Cloud Service Model | Provided Abstraction | Customer Responsibility | Provider Responsibility |
| :--- | :--- | :--- | :--- |
| **IaaS (Infrastructure as a Service)** | Virtual Machines, Storage, Networks | OS, Middleware, Apps, Data | Physical Hardware, Hypervisor |
| **PaaS (Platform as a Service)** | Runtime Environment, Development Stack | Application Code, Data | OS, Middleware, Hardware, Runtime |
| **SaaS (Software as a Service)** | Ready-to-use End User Software | User Access & Data Configuration | Entire Stack, App, Infrastructure |

**Cloud Deployment Models**:
- **Public Cloud**: Shared infrastructure owned by third-party provider (AWS, Azure, GCP).
- **Private Cloud**: Dedicated infrastructure exclusively used by a single organization.
- **Hybrid Cloud**: Combines public and private clouds, connected by secure encryption.

---

## Shortcut: The Shared Responsibility & Security Matrix

> [!TIP]
> ### The Auth-vs-Auth & Encryption Matrix
> Keep these two core security concepts clear:
> 
> 1. **Authentication vs Authorization**:
>    - **Authentication (AuthN)**: *Who are you?* (Verifying identity via Password, OTP, Biometrics).
>    - **Authorization (AuthZ)**: *What are you allowed to do?* (Checking permissions, Role-Based Access Control).
> 2. **Symmetric vs Asymmetric Encryption**:
>    - **Symmetric**: **1 Shared Key** for both encryption and decryption (Fast, e.g. AES).
>    - **Asymmetric**: **2 Keys (Public Key + Private Key)** (Public encrypts, Private decrypts, e.g. RSA).
> 
> *Why it works*: 80% of entry-level security MCQs test whether a scenario represents AuthN vs AuthZ or Single Key vs Key Pair.

---

## Worked Examples

### Example 1: Identifying Cloud Models (Easy)
- **Scenario**: A company uses Google Workspace (Gmail, Google Docs) for daily email and documentation. What cloud service model does this represent?
- **Step-by-step Solution**:
  1. The software application is fully hosted, managed, and delivered over the web browser.
  2. Users manage no underlying OS or servers.
  3. **Answer**: **SaaS (Software as a Service)**.

### Example 2: Asymmetric Key Cryptography (Medium)
- **Scenario**: Alice wants to send a secure confidential message to Bob using Public Key Infrastructure (PKI). Whose key should Alice use to encrypt the message?
- **Step-by-step Solution**:
  1. Confidentiality rule: Only Bob should be able to decrypt the message.
  2. Bob holds his secret **Private Key**.
  3. Alice encrypts using **Bob's Public Key**.
  4. **Result**: Only Bob can decrypt it using **Bob's Private Key**.

### Example 3: DDoS Attack Conceptual Awareness (Hard)
- **Scenario**: A company web server becomes completely unresponsive after being flooded with millions of bogus HTTP requests simultaneously originating from a compromised botnet of 50,000 infected IoT devices worldwide. What type of attack is this?
- **Step-by-step Solution**:
  1. Attack targets service availability rather than data theft.
  2. Requests originate from multiple distributed sources (botnet).
  3. **Answer**: **DDoS (Distributed Denial of Service) Attack**.

---

## Practice Questions (PYQ Bank)

Q1. Which cloud service model provides virtualized computing infrastructure (VMs, storage, firewalls) where the customer manages the operating system?  
a) SaaS  
b) PaaS  
c) IaaS  
d) FaaS  

Q2. AWS Elastic Beanstalk and Heroku, which allow developers to deploy code without managing servers or OS, are examples of:  
a) IaaS  
b) PaaS  
c) SaaS  
d) CaaS  

Q3. What process verifies the identity of a user claiming to access a system (e.g. entering a password or OTP)?  
a) Authorization  
b) Authentication  
c) Encryption  
d) Auditing  

Q4. Which encryption technique uses a single secret key for both encryption and decryption?  
a) Asymmetric Encryption  
b) Symmetric Encryption  
c) Hashing  
d) Public Key Cryptography  

Q5. A cyber attack where an attacker sends fraudulent emails posing as a legitimate bank to trick users into revealing passwords is:  
a) DDoS  
b) Phishing  
c) SQL Injection  
d) Man-in-the-Middle  

Q6. What cloud deployment model combines on-premise private infrastructure with public cloud services?  
a) Private Cloud  
b) Community Cloud  
c) Hybrid Cloud  
d) Multitenant Cloud  

Q7. In RSA asymmetric encryption, if Message M is encrypted with the Recipient's Public Key, which key must be used to decrypt it?  
a) Sender's Public Key  
b) Sender's Private Key  
c) Recipient's Public Key  
d) Recipient's Private Key  

Q8. What type of security threat involves flooding a target server with overwhelming traffic from multiple distributed computers to cause outage?  
a) Phishing  
b) Distributed Denial of Service (DDoS)  
c) Trojan Horse  
d) Spyware  

Q9. What is a key difference between Hashing and Encryption?  
a) Encryption is one-way, Hashing is two-way  
b) Hashing is a one-way mathematical function (cannot be decrypted), whereas Encryption is two-way  
c) Hashing requires keys  
d) They are identical  

Q10. What does MFA stand for in identity security?  
a) Multi-Factor Authentication  
b) Master File Access  
c) Main Frame Architecture  
d) Multi-Format Authorization  

Q11. Microsoft 365, Salesforce, and Dropbox are prime examples of which cloud service model?  
a) IaaS  
b) PaaS  
c) SaaS  
d) Bare Metal  

Q12. What process determines whether an authenticated user has permission to read a specific confidential database file?  
a) Authentication  
b) Authorization  
c) Hashing  
d) Encryption  

Q13. What is a Public Cloud?  
a) Cloud infrastructure available to the general public or industry groups owned by a cloud provider  
b) Free wifi  
c) Government owned cloud  
d) Open source database  

Q14. What algorithm family is widely used for symmetric data encryption?  
a) RSA  
b) AES (Advanced Encryption Standard)  
c) SHA-256  
d) ECC  

Q15. Why does asymmetric encryption require two distinct keys?  
a) To allow key distribution over untrusted public networks without sharing secret keys beforehand  
b) To double file size  
c) To slow down network speed  
d) Hardware requirement  

---

## Answers

1. **c) IaaS** — IaaS provides raw infrastructure (VMs, storage).
2. **b) PaaS** — PaaS provides managed development environment.
3. **b) Authentication** — Identity verification.
4. **b) Symmetric Encryption** — Single shared secret key.
5. **b) Phishing** — Fraudulent email trickery.
6. **c) Hybrid Cloud** — Mix of public and private cloud.
7. **d) Recipient's Private Key** — Only recipient's private key decrypts messages encrypted with their public key.
8. **b) Distributed Denial of Service (DDoS)** — Traffic flood outage attack.
9. **b) Hashing is a one-way mathematical function...** — Hashing is irreversible.
10. **a) Multi-Factor Authentication** — Verification using 2+ independent factors.
11. **c) SaaS** — Software as a Service.
12. **b) Authorization** — Checking access permissions.
13. **a) Cloud infrastructure available to the general public...** — Public cloud definition.
14. **b) AES (Advanced Encryption Standard)** — Standard symmetric encryption algorithm.
15. **a) To allow key distribution over untrusted public networks...** — Solves key exchange problem.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Technical Assessment (Cloud & Security fundamentals sub-section).

---

## Recommended videos
- TODO: find video for Cloud & Security fundamentals specific to Accenture's format
