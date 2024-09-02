# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of flowers
flowers = ["Rose", "Lily", "Tulip", "Daffodil", "Orchid", "Sunflower", "Daisy", "Lavender", "Marigold", "Jasmine"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    dob = request.form['dob']
    flower = random.choice(flowers)  # Randomly select a flower
    return render_template('result.html', name=name, flower=flower)

if __name__ == '__main__':
    app.run(debug=True)
