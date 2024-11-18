# Boston Housing Price Prediction Model with Docker & FastAPI

<img src=https://i.imgur.com/WKQ0nH2.jpg height=350>

Building a model that can provide a price estimate based on a home's characteristics like:
* The number of rooms
* The distance to employment centres
* How rich or poor the area is
* How many students there are per teacher in local schools etc

<img src=https://i.imgur.com/WfUSSP7.png height=350>



## Project Overview:

    Developed a machine learning model to predict Boston housing prices, using a dataset containing features like crime rate, average number of rooms, and proximity to employment centers.
    Log transformation was applied to the target variable (price) to normalize skewed data and improve model performance.
    Trained a Gradient Boosting Regressor (GBR) model using PyCaret and fine-tuned it with cross-validation and hyperparameter optimization.
    Achieved a significant performance improvement in model accuracy:
        Relative RMSE improved from 1.548% (without log transformation) to 0.67% (with log transformation), demonstrating the effectiveness of the transformation in reducing prediction error.

## Key Highlights:

    Trained and compared multiple regression models (e.g., Random Forest, Gradient Boosting, XGBoost) and selected the best-performing model using RMSE and R².
    Leveraged PyCaret for automated machine learning tasks, including feature selection, model comparison, and hyperparameter tuning.
    Used FastAPI to expose the trained model as an API, enabling real-time predictions for new housing data.

## Technologies & Tools:

    Programming Languages: Python (scikit-learn, PyCaret, FastAPI)
    Machine Learning: scikit-learn, XGBoost, RandomForest, Gradient Boosting
    Data Science Libraries: pandas, numpy, matplotlib, seaborn
    Model Deployment: Docker, Docker Compose, FastAPI
    Version Control: GitHub (for project management and collaboration)

## Deployment & Containerization:

    Dockerized the entire pipeline, including data preprocessing, model training, and the FastAPI server for serving predictions.
    Used Docker Compose to manage multi-container applications, integrating the model container, FastAPI server, and any necessary services (e.g., databases).
    Exposed the trained model through a FastAPI server, allowing seamless integration with front-end applications or other services for real-time predictions.
