

---

# **Packet Sniffer**

## Overview

The **Packet Sniffer** is a network monitoring and security tool built with Python and Flask. It captures network packets in real-time, analyzes traffic for anomalies, and provides insights into potential vulnerabilities within a network. This tool is designed for educational and security research purposes.

## Features

- **Network Scanning**: Detects devices on your network by scanning IP addresses and MAC addresses.
- **Packet Sniffing**: Captures and analyzes network packets, including IP addresses, protocols, and payloads.
- **Anomaly Detection**: Uses machine learning to detect unusual network behavior.
- **Vulnerability Detection**: Scans for potential vulnerabilities such as weak passwords and open ports.
- **SSL/TLS Analysis**: Detects outdated encryption protocols or SSL/TLS certificate issues.
- **ARP Spoofing & MITM Detection**: Identifies ARP spoofing and man-in-the-middle (MITM) attacks.
- **Real-Time Alerts**: Notifies users of detected threats, vulnerabilities, and network anomalies.
- **Geo-Tracking**: Maps external IP addresses to their geographical location.
- **Bandwidth Monitoring**: Tracks the bandwidth usage of devices on the network.

## Requirements

- Python 3.7 or above
- `pip` package manager

### Dependencies
The following Python libraries are required for the project:

- Flask
- Flask-SocketIO
- scapy
- pandas
- scikit-learn
- requests
- nmap

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the repository**:
   - Clone or download the project repository to your local machine.

2. **Set up a virtual environment** (optional but recommended):
   - Navigate to your project folder and create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - **Mac/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies**:
   - Use the `requirements.txt` file to install the necessary Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the application**:
   - After setting up, run the Flask application:
     ```bash
     python app.py
     ```

5. **Access the Dashboard**:
   - Open a browser and go to `http://127.0.0.1:5000` to view the Packet Sniffer dashboard.
   - From the dashboard, you can monitor network activity, detect vulnerabilities, and analyze traffic.

## Usage

1. **Real-Time Packet Sniffing**: Start packet sniffing from the dashboard to capture live network packets.
2. **Vulnerability Scanning**: Use the `Vulnerabilities` section to scan for open ports, weak passwords, and other potential security issues.
3. **Monitor Bandwidth**: View bandwidth usage for each device on your network in the `Bandwidth` section.
4. **Geo-Tracking**: Use the `Geo-Tracking` page to see the geographical location of external IP addresses.
5. **ARP Spoofing Detection**: The tool will automatically detect and alert you to ARP spoofing attempts in your network.

## License

This project is licensed under the MIT License.

