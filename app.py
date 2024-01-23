from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder="templates")


with open('rain_pred_final.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def home(): 
    return render_template('rainfall_predict.html', **locals())


@app.route("/predict",methods=['GET', 'POST'])
def predict():
	if request.method == "POST":
		# Rainfall
		rainfall = float(request.form['rainfall'])
		# Sunshine
		sunshine = float(request.form['sunshine'])
		# Wind Gust Speed
		windGustSpeed = float(request.form['windgustspeed'])
		# Humidity 3pm
		humidity3pm = float(request.form['humidity3pm'])
		# Pressure 3pm
		pressure3pm = float(request.form['pressure3pm'])
		# Cloud 9am
		cloud9am = float(request.form['cloud9am'])
		# Cloud 3pm
		cloud3pm = float(request.form['cloud3pm'])
		# Rain Today
		rainToday = float(request.form['raintoday'])

		prediction = model.predict([[rainfall , sunshine ,windGustSpeed , humidity3pm , pressure3pm , cloud9am , cloud3pm ,
					 rainToday]])
		output = int(prediction[0])
		if output == 1:
			return render_template("Rainfall.html")
		else:
			return render_template("Sunny.html")
	return render_template("Rainfall_predict.html")

if __name__=='__main__':
	app.run(debug=True)