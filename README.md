# Comparative Analysis of Heart Disease Datasets with Logistic Regression and Random Forest

## Project Overview
This project performs a **comparative analysis of two independent heart disease datasets** and builds predictive models to evaluate risk factors.  
The analysis has two main goals:
- Explore and statistically compare **risk factors** across datasets.  
- Train and evaluate **Logistic Regression** (interpretability) and **Random Forest** (predictive power).  

Additionally, the project includes a **Gradio-based interface** that allows users to test predictions for new patients using a pre-trained Random Forest model.

---

## Key Features
- **Data Analysis & Preprocessing**: Cleaning, encoding, normalization, and feature engineering.  
- **Statistical Testing**: Shapiro-Wilk, Mann-Whitney U, and others to validate differences across groups.  
- **Modeling**: Logistic Regression & Random Forest trained on both datasets.  
- **Evaluation**: Accuracy, Precision, Recall, F1-score, ROC curve, and AUC.  
- **Comparative Insights**: Strengths/weaknesses of each dataset and model.  
- **Interactive Prediction App**: Gradio interface for predicting heart disease.  

---

## Folder Structure

- **`data/`**  
  Contains datasets and intermediate processed files.  
  - `dataset_1.csv`, `dataset_2.csv` – raw datasets  
  - `cleaned_data/`, `preprocessed_rf/` – processed data  
  - `stats_results/` – exported test results  

- **`images/`**  
  Stores plots and confusion matrices, separated by dataset:  
  - `dataset1_images/`  
  - `dataset2_images/`  

- **`notebooks/`**  
  Jupyter notebooks organized by workflow stage:  
  - `01_data_overview.ipynb` – dataset overview and descriptive statistics  
  - `02_preprocessing.ipynb` – data cleaning and preparation  
  - `03_eda_dataset_1.ipynb`, `04_eda_dataset_2.ipynb` – exploratory data analysis  
  - `05_stats_tests.ipynb` – statistical hypothesis testing  
  - `06_modeling_dataset_1_lr.ipynb`, `06_modeling_dataset_1_rf.ipynb` – Logistic Regression & Random Forest on Dataset 1  
  - `07_modeling_dataset_2_lr.ipynb`, `07_modeling_dataset_2_rf.ipynb` – Logistic Regression & Random Forest on Dataset 2  
  - `08_comparative_analysis.ipynb` – model comparison across datasets  
  - `09_final_report.ipynb`
  - `10_test_notebook.ipynb` 
  - `11_random_forest_ds1.ipynb` – Gradio app for real-time predictions  
  - `12_random_forest_ds2.ipynb` – Gradio app for real-time predictions  

- **`src/`**  
  Reusable Python functions and helpers:  
  - `overview_functions.py`  
  - `stats_tests_functions.py`  

- **`tests/`**  
  Unit tests for reproducibility and validation:  
  - `01_data_overview_unittests.py`  
  - `eda_dataset_functions_unittests.py`  

- **`requirements.txt`**  
  List of dependencies required to run the project.  

- **`README.md`**  
  Project description and usage instructions.  

- **`LICENSE`**  
  License file for the project.  

---

## Installation & Usage

To reproduce the analysis locally:

```bash
# Clone the repository
git clone https://github.com/plamensve/DS_FINAL_PROJECT.git
cd DS_FINAL_PROJECT

# Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Open Jupyter Notebook
jupyter notebook
