import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle
import os

def train_and_evaluate():
    print("Loading cleaned dataset...")
    df = pd.read_csv("../../datasets/processed/hdi_cleaned.csv")
    
    # Define features and target
    features = ['life_expectancy', 'expec_yr_school', 'mean_yr_school', 'log_gross_inc_percap']
    target = 'hdi'
    
    X = df[features]
    y = df[target]
    
    # Train/Test Split
    print("Splitting data into 80% train and 20% test...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and Train Model
    print("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Evaluate
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    print("-" * 30)
    print("Model Evaluation Metrics:")
    print(f"R2 Score: {r2:.4f}")
    print(f"MAE:      {mae:.4f}")
    print(f"MSE:      {mse:.4f}")
    print(f"RMSE:     {rmse:.4f}")
    print("-" * 30)
    
    # Save the model
    os.makedirs("../../models", exist_ok=True)
    model_path = "../../models/HDI.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved successfully to {model_path}")
    
    # Generate Actual vs Predicted Scatter Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='b')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("Actual HDI")
    plt.ylabel("Predicted HDI")
    plt.title("Actual vs Predicted HDI (Linear Regression)")
    
    os.makedirs("../../reports", exist_ok=True)
    plot_path = "../../reports/actual_vs_predicted.png"
    plt.savefig(plot_path, bbox_inches="tight")
    print(f"Scatter plot saved to {plot_path}")

if __name__ == "__main__":
    train_and_evaluate()
