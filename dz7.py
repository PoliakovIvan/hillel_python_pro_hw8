from flask import Flask
from flask import request
from datetime import datetime
import random
from random import choice
import string

app = Flask(__name__)

@app.route("/")
def s():
    a = 'code'
    return a

@app.route("/whoami/")
def whoami():
    ip_address = request.remote_addr
    brow = request.headers
    brow = brow.get('Sec-Ch-Ua')
    brow = brow.split(";")
    brow = brow[0]
    now = datetime.now()
    return f"<p>Browser: {brow}</p>" \
        f'<p>Ip user: {ip_address}</p> ' \
        f'<p>Ip user: {now}</p> '


@app.route("/source_code/")
def source_code():
    code = open('dz7.py', 'r')
    return code


@app.route("/random", methods = ["POST", "GET"])
def task_random():
    length = request.args.get('length', type=int)
    specials = request.args.get('specials', type=int)
    digits = request.args.get('digits', type=int)
    letters = ''

    if specials == 1 and digits == 0:
        letters = letters.join(string.ascii_lowercase + string.punctuation)
    elif specials == 0 and digits == 0:
        letters = letters.join(string.ascii_lowercase)
    elif specials == 1 and digits == 1:
        letters = letters.join(string.ascii_lowercase + string.punctuation + string.digits)
    elif specials == 0 and digits == 1:
        letters = letters.join(string.ascii_lowercase + string.digits)

    rand_string = ''.join(random.choice(letters) for i in range(length))
    return f"<p>{rand_string}</p>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')