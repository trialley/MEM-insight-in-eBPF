from flask import Flask

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/<path:path>')
def hello_world(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80',debug=True)