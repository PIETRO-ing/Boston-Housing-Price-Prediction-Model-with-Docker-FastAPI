# Boston_LR

<img src=https://i.imgur.com/WKQ0nH2.jpg height=350>

Building a model that can provide a price estimate based on a home's characteristics like:
* The number of rooms
* The distance to employment centres
* How rich or poor the area is
* How many students there are per teacher in local schools etc

<img src=https://i.imgur.com/WfUSSP7.png height=350>

To accomplish the task I will:

1. Analyse and explore the Boston house price data
2. Split the data for training and testing
3. Run a Multivariable Regression
4. Evaluate the model's coefficients and residuals
5. Use data transformation to improve the model performance
6. Use the model to estimate a property price
7. Dockerize the model
8. Deploy the model in an app


sudo docker build -t jupyter . && sudo docker run -it --rm -p 8888:8888 --mount src="$(pwd)",target=/app,type=bind jupyter

* build the image with all the requirements
* run a container 
* access to jupyter lab
* work on the file inside the continer and see the change in my local directory outside the container
