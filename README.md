# Cloud Data Encryption & Access Control (SDG 9 & 16) 🔒

This project is a secure web application built with **Python (Flask)** that demonstrates local-first data encryption before "cloud storage" (simulated by file download) and strict access control for authorized users. It addresses the crucial need for **data privacy** and **security** in digital infrastructure.

## 🎯 SDG Alignment

This project directly supports the following UN Sustainable Development Goals:

| SDG | Goal | Alignment |
| :--- | :--- | :--- |
| **SDG 9** | **Industry, Innovation, and Infrastructure** | Promotes **secure digital infrastructure** and innovative approaches to data security using strong cryptography (Fernet). |
| **SDG 16** | **Peace, Justice, and Strong Institutions** | Ensures **integrity** and **accountability** in digital data handling by restricting access to authorized users via session-based authentication and secure password hashing. |

---

## ⚙️ Setup and Installation

Follow these steps to get the project running locally.

### 1. Prerequisites

* Python 3.x installed.
* The project structure organized as follows: `src/` must contain `app.py`, and the security modules must be in `src/encryption/`.

### 2. Setup and Dependencies

```bash
# 1. Create and activate the virtual environment
python -m venv venv
source venv/bin/activate # Use venv\Scripts\activate on Windows

# 2. Install Dependencies (Flask and cryptography)
pip install -r requirements.txt






💻 Usage and Credentials
1. Login Credentials
Use one of the pre-configured credentials to access the system:

Username	Password
admin	admin123


Export to Sheets

2. Essential First Step: Generate Key
After logging in, you must click the 🔑 Generate New Key link on the dashboard first. This creates the required secret.key file that the application uses for all encryption and decryption operations.

3. Encryption/Decryption Workflow
Encryption: Upload any file. The server encrypts it using the loaded key and streams the new .encrypted file back to your browser.

Decryption: Upload the .encrypted file. The server decrypts it using the same key and streams the original content back to your browser.

Security Note: All temporary uploaded files and their processed counterparts are immediately deleted from the server after the download begins, ensuring data security and system hygiene.

📂 Project Structure
cloud-data-encryption-access-control/
├── .gitignore
├── requirements.txt
└── src/
    ├── app.py                      # Main Flask application and session control
    ├── encryption/                 # Security logic package
    │   ├── __init__.py
    │   ├── access_control.py       # Password hashing and authentication
    │   ├── decrypt.py              # Fernet decryption
    │   └── encrypt.py              # Key generation and Fernet encryption
    └── templates/                  # Frontend HTML files
        ├── dashboard.html
        └── login.html
