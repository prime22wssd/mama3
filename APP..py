from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def gracias_mama():
    return render_template('gracias_mama.html')

if __name__ == '__main__':
    app.run(debug=True)
