# Build Your First Machine Learning Web App (No Experience Needed!)

Have you ever wanted to build a Machine Learning application but felt overwhelmed by all the complex terminology, frameworks, and tools? You are not alone!

Today, we are going to build a **Human Development Index (HDI) Predictor** from scratch. The HDI is a score that measures how well a country is doing based on health, education, and standard of living. We will build a web app where a user can type in these details, and our Machine Learning model will instantly predict the country's HDI score.

We will keep this **extremely simple**. No complex design frameworks, no confusing commands, and no advanced coding knowledge required. 

Let's get started.

---

## Step 1: Setting Up Your Computer

Before we write any code, we need to make sure your computer has the right tools.

1. **Install Python**: Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest version. **Important:** During installation on Windows, make sure to check the box that says **"Add Python to PATH"** before clicking Install.
2. **Create a Folder**: Right-click on your Desktop and create a new folder called `HDI_Project`. Open this folder.
3. **Open the Terminal / Command Prompt**:
   - **Windows**: Click the address bar inside your `HDI_Project` folder, type `cmd`, and press Enter.
   - **Mac/Linux**: Open the "Terminal" app, type `cd Desktop/HDI_Project` and press Enter.
4. **Install the Magic Libraries**: In the black terminal window, type the following command and press Enter. This downloads the code libraries we need:
   ```bash
   pip install flask scikit-learn numpy pandas
   ```

---

## Step 2: Training the Machine Learning Model

A Machine Learning model is basically a math formula that learns patterns from data. We need to train it so it knows how to predict HDI. Rather than just giving you a massive block of code to copy-paste, let's look at how it works.

Inside your `HDI_Project` folder, create a new file named `train_model.py`. Open it with any text editor (like Notepad or VS Code) and paste the following code:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

print("1. Creating data...")
# We create a tiny fake dataset.
# (In the real world, you would load this from an Excel file.)
data = {
    'life_expectancy': [70.5, 80.2, 55.3, 75.1],
    'expec_yr_school': [12.0, 16.5, 8.0, 14.2],
    'mean_yr_school': [9.0, 13.0, 4.5, 11.5],
    'log_gross_inc_percap': [9.5, 10.8, 7.2, 10.1],
    'hdi': [0.700, 0.900, 0.450, 0.800]
}
df = pd.DataFrame(data)
```
**What does this do?** `pandas` (abbreviated as `pd`) is a tool used to create tables of data. Here, we are creating a small table with 4 rows of mock data so our model has something to study. 

Next, add this to the bottom of the same file:

```python
print("2. Training model...")
# Our inputs (the details) and our output (the final score)
X = df[['life_expectancy', 'expec_yr_school', 'mean_yr_school', 'log_gross_inc_percap']]
y = df['hdi']

# The 'LinearRegression' is the brain. We tell it to study the data (.fit)
model = LinearRegression()
model.fit(X, y)
```
**What does this do?** We split our table into `X` (the questions) and `y` (the answers). Then, we bring in `LinearRegression`, which acts as the "brain". The `.fit(X, y)` command is where the actual learning happens!

Finally, add this to save your work:

```python
print("3. Saving the brain...")
os.makedirs("models", exist_ok=True)

# Save the trained model to a file so our website can use it later
with open("models/HDI.pkl", "wb") as file:
    pickle.dump(model, file)

print("Success! Model saved to models/HDI.pkl")
```
**What does this do?** Training a model can take a long time with real data, so we don't want to do it every time someone visits our website. We use a tool called `pickle` to save the model's memory into a file named `HDI.pkl`.

**Run the script:** Go back to your terminal and type:
```bash
python train_model.py
```
Look inside your folder! You will see a new folder called `models` containing `HDI.pkl`. 

---

## Step 3: Building the Web Server (Backend)

Now we need a web server to act as a bridge between the internet and our Machine Learning model. We will use a tool called **Flask**.

Create a new file called `app.py`. Paste this setup code at the top:

```python
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__) # Create the app

# Load the saved ML model from Step 2
with open('models/HDI.pkl', 'rb') as file:
    model = pickle.load(file)
```
**What does this do?** This initializes our website and loads the `HDI.pkl` brain we created earlier. 

Now, let's add the code that handles what happens when a user visits the website. Add this below:

```python
# The Home Page
@app.route('/')
def home():
    return render_template('index.html')

# The Prediction Page
@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get the numbers the user typed into the website
    life = float(request.form['life_expectancy'])
    expec_school = float(request.form['expec_yr_school'])
    mean_school = float(request.form['mean_yr_school'])
    gni = float(request.form['gross_inc_percap'])
    
    # 2. Ask the ML model to predict based on those numbers
    log_gni = np.log(gni) if gni > 0 else 0
    features = np.array([[life, expec_school, mean_school, log_gni]])
    prediction = model.predict(features)[0]
    
    # 3. Send the result to the result page
    return render_template('result.html', score=round(prediction, 3))

if __name__ == '__main__':
    app.run(debug=True)
```
**What does this do?** `@app.route` tells the server what to do for specific URLs. The `/` route just shows the home page. The `/predict` route grabs the information the user typed in, asks the model to predict the HDI score, and passes that score to the `result.html` page.

---

## Step 4: Creating the Web Pages (Frontend)

Finally, we need to create the visual web pages. We will use pure HTML to keep things simple.

1. Inside your `HDI_Project` folder, create a new folder named `templates`. **(It must be named exactly `templates`)**.
2. Inside the `templates` folder, create a file named `index.html`.

Paste this code into `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>HDI Predictor</title>
</head>
<body style="text-align: center; font-family: Arial, sans-serif; margin-top: 50px;">

    <h1>Human Development Index Predictor</h1>
    <p>Enter the details below to predict a country's development score.</p>

    <!-- The form sends data to our /predict route in Python -->
    <form action="/predict" method="POST">
        <p>
            <label>Life Expectancy (Years):</label><br>
            <input type="number" step="any" name="life_expectancy" required>
        </p>
        <p>
            <label>Expected Years of Schooling:</label><br>
            <input type="number" step="any" name="expec_yr_school" required>
        </p>
        <p>
            <label>Mean Years of Schooling:</label><br>
            <input type="number" step="any" name="mean_yr_school" required>
        </p>
        <p>
            <label>Gross National Income per Capita ($):</label><br>
            <input type="number" step="any" name="gross_inc_percap" required>
        </p>
        <button type="submit" style="padding: 10px 20px; font-size: 16px;">Predict Score!</button>
    </form>

</body>
</html>
```
**What does this do?** The `<form action="/predict" method="POST">` is the most important part. It tells the browser, "When the user clicks submit, grab all these inputs and send them securely to our `/predict` URL in Python."

3. Inside the same `templates` folder, create another file named `result.html` and paste this code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Prediction Result</title>
</head>
<body style="text-align: center; font-family: Arial, sans-serif; margin-top: 50px;">

    <h1>Prediction Complete!</h1>
    
    <!-- The {{ score }} tag is where Python injects our prediction -->
    <h2>The predicted HDI Score is: <strong>{{ score }}</strong></h2>
    
    <p>(Scores are between 0 and 1. Closer to 1 means higher development!)</p>

    <br>
    <a href="/" style="padding: 10px 20px; background-color: #ddd; text-decoration: none; color: black; border-radius: 5px;">Go Back</a>

</body>
</html>
```
**What does this do?** Remember `return render_template('result.html', score=...)` from our Python code? The `{{ score }}` syntax is how HTML receives that number from Python and displays it!

---

## Step 5: Run Your App!

You are finished! Let's turn it on.

1. Go back to your terminal window (which should still be pointing at your `HDI_Project` folder).
2. Type the following command to start the web server:
   ```bash
   python app.py
   ```
3. Open your web browser (Chrome, Safari, Edge) and go to **`http://127.0.0.1:5000`**

**Congratulations!** You should see your web page. Try typing in some numbers (like Life Expectancy: 75, Expected School: 14, Mean School: 11, Income: 20000) and click the predict button. 

You have just successfully trained a Machine Learning model and served it on the internet!
