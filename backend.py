from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        form_data = request.form
        # Form verilerini konsola ve tarayıcıya yazdırın
        print("Gelen form verileri:", form_data)
        return render_template('submitted.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
