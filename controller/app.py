from flask import Flask, render_template, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import drive

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command/<cmd>')
def command(cmd):
    commands = {
        'forward':    drive.forward,
        'reverse':    drive.reverse,
        'turn_left':  drive.turn_left,
        'turn_right': drive.turn_right,
        'spin_left':  drive.spin_left,
        'spin_right': drive.spin_right,
        'stop':       drive.stop,
    }
    if cmd not in commands:
        return jsonify({'error': 'unknown command'}), 400
    commands[cmd]()
    return jsonify({'status': 'ok', 'command': cmd})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
