from flask import Flask, request, render_template
from parser.resume_parser import parse_resume

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            data = parse_resume(file)
            return render_template('result.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)