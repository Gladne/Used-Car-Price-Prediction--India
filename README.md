# Used-Car-Price-Prediction--India
Predicting used car prices with machine learning using real-world vehicle data from India.

## Project Overview

This project focuses on building a **Machine Learning model to predict the selling price of used cars** based on several vehicle attributes such as brand, model, mileage, age, fuel type, and other characteristics.
The model is trained using historical car sales data and evaluates multiple features that influence vehicle value.

### The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Model training and evaluation
- Hyperparameter tuning
- Model comparison and final selection

### Dataset
The dataset contains car models, brands and selling price information, including:
- Car brand
- Car model
- Vehicle age
- Kilometers driven
- Maximum Engine Power',
- Car seats
- Selling Price (target variable)

## Project Workflow

The project follows a typical **machine learning pipeline**:

### Data Understanding

* Loaded and explored the dataset
* Checked dataset shape, types, and structure
* Generated statistical summaries

### Data Cleaning

* Verified missing values
* Removed unnecessary columns
* Ensured correct data types

### Exploratory Data Analysis (EDA)

Performed analysis to understand feature relationships:

* Distribution of car prices
* Relationship between mileage and price
* Impact of vehicle age
* Brand and model price variations

### Feature Engineering

Key transformations applied:
* Converted categorical variables into numerical form using:

  * **Target Encoding**
  * **One-Hot Encoding**

### Data Splitting

Dataset divided into:

* **Training set**
* **Testing set**

Typically using:

```
train_test_split()
```
### Model Training

Machine learning model used:

**Random Forest Regressor**

Key parameters used:

```
RandomForestRegressor(
    n_estimators=500,
    max_depth=12,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
```

Random Forest was chosen because it:

* Handles non-linear relationships well
* Reduces overfitting through ensemble learning
* Works effectively with tabular datasets

### Model Evaluation

Model performance evaluated using:

* **Cross Validation**
* **Regression metrics**
    - Mean Absolute Error (MAE)
    - Root Mean Squared Error (RMSE)
    - R² Score

Example cross-validation output:

```
Cross Validation Scores:
[-0.1234, -0.1212, -0.1158, -0.1177, -0.1160]

Mean CV Score:
-0.1188
```

This indicates the model's stability across multiple folds.

### Technologies Used
Python, Pandas, NumPy, Matplotlib / Seaborn, Scikit-learn

## How to test the App
https://used-car-price-prediction--india-first-release.streamlit.app/

## How to Run the Project
git clone https://github.com/Gladne/Used-Car-Price-Prediction--India.git </br>
pip install pandas numpy matplotlib seaborn scikit-learn </br>
jupyter notebook
