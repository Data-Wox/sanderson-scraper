from flask import Flask, request, jsonify
from scraper import do_scraping
from database import last_log, getEmpresaId

import threading
import re

app = Flask(__name__)

EXECUTING = [False]
ERROR = None

@app.route('/activate', methods=['POST'])
def activate():
    global EXECUTING
    global ERROR
    
    email = request.json.get('email')
    password = request.json.get('password')
    link = request.json.get('link')
    startDate = request.json.get('start_date')
    finalDate = request.json.get('final_date')

    date_pattern = r'\d{2}/\d{2}/\d{4}'

    if EXECUTING[-1] == False:
        if re.match(date_pattern, startDate) and re.match(date_pattern, finalDate):
            id = getEmpresaId(email, password)

            if id:
                EXECUTING.append(True)

                thread = threading.Thread(target=do_scraping, args=(EXECUTING, email, password, link, id, startDate, finalDate))
                thread.start()

                response = {"message": "successfully started"}
                return jsonify(response), 200
        else:
            response = {"message": "Dates must be in dd/mm/yyyy format"}
            return jsonify(response), 400
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
    app.run(host='0.0.0.0', port=5001)
