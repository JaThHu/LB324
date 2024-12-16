from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Lese die beiden Zahlen aus den Formularfeldern
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            summe = num1 + num2
            return render_template('index.html', summe=summe)
        except ValueError:
            error_message = "Bitte gib gültige Zahlen ein!"
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
