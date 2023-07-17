import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deploy', methods=['GET'])
def run_command():
    directory = os.environ.get('LINUX_DIRECTORY', '')
    command = os.environ.get('LINUX_COMMAND', '')

    if directory:
        os.chdir(directory)

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8')), 500

if __name__ == '__main__':
    app.run(debug=True)
