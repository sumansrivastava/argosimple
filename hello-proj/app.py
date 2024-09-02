from flask import Flask

app = Flask(__name__)

@app.route('/')
def argo_success():
    return 'Hi Suman!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
