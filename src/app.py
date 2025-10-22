from flask import Flask, render_template, request, redirect, url_for, flash, send_file, session, after_this_request
from encryption.encrypt import generate_key, encrypt_file
from encryption.decrypt import decrypt_file
from encryption.access_control import authenticate
import os
from functools import wraps

# --- Configuration ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)
# IMPORTANT: This secret key is now used for session security. 
app.secret_key = "secure_project_2025" 

UPLOAD_FOLDER = os.path.join(BASE_DIR, "upload")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Security Decorator ---
def login_required(f):
    """Decorator to ensure user is logged in before accessing a route."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            flash('Access denied. Please log in.', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

# --- Routes ---

@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if authenticate(username, password):
        # Set session variable on successful login
        session['logged_in'] = True 
        session['username'] = username
        flash(f"Welcome back, {username}!", "success")
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid credentials", "danger")
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear session variables
    session.pop('logged_in', None)
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required 
def dashboard():
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/generate-key')
@login_required 
def generate():
    generate_key()
    flash("New encryption key generated successfully!", "success") # Changed to success for better visibility
    return redirect(url_for('dashboard'))

@app.route('/encrypt', methods=['POST'])
@login_required 
def encrypt():
    file = request.files.get('file')
    if file and file.filename != '':
        # 1. Save uploaded file temporarily
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # 2. Encrypt the file
        encrypted_path = encrypt_file(filepath)

        # 3. Register cleanup function to run AFTER the response is sent
        @after_this_request
        def cleanup(response):
            try:
                # Delete both the original uploaded file and the encrypted temporary file
                os.remove(filepath)
                os.remove(encrypted_path)
            except Exception as e:
                app.logger.error(f"Error cleaning up files after encrypt: {e}")
            return response
        
        # 4. Stream the encrypted file to the user
        flash("File encrypted successfully and ready for download!", "success")
        return send_file(
            encrypted_path, 
            as_attachment=True, 
            download_name=os.path.basename(encrypted_path)
        )
    else:
        flash("No file selected!", "warning")
        return redirect(url_for('dashboard'))

@app.route('/decrypt', methods=['POST'])
@login_required 
def decrypt():
    file = request.files.get('file')
    if file and file.filename != '':
        # 1. Save uploaded file temporarily
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # 2. Define output path and decrypt
        output_file = filepath.replace(".encrypted", "_decrypted.bin")
        
        try:
            decrypted_path = decrypt_file(filepath, output_file)
        except Exception as e:
            # Handle potential decryption errors (InvalidToken)
            os.remove(filepath) 
            flash("Decryption failed. File may be corrupted or key is incorrect.", "danger")
            app.logger.error(f"Decryption Error: {e}")
            return redirect(url_for('dashboard'))

        # 3. Register cleanup function to run AFTER the response is sent
        @after_this_request
        def cleanup(response):
            try:
                # Delete the encrypted input and the decrypted temporary file
                os.remove(filepath)
                os.remove(decrypted_path)
            except Exception as e:
                app.logger.error(f"Error cleaning up files after decrypt: {e}")
            return response
        
        # 4. Stream the decrypted file to the user
        flash("File decrypted successfully and ready for download!", "success")
        return send_file(
            decrypted_path, 
            as_attachment=True, 
            download_name=os.path.basename(output_file)
        )
    else:
        flash("No file selected!", "warning")
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)