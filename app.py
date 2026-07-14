from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'HDI.pkl')
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print("Warning: Model file not found. Ensure HDI.pkl exists in the models directory.")

def get_hdi_category(score):
    if score >= 0.800:
        return "Very High", "success"
    elif score >= 0.700:
        return "High", "info"
    elif score >= 0.550:
        return "Medium", "warning"
    else:
        return "Low", "danger"

@app.route('/')
def home():
    return render_template('home.html', current_page='home')

@app.route('/about')
def about():
    return render_template('about.html', current_page='about')

@app.route('/portal')
def portal():
    return render_template('portal.html', current_page='portal')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from form
            life_expectancy = float(request.form['life_expectancy'])
            expec_yr_school = float(request.form['expec_yr_school'])
            mean_yr_school = float(request.form['mean_yr_school'])
            gross_inc_percap = float(request.form['gross_inc_percap'])

            # Preprocess (log transform GNI per capita as per Phase 1-3)
            log_gross_inc_percap = np.log(gross_inc_percap) if gross_inc_percap > 0 else 0
            
            # Predict
            features = np.array([[life_expectancy, expec_yr_school, mean_yr_school, log_gross_inc_percap]])
            if model:
                prediction = model.predict(features)[0]
                prediction = min(max(prediction, 0.0), 1.0) # Clamp between 0 and 1
            else:
                prediction = 0.0 # Fallback if no model

            category, badge_class = get_hdi_category(prediction)
            
            return render_template('result.html', 
                                   prediction=round(prediction, 3),
                                   category=category,
                                   badge_class=badge_class,
                                   inputs={
                                       'Life Expectancy': life_expectancy,
                                       'Expected Years of Schooling': expec_yr_school,
                                       'Mean Years of Schooling': mean_yr_school,
                                       'GNI Per Capita': f"${gross_inc_percap:,.2f}"
                                   })
        except Exception as e:
            return render_template('predict.html', error=str(e), current_page='predict')

    return render_template('predict.html', current_page='predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
