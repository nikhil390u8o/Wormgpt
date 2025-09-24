#!/usr/bin/env python3
"""
Flask web server for ping and health checks for Render hosting
"""

from flask import Flask, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "status": "online",
        "service": "NGYT777GG WORM AI Telegram Bot",
        "message": "Bot is running and ready to serve!"
    })

@app.route('/ping')
def ping():
    """Ping endpoint for health checks"""
    return jsonify({
        "status": "ok",
        "ping": "pong",
        "service": "healthy"
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "NGYT777GG WORM AI Bot",
        "uptime": "running"
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
