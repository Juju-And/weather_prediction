# Predict weather

This is a simple Python application intended to draw a linear regression line based on counted prediction.
Prediction was calculated based on the gradient descent algorithm and loss function.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install requirements.txt
```

### Installing

First step is to run the first file in order to generate pseudo-random weather data:

```
$ python3 generate_weather_to_csv.py
```

in order to have .png files created, run the second file;

```
$ python3 predict_weather.py
```

Ready plots in .png format can be found in the results folder.