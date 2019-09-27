import os

from flask import Flask, send_from_directory

app = Flask(__name__,
            static_url_path='', 
            static_folder='./')

@app.route('/')
def root():
    return send_from_directory('./1_Introduction', 'index.html')

app.run(port=int(os.environ["CDSW_APP_PORT"]))