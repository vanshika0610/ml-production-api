# ML Production API

A simple machine learning API built using FastAPI and Docker for the "Getting Started with ML in Production" workshop.

## Model

This project uses a Random Forest Classifier trained on the Iris dataset.

The model predicts the species of an Iris flower based on these four features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The possible predictions are:

- Setosa
- Versicolor
- Virginica

## API Endpoint

### POST `/predict`

Example request:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}