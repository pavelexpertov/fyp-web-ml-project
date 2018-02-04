from flask import Flask, request

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='development key'
    ))

@app.route('/')
def serve_spa():
    '''Serving the single page application to a client'''
    return app.send_static_file('index.html')
