# Weather Forecast Prediction using ANN

This project builds an Artificial Neural Network (ANN) to predict whether it will rain tomorrow based on historical weather data.
It uses datasets containing weather features such as temperature, humidity, wind, and pressure, and trains a binary classification model.

## Project Workflow

Data Loading & Merging
All .csv weather datasets are loaded and merged using pandas and glob.

## Feature Selection

Selected important features:
Location, MinTemp, MaxTemp, Rainfall, Wind-related features, Humidity, Pressure, Temperature, RainToday, RainTomorrow.

## Data Preprocessing

Shuffling the dataset.
Encoding categorical data (Location, Wind directions, RainToday).
Handling missing values with Imputer (mean strategy).
Feature scaling using StandardScaler.

## Model Building (ANN)

Built with Keras Sequential API:
Input layer (17 features).
Two hidden layers with ReLU activation.
Output layer with Sigmoid activation for binary classification.

Compiled with:
Optimizer: Adam

Loss: binary_crossentropy

Metric: accuracy

## Training

Model trained for 10 epochs with batch size = 10.

## Evaluation

Predictions made on the test set.
Classification threshold: 0.5.
Final accuracy score printed.

Example Training Log (Accuracy ~84%) <br>
Epoch 1/10 - loss: 0.3758 - acc: 0.8372 <br>
Epoch 5/10 - loss: 0.3623 - acc: 0.8437 <br>
Epoch 10/10 - loss: 0.3592 - acc: 0.8436 <br>

## Requirements

Python 3.6+
Libraries:
pandas
numpy
scikit-learn
keras / tensorflow
glob

Install dependencies:
pip install pandas numpy scikit-learn keras tensorflow

## How to Run

Place all weather dataset .csv files inside:
/WeatherForcast/DataSets/


Run the Python script:
python weather_forecast_ann.py


The script will:
Preprocess data, train an ANN model and print the final accuracy score.
