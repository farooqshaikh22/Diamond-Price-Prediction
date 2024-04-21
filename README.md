# Diamond Price Prediction Web Application
![Screenshot (6)](https://github.com/farooqshaikh22/Diamond-Price-Prediction/assets/127769353/6bb88ec2-14a6-450a-b462-45143d769e26)


## Overview

Welcome to the Diamond Price Prediction web application! This project offers a comprehensive solution for predicting diamond prices using machine learning techniques. The application provides functionalities for single-value prediction, batch prediction, and a robust training pipeline.

## Features

- **Single-Value Prediction**: Users can input specific diamond attributes and receive an instant price prediction.
- **Batch Prediction**: Upload CSV files containing multiple diamond records for batch prediction analysis.
- **Training Pipeline**: A complete pipeline for training machine learning models on diamond datasets, enabling continuous improvement of prediction accuracy.

## Technologies Used

- **Flask**: The web application framework used for building the user interface and handling HTTP requests.
- **Scikit-Learn**: Utilized for implementing machine learning models and data preprocessing.
- **Pandas**: Used for data manipulation and analysis.
- **Git**: Version control system employed for managing project iterations and collaboration.
- **Logging**: Comprehensive logging integrated to track application behavior and debug issues effectively.
- **Exception Handling**: Robust try-except blocks implemented to handle errors gracefully and ensure smooth application execution.
- **Modular Coding**: The project is structured using modular coding practices for enhanced readability, maintainability, and scalability.

## Directory Structure
```
.
├── Artifacts
│   ├── ingested_data
│   ├── transformed_data
│   └── trained_models
└── src
    ├── components
    │   └── __init__.py
    ├── config
    │   ├── __init__.py
    │   └── config.yaml
    ├── constants
    │   └── __init__.py
    ├── entity
    │   └── __init__.py
    ├── exception
    │   └── __init__.py
    ├── logger
    │   └── __init__.py
    ├── pipeline
    │   └── __init__.py
    └── utils
        └── __init__.py
├── .gitignore
├── app.py
├── main.py
├── schema.yaml
├── setup.py
└── README.md
```


## Usage

1. Clone the repository to your local machine using Git.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the web application through your browser at `http://localhost:5000`.

## Contributors

- [FARUQ SHAIKH](#): Project Lead and Developer

## License

This project is licensed under the [MIT License](#).




