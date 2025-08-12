 Firmware Co-Simulation Log Analyzer

 Overview
The Firmware Co-Simulation Log Analyzer is a Python-based tool designed to parse and analyze co-simulation logs from HDD SoC model and firmware testing environments. It automates error detection, checks protocol compliance for SAS, SATA, and PCIe, and generates real-time performance graphs. This tool reduces manual log review time, improves debugging accuracy, and speeds up pre-silicon verification cycles.

 Features
- Automated error pattern detection in large log files
- Protocol compliance checks for SAS, SATA, and PCIe
- Real-time performance graph generation
- Multi-threaded log parsing for faster analysis
- Configurable rules for error matching
- Secure API endpoints for integration with testing pipelines

 Tech Stack
- Python
- Multi-threading
- SAS, SATA, PCIe protocol knowledge
- FastAPI
- MongoDB
- JWT & OAuth2
- Postman (API testing)

 Installation
1. Clone the repository:
git clone https://github.com/Charanlokesh22/Firmware-CoSim-Log-Analyzer.git

2. Install dependencies:
  
3. Configure database connection and authentication in
config.py


4. Access API endpoints at :-
http://localhost:8000/docs



