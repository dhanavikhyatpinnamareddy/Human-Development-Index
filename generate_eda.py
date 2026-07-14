import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set styles for premium look
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Roboto', 'Arial']

# Load data
df = pd.read_csv('datasets/processed/hdi_cleaned.csv')
out_dir = 'app/static/img/eda/'

# 1. Target Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['hdi'], bins=30, kde=True, color='#1a73e8')
plt.title('Distribution of Human Development Index (Target)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('HDI Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'hdi_dist.png'), dpi=300)
plt.close()

# 2. Correlation Heatmap
plt.figure(figsize=(8, 6))
cols = ['life_expectancy', 'expec_yr_school', 'mean_yr_school', 'log_gross_inc_percap', 'hdi']
corr = df[cols].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".3f", linewidths=.5)
plt.title('Pearson Correlation Matrix', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'correlation.png'), dpi=300)
plt.close()

# 3. Life Expectancy vs HDI
plt.figure(figsize=(8, 5))
sns.scatterplot(x='life_expectancy', y='hdi', data=df, color='#34a853', alpha=0.6)
plt.title('Life Expectancy vs. HDI', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Life Expectancy (Years)', fontsize=12)
plt.ylabel('HDI Score', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'life_exp_scatter.png'), dpi=300)
plt.close()

# 4. GNI Distribution (Before Log vs After Log) - We only have log in cleaned dataset usually, let's check
if 'gross_inc_percap' in df.columns and 'log_gross_inc_percap' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(df['gross_inc_percap'], bins=30, ax=axes[0], color='#ea4335')
    axes[0].set_title('Raw GNI (Heavily Skewed)', fontweight='bold')
    axes[0].set_xlabel('GNI Per Capita ($)')
    
    sns.histplot(df['log_gross_inc_percap'], bins=30, ax=axes[1], color='#fbbc05')
    axes[1].set_title('Log GNI (Normalized)', fontweight='bold')
    axes[1].set_xlabel('Log(GNI Per Capita)')
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'gni_transform.png'), dpi=300)
    plt.close()
else:
    # Just do a scatter of Log GNI vs HDI
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='log_gross_inc_percap', y='hdi', data=df, color='#ea4335', alpha=0.6)
    plt.title('Log GNI vs. HDI', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Log GNI Per Capita', fontsize=12)
    plt.ylabel('HDI Score', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'gni_transform.png'), dpi=300)
    plt.close()

print("EDA plots generated successfully.")
