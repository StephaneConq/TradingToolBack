from flask import Flask
from flask_cors import CORS

from blueprints import user_bp, ftx_bp, telegram_bp, routine_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(ftx_bp, url_prefix='/api/market')
app.register_blueprint(telegram_bp, url_prefix='/api/telegram')
app.register_blueprint(routine_bp, url_prefix='/api/run')

if __name__ == '__main__':
    app.run()
