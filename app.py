from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="templates")

with open('rain_pred_final.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home(): 
    return render_template('rainfall_predict.html', **locals())

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        try:
            # Convert form values to float
            rainfall = float(request.form['rainfall'])
            sunshine = float(request.form['sunshine'])
            windGustSpeed = float(request.form['windgustspeed'])
            humidity3pm = float(request.form['humidity3pm'])
            pressure3pm = float(request.form['pressure3pm'])
            cloud9am = float(request.form['cloud9am'])
            cloud3pm = float(request.form['cloud3pm'])
            rainToday = float(request.form['raintoday'])

            # Make prediction
            prediction = model.predict([[rainfall, sunshine, windGustSpeed, humidity3pm, pressure3pm, cloud9am, cloud3pm, rainToday]])
            output = int(prediction[0])

            # Render templates based on the prediction
            if output == 1:
                return render_template("Rainfall.html")
            else:
                return render_template("Sunny.html")

        except ValueError:
            # Handle the case where form values are not valid floats
            return render_template("error.html", error_message="Invalid input. Please enter numeric values.")
    
    return render_template("Rainfall_predict.html")

if __name__ == '__main__':
    app.run(debug=True)
