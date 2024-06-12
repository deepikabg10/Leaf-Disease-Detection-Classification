import misc

from flask import Flask, render_template, request
from markupsafe import Markup
from model import predict_image
from utils import save_file, delete_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            filename = save_file(file)
            prediction = predict_image(filename)
            print(prediction)
            delete_file(filename)
            res = Markup(misc.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except Exception as e:
            print(e)
    return render_template('index.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True)
