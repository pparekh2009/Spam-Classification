from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('pipeline.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Website.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    print(request.form)

    email = request.form.get('email')
    print(email)

    string_feature = np.array([email])
    print(string_feature)

    prediction = model.predict(string_feature)
    print(prediction)

    try:
        if prediction == 0:
            return render_template('Website.html', pred="The email is not spam")
        else:
            return render_template('Website.html', pred="The email is spam")
    except ValueError:
        return 'Please enter valid values!'


if __name__ == '__main__':
    app.run(debug=True)
