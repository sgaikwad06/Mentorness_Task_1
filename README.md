## Predicting Salaries of Data Professionals

### Description :
The Salary Prediction Project is designed to predict salaries based on various input features using machine learning techniques. 
The project comprises two main components :

1. Jupyter Notebook (salary_prediction.ipynb) :
   - This notebook includes data analysis, preprocessing, model training, and evaluation steps.
   - It leverages various machine learning algorithms to predict salaries and compares their performance.
   - Detailed visualizations and explanations are provided to understand the data and the model's behavior.

2. Flask Application (app.py) :
   - This is a web application built using Flask, a lightweight web framework for Python.
   - The trained machine learning model is deployed through this application.
   - Users can input features via the web interface, and the application returns the predicted salary based on the model.
   - The application serves as a practical demonstration of how machine learning models can be integrated into web services.

### Features :
- Data Analysis :
  Comprehensive analysis of the dataset, including handling missing values, encoding categorical variables, and feature scaling.
  
- Model Training :
  Implementation of various regression algorithms such as Linear Regression, Decision Trees, and Random Forest.
  
- Model Evaluation :
  Evaluation metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to assess the model's performance.
  
- Web Deployment :
  A Flask-based web application that provides an interface for users to input data and receive salary predictions.
  
- User-friendly Interface :
  Easy-to-use web interface for making predictions without needing in-depth knowledge of the underlying machine learning model.
  
This project showcases the end-to-end process of developing a machine learning model, from data preprocessing and model training to deployment in a web application, making it a valuable resource for anyone interested in applied machine learning and web development.

### Usage :
#### Jupyter Notebook:
To explore the data and train the model, follow these steps :
1. Open the Jupyter Notebook 
2. Execute the cells in the notebook sequentially to:
     - Load and analyze the dataset.
     - Preprocess the data (handle missing values, encode categorical variables, scale features).
     - Train various machine learning models (e.g., Linear Regression, Decision Trees, Random Forest).
     - Evaluate the models' performance using metrics like Mean Absolute Error (MAE) and R-squared.
     - Visualize the results and understand the model's behavior.

#### Flask Application :
To run the Flask web application and use the model for making predictions :
1. Ensure you are in the project directory
2. Start the Flask application
3. Open your web browser and navigate
4. Use the web interface to input features and get a predicted salary. The application will use the trained model to provide the prediction based on the input data.

This setup allows you to interact with the machine learning model through a web application, making it easy to input data and obtain salary predictions without needing to run the notebook manually each time.

### Conclusion :
The Salary Prediction Project demonstrates how to build, train, and deploy a machine learning model for predicting salaries. It includes a Jupyter Notebook for data analysis and model training, and a Flask web application for user-friendly predictions. This project showcases the complete workflow from data preprocessing and model evaluation to web deployment, making it an excellent example of applying machine learning to real-world problems.
