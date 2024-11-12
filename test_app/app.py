from flask import Flask, jsonify
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App! Visit /htop to see system information."

@app.route('/htop')
def htop():
    name = "Raamji A - 21i241"
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1") 
    return f"<pre>Name: {name}\nUsername: {username}\nServer Time: {server_time} (IST)\n\n{top_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
