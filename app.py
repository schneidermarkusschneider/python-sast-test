from flask import Flask, request, jsonify
from controllers.access_control_controller import access_control_bp
from controllers.crypto_controller import crypto_bp
from controllers.injection_controller import injection_bp
from controllers.design_controller import design_bp
from controllers.config_controller import config_bp
from controllers.auth_controller import auth_bp
from controllers.integrity_controller import integrity_bp
from controllers.logging_controller import logging_bp
from controllers.ssrf_controller import ssrf_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardcoded-secret-key-123'
app.config['DEBUG'] = True

app.register_blueprint(access_control_bp, url_prefix='/api/v1/access')
app.register_blueprint(crypto_bp, url_prefix='/api/v1/crypto')
app.register_blueprint(injection_bp, url_prefix='/api/v1/inject')
app.register_blueprint(design_bp, url_prefix='/api/v1/design')
app.register_blueprint(config_bp, url_prefix='/api/v1/config')
app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
app.register_blueprint(integrity_bp, url_prefix='/api/v1/integrity')
app.register_blueprint(logging_bp, url_prefix='/api/v1/logging')
app.register_blueprint(ssrf_bp, url_prefix='/api/v1/ssrf')

@app.route('/')
def home():
    return jsonify({"message": "OWASP Top 10 Vulnerable Test Application"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
