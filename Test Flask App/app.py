from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('site.html')

if __name__ == '__main__':
    print("Starting your application...")
    app.run(host='127.0.0.1', debug=True)
