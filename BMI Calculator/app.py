from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# BMI calculation route
@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # convert height to meters
    bmi = weight / (height * height)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
