from flask import Flask, render_template
from routes.user_routes import user_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(user_bp)

# Optional: simple frontend route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)