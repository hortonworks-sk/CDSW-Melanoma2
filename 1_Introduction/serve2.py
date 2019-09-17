from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/home/cdsw/1_Introduction')

app.run(host='0.0.0.0', port=8090)

@app.route('/')
def root():
    return app.send_static_file('index.html')