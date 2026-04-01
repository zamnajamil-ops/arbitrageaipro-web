"""
ArbitrageAI Pro - Main Flask Application
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'arbitrageaipro2026')
CORS(app)

# ─── LANDING PAGE ───────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

# ─── AUTH PAGES ─────────────────────────────
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ─── API ENDPOINTS ───────────────────────────
@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "message": "ArbitrageAI Pro is running!"})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    return jsonify({"success": True, "message": "Message received!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
