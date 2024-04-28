# Sentiment Analysis Web Application
### Overview
This project implements a sentiment analysis web application using Flask, NLTK for natural language processing, and a trained logistic regression model. The application allows users to input text, which is then processed to determine the sentiment (positive or negative) of the input text.

## Installation
**Clone the Repository:** Clone the repository to your local machine using Git:
```
git clone https://github.com/yourusername/sentiment-analysis.git
```
**Navigate to Project Directory:** Change your current directory to the project directory:
```
cd sentiment-analysis
```
**Install Dependencies:** Install the required dependencies by running:
```
pip install -r requirements.txt
```
### Usage
**Run the Flask Application:** Start the Flask application by running the following command:
```
python app.py
```
**Access the Application:** Open a web browser and navigate to http://localhost:5000 to access the sentiment analysis web application.\
**Input Text:** Enter the text you want to analyze into the input field provided on the web page.\
**View Results:** The application will display the predicted sentiment (positive or negative) for the input text.
# Key Components:
### 1. Data Preprocessing:
* Cleaning and preprocessing raw text data by removing noise (e.g., URLs, special characters).
* Tokenization to split text into individual words (tokens).
* Stopword removal to filter out common words (e.g., "the", "is") that don't contribute to sentiment analysis.
* Lemmatization to convert words to their base or root form (e.g., "running" to "run").
### 2. Model Loading and Prediction:
* Loading a pre-trained Logistic Regression model (loaded_model) and a vectorizer (loaded_vectorizer) from saved files.
* Processing a given text input (test_string) using the defined preprocessing functions (process_tweet and list_to_string).
* Transforming the preprocessed text into a numerical vector using the loaded vectorizer (test_vector).
* Making sentiment predictions (prediction) using the loaded Logistic Regression model.
* Mapping the predicted sentiment label (0 or 1) to human-readable sentiment (Negative or Positive).

# Tools and Technologies:
### Python Libraries:
* **Flask:** Web framework for creating RESTful APIs (used for deployment).
* **pickle:** Python object serialization library used for saving and loading machine learning models.
* **nltk:** Natural Language Toolkit for NLP tasks (e.g., tokenization, lemmatization).
* **scikit-learn:** Machine learning library for building and training models.

# Outcome:
The outcome of this Sentiment Analysis project includes:

### Sentiment Prediction API:
Developing a Flask-based API that can receive text inputs and return sentiment predictions (Negative or Positive).
Integration with Frontend or Applications:
Integrating the sentiment analysis model into frontend applications or other systems that require sentiment analysis capabilities.
### Real-time Sentiment Analysis:
Providing real-time sentiment analysis for user-generated text inputs (e.g., social media posts, customer feedback).
### Scalable Deployment:
Deploying the sentiment analysis system to a production environment (e.g., cloud platform) for scalable and reliable usage.
