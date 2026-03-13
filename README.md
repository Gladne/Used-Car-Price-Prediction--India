# Used-Car-Price-Prediction--India
Predicting used car prices with machine learning using real-world vehicle data from India.

# The project includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Model training and evaluation
- Hyperparameter tuning
- Model comparison and final selection

# Dataset
The dataset contains car models, brands and selling price information, including:
- Car brand
- Car model
- Vehicle age
- Kilometers driven
- Maximum Engine Power',
- Car seats
- Selling Price (target variable)

# Exploratory Data Analysis</h4>

__Correlation Analysis__ <br>
A correlation heatmap was used to examine the relationships among the variables in the dataset. The analysis revealed a moderate positive correlation between the features *vehicle_age* and *km_driven*. Highly correlated features may introduce redundancy and potentially contribute to model overfitting during training.

Furthermore, the correlation analysis identified *max_power* as one of the most influential variables affecting the selling price, exhibiting a strong positive correlation with the target variable. This suggests that vehicles with higher engine power tend to have higher resale values.

__Features affecting Selling Price__ <br>
Based on exploratory data analysis, three key features were identified as having a significant influence on the selling price of used cars:
- Maximum engine power (*max_power*)
- Car brand
- Car model

Other available features were retained to allow the machine learning models to automatically learn additional patterns in the data. However, the *car_name* column was removed because it contains information closely related to the car model, which could lead to data leakage or overfitting.

# Encoding Categorical features

Two encoding techniques were used to transform categorical variables into numerical representations:

- __One-Hot Encoding__ was applied to the brand feature.
- __Target Encoding__ was applied to the model feature.

These encoding techniques allowed the models to effectively incorporate categorical information while maintaining computational efficiency.

# Feature Scaling

Feature scaling was applied selectively based on the requirements of each machine learning algorithm.

Scaling was necessary for the Linear Regression model because it is sensitive to differences in feature magnitude. Without scaling, features with larger numerical ranges may dominate the model and negatively affect coefficient estimation.

In contrast, tree-based models such as Decision Tree, Random Forest, and XGBoost do not require feature scaling. These algorithms split data based on decision thresholds rather than feature magnitude or distance, making them invariant to the scale of input variables.

# Modelling and Evaluation

The following machine learning models were implemented in this study:

- RandomForestRegressor
- DecisionTreeRegressor
- XGBRegressor
- LinearRegression

Model performance was evaluated using the following regression metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Since the dataset is relatively small, cross-validation was applied during model training to improve model reliability and ensure better generalization performance. Cross-validation allows the model to learn from multiple training subsets of the data, thereby reducing the risk of overfitting.

The experimental results indicate that tree-based ensemble models, particularly Random Forest and XGBoost, outperform Linear Regression. This is because ensemble tree models are capable of capturing nonlinear relationships and complex interactions between variables, which are common in real-world pricing data such as used car markets.

### Technologies Used
Python, Pandas, NumPy, Matplotlib / Seaborn, Scikit-learn

## How to test the App
https://used-car-price-prediction--india-first-release.streamlit.app/

## How to Run the Project
git clone https://github.com/Gladne/Used-Car-Price-Prediction--India.git </br>
pip install pandas numpy matplotlib seaborn scikit-learn </br>
jupyter notebook
