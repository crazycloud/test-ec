from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)


@app.route('/', methods=['POST'])
def stress_cpu():
    # create a subprocess for running "stress_cpu.py"
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'CPU stress test initiated'


@app.route('/', methods=['GET'])
def get_private_ip():
    # return the private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return f'The private IP address is {private_ip}'


if __name__ == '__main__':
    app.run()
