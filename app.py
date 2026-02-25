from flask import Flask, redirect
from config import Config
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

@app.route("/")
def home():
    return redirect("/login")

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)