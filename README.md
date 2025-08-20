# Comparative Analysis of Heart Disease Datasets with Logistic Regression and Random Forest

## Project Overview
This project performs a comparative analysis of two independent **heart disease datasets**.  
The main objectives are:
- Identify and evaluate **risk factors** for heart disease.
- Conduct **statistical hypothesis testing** (Shapiro-Wilk, Mann-Whitney U, etc.).
- Train and compare **Logistic Regression** and **Random Forest** models.
- Assess model performance using **accuracy, precision, recall, F1-score, ROC curve, and AUC**.
- Provide a **comparative evaluation** of both datasets and models to highlight trade-offs between interpretability and predictive power.

The project follows a clean research workflow with reproducibility in mind.

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
  - `09_error_analysis.ipynb` – error and misclassification review  
  - `10_final_report.ipynb` – consolidated conclusions  

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
