Cloud Data Encryption & Access Control (SDG 9 & 16) 🔒

This project is a secure web application built with Python (Flask) that demonstrates local-first data encryption and strict access control, addressing core requirements for data privacy and security in digital infrastructure.🎯 Sustainable Development Goals (SDG) AlignmentThis project directly supports the following UN Sustainable Development Goals:SDGGoalAlignmentSDG 9Industry, Innovation, and InfrastructurePromotes secure digital infrastructure and innovative approaches to data security using strong cryptography (Fernet).SDG 16Peace, Justice, and Strong InstitutionsEnsures integrity and accountability in digital data handling by restricting access to authorized users via session-based authentication and secure password hashing.⚙️ Core Technology and FeaturesTechnology StackBackend Framework: Python / FlaskCryptography: cryptography library (Fernet symmetric encryption)Security: werkzeug.security for password hashingKey FeaturesSecure Access Control: The application uses sessions to enforce login, protecting all core routes (/dashboard, /encrypt, /decrypt).Symmetric Encryption: Files are encrypted and decrypted using a single, unique secret.key.Secure Cleanup: Temporary files uploaded and created during processing are automatically deleted from the server after the download is complete, preventing data leakage and disk clutter.Modern UI: A clean, dark-mode theme is applied using inline CSS for a consistent and modern look across the Login and Dashboard pages.🛠️ Installation and Setup1. PrerequisitesPython 3.x (Version 3.13.5 was used in development).git (for cloning).2. Clone and NavigateBash# Clone the repository
git clone https://github.com/HarshithaGovindasamy/cloud-data-encryption-access-control.git
cd cloud-data-encryption-access-control
3. Setup Virtual Environment and DependenciesBash# Create and activate the virtual environment
python -m venv venv
source venv/bin/activate # Use venv\Scripts\activate on Windows

# Install the dependencies (Flask, cryptography)
pip install -r requirements.txt
4. Run the ApplicationThe main application file (app.py) is inside the src/ directory.Bash# Navigate to the source folder
cd src

# Run the application
python app.py
The application will be accessible at: http://127.0.0.1:5000/💻 How to Use the System1. LoginNavigate to the address above. Use one of the pre-configured credentials:UsernamePasswordadminadmin123harshasecurelove2. Generate the Key (CRITICAL STEP)The application cannot encrypt or decrypt without the secret.key file.After logging in, click the "🔑 Generate New Key" link on the dashboard.This creates or overwrites the secret.key file in the project's root directory.3. File OperationsEncrypt File: Upload any file, and the server returns a new .encrypted version.Decrypt File: Upload the .encrypted file you received, and the server returns the original, readable file.📂 Project StructureThe project uses a clean structure to separate the Flask core from security logic:cloud-data-encryption-access-control/
├── .gitignore                   # Ignores venv, secret.key, and temporary files
├── README.md                    # This file
├── requirements.txt
└── src/
    ├── app.py                   # Main app, routes, session management, file cleanup
    ├── encryption/              # Security and cryptography modules
    │   ├── access_control.py
    │   ├── decrypt.py
    │   └── encrypt.py
    └── templates/               # HTML templates (Login, Dashboard)
