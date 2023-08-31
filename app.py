from flask import Flask, request, jsonify
from scraper import do_scraping
from database import last_log

import threading

app = Flask(__name__)

EXECUTING = [False]
ERROR = None

@app.route('/activate', methods=['POST'])
def activate():
    global EXECUTING
    global ERROR
    
    if EXECUTING[-1] == False:
        EXECUTING.append(True)

        thread = threading.Thread(target=do_scraping, args=(EXECUTING,))
        thread.start()

        response = {"message": "successfully started"}
        return jsonify(response), 200
    else:
        response = {"message": "another thread is running"}
        return jsonify(response), 405

@app.route('/status', methods=['GET'])
def status():
    global EXECUTING
    global ERROR
    
    if ERROR:
        return jsonify({"message": ERROR}), 200
    else:
        if len(EXECUTING) > 0:
            if EXECUTING[-1]:
                return jsonify({"message": "running"}), 200
            else:
                return jsonify({"message": "not running"}), 200
        else:
            return jsonify({"message": "not running"}), 200

@app.route('/last-log', methods=['GET'])
def getLastLog():
    global EXECUTING
    global ERROR
    
    log = last_log()

    if log and len(log) > 1:
        return jsonify({"time": log[1], "message": log[2]}), 200

    return jsonify({"message": "no log"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
