from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['image']
    img = Image.open(file)
    text = pytesseract.image_to_string(img)
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
