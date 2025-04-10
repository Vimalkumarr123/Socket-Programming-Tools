# **Socket-Programming-Tools** 🚀  

*A Python-based collection of networking utilities demonstrating socket programming fundamentals, from port scanning to multi-client chat applications.*  

---

## **🔍 Overview**  

This project implements essential network tools using Python's `socket` module, covering both TCP and UDP protocols. Ideal for learning networking concepts, debugging, or building foundational knowledge for cybersecurity and distributed systems.  

### **✨ Features**  

| Tool | Description |  
|------|------------|  
| **Port Scanner** | Scans IP addresses for open ports with configurable range and multi-threading support |  
| **Banner Grabber** | Retrieves service banners from open ports (e.g., HTTP, SSH, FTP) |  
| **TCP Client/Server** | Demonstrates reliable, connection-oriented communication |  
| **UDP Client/Server** | Shows fast, connectionless messaging with datagrams |  
| **Multi-Client Chat** | Real-time chat application supporting multiple users with basic commands |  

---

## **🚀 Getting Started**  

### **Prerequisites**  
- Python 3.6+  
- Basic understanding of networking (TCP/UDP, ports)  

### **Installation**  
Clone the repository:  
```bash
git clone git@github.com:Vimalkumarr123/Socket-Programming-Tools.git
cd Socket-Programming-Tools
```  

### **Usage**  
Each tool is standalone. Run them directly:  

| Tool | Command |  
|------|---------|  
| Port Scanner | `python port_scanner.py` |  
| Banner Grabber | `python banner_grabber.py` |  
| TCP Server | `python tcp_server.py` |  
| TCP Client | `python tcp_client.py` |  
| UDP Server | `python udp_server.py` |  
| UDP Client | `python udp_client.py` |  
| Chat Server | `python chat_server.py` |  
| Chat Client | `python chat_client.py` |  

---

## **📸 Screenshots (Optional)**  

*(You can add GIFs/images here showing the tools in action.)*  

**Port Scanner Output:**  
```
🚪 Scanning 127.0.0.1 from port 20 to 80...  
✨ Found open door: Port 22 (SSH)  
✨ Found open door: Port 80 (HTTP)  
```  

**Chat Application Demo:**  
```
[SERVER] Alice joined the chat!  
Alice: Hey everyone!  
Bob: Welcome, Alice!  
```  

---

## **🛠️ Technical Details**  

- **Concurrency:** Uses `ThreadPoolExecutor` for efficient port scanning.  
- **Error Handling:** Gracefully manages timeouts and connection issues.  
- **Extensible:** Modular design allows easy integration of new features.  

---

## **💡 Contributing**  
Contributions are welcome! Open an issue or submit a PR for improvements.  

---

## **📬 Contact**  
Let’s connect!  
🔗 [LinkedIn](https://www.linkedin.com/in/vimal-kumar-r-aa8265184?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BuHvqf2JGRwS1wdpubCkHuQ%3D%3D)  
📧 vimalkumarr738@gamil.com  

---

**🌟 Star this repo if you found it useful!**  

--- 

### **Why This Project?**  
- **Great for learning** socket programming and networking basics.  
- **Practical utilities** that can be extended for real-world use.  
- **Clean, documented code** suitable for beginners and intermediate developers.  

---

This README is designed to:  
✅ **Attract recruiters** with clear skills demonstration  
✅ **Help users** quickly understand and run the project  
✅ **Encourage contributions** with a friendly tone  

Would you like to add any specific badges (e.g., Python version, build status) or a project roadmap?
