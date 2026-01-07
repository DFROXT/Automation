from flask import Flask, render_template
from groq_ai import generate_script
from video_engine import create_video

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run")
def run():
    script = generate_script()
    create_video(script)
    return "Video Generated Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
