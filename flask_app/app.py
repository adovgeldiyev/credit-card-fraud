from flask import render_template, Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homeRoute():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
