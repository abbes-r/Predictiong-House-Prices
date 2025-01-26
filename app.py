import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
sc = pickle.load(open('models/scaler.pkl', 'rb'))
model = pickle.load(open('models/xgb_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print(request.args)
    int_features = [int(x)for x in request.form.values()]
    df = pd.DataFrame([int_features], columns=['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
                                               'guestroom', 'basement', 'airconditioning', 'parking', 'prefarea'])
   
    features_to_standardize = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    df[features_to_standardize] = sc.transform(df[features_to_standardize])
    prediction = model.predict(df)
    
    output = f"Based on its characteristics, the estimated value of this house is {np.round(prediction[0])} $."

    return render_template('index.html', prediction_text=output)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    df = pd.DataFrame([list(data.values())], columns=['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
                                               'guestroom', 'basement', 'airconditioning', 'parking', 'prefarea'])
    features_to_standardize = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    df[features_to_standardize] = sc.transform(df[features_to_standardize])
    prediction = model.predict(df)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)