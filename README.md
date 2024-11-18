# Boston_LR

<img src=https://i.imgur.com/WKQ0nH2.jpg height=350>

Building a model that can provide a price estimate based on a home's characteristics like:
* The number of rooms
* The distance to employment centres
* How rich or poor the area is
* How many students there are per teacher in local schools etc

<img src=https://i.imgur.com/WfUSSP7.png height=350>

## Project Overview:

    Developed a machine learning model to predict housing prices in Boston using a comprehensive dataset of features (e.g., crime rate, average rooms per dwelling, etc.).
    Applied log transformation to target variables to improve model performance and utilized PyCaret for automated model selection and hyperparameter tuning.
    Model Performance: Achieved a Relative RMSE of 0.67%, meaning the model's predictions were accurate to within $335 for a $50,000 house price.

## Key Highlights:

    Trained multiple regression models (e.g., Random Forest, Gradient Boosting, XGBoost) and selected the best model based on RMSE and R².
    Leveraged feature engineering, including log transformation of the target variable and cross-validation to tune hyperparameters and improve model generalization.
    Integrated FastAPI to serve the trained model via a RESTful API for easy consumption of predictions in web or mobile applications.

## Technologies & Tools:

    Programming Languages: Python (scikit-learn, PyCaret, FastAPI)
    Machine Learning: scikit-learn, PyCaret, XGBoost, RandomForest, Gradient Boosting
    Data Science Libraries: pandas, numpy, matplotlib, seaborn
    Model Deployment: Docker, Docker Compose, FastAPI
    Version Control: GitHub (for project management and collaboration)

## Deployment & Containerization:

    Dockerized the entire machine learning pipeline, including data preprocessing, model training, and the FastAPI server, to ensure reproducibility and ease of deployment.
    Used Docker Compose to manage multi-container applications, integrating the model container, FastAPI server, and any necessary services (e.g., databases or caching).
    The FastAPI framework was used to expose model predictions as API endpoints, making it easy to integrate into production systems for real-time predictions.
