from flask import Flask, redirect
import os
import datetime
import subprocess

app = Flask(__name__)

def get_username():
    try:
        return os.getlogin()
    except:
        return os.environ.get('USER', 'Unknown')

def get_top_output():
    try:
        cmd = "ps aux | head -n 20"
        output = subprocess.check_output(cmd, shell=True).decode()
        return output
    except:
        return "Could not fetch process data"

@app.route('/')
def root():
    # Redirect root path to /htop
    return redirect('/htop')

@app.route('/htop')
def htop():
    # Get basic system information
    name = "Your Full Name"  # Replace with your name
    username = get_username()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = get_top_output()

    response = f"""Name: {name}
Username: {username}
Server Time (IST): {server_time}
TOP output:

{top_output}"""
    
    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    print("Server is running. Access the application at:")
    print("http://localhost:5000/htop")  # Local access
    print("or your Codespace URL with /htop")
    app.run(host='0.0.0.0', port=5000, debug=True)
