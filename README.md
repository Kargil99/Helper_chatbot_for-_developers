# AI Career Chatbot

An AI-powered chatbot that assists users in exploring career opportunities, choosing appropriate tech stacks, and discovering roadmaps for technology roles. This chatbot project is designed to help both students and professionals seeking guidance in the tech industry.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Files](#project-files)
- [Error Handling](#error-handling)
- [Future Improvements](#future-improvements)

## Features

- **Career Guidance**: Provides information on choosing career paths in technology.
- **Tech Stack Advice**: Recommends relevant technologies for front-end, back-end, and full-stack development.
- **Roadmap Assistance**: Offers step-by-step roadmaps for skills in web development, data science, and more.
- **Natural Language Processing**: Uses machine learning and NLP to understand user questions.

## Project Structure
ai_career_chatbot/ ├── app/ │ ├── templates/ │ │ └── index.html │ ├── static/ │ │ ├── styles.css │ │ └── script.js │ ├── main.py ├── models/ │ ├── my_model.keras │ └── tokenizer.pickle ├── nlp/ │ ├── intent_model.py │ ├── nlp_model.py │ └── train_model.py ├── data/ │ └── intents.json └── README.md


- `app/`: Contains the Flask application files, including HTML templates and static assets.
- `models/`: Stores trained machine learning models and tokenizers.
- `nlp/`: Contains code for training and deploying the NLP model.
- `data/`: Holds training data (e.g., intents.json).

## Setup and Installation

### Prerequisites

- Python 3.6+
- TensorFlow, Keras, Flask, Scikit-learn, Pandas
- Recommended: Virtual environment (e.g., Conda or venv)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai_career_chatbot.git
   cd ai_career_chatbot

Create a Virtual Environment

bash
Copy code
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Train the Model (Optional)

To train your own intent classification model, run train_model.py in the nlp/ directory:

bash
Copy code
python nlp/train_model.py
Run the Application

bash
Copy code
python app/main.py
Access the Chatbot

Open your browser and go to http://127.0.0.1:5000 to interact with the chatbot.

Usage
Enter a question about career advice, tech stack suggestions, or roadmap information.
The chatbot will respond with relevant guidance based on predefined intents.
Project Files
main.py: The main file for running the Flask application.
intent_model.py: Handles intent classification for user inputs.
nlp_model.py: Manages the chatbot’s response model.
train_model.py: Script for training the chatbot’s intent recognition model.
intents.json: Contains training data for various intents.
Error Handling
During development, a few common errors might arise:

Model File Not Found: Ensure my_model.keras and tokenizer.pickle are saved in the models/ directory.
Flask Endpoint Issues: Match endpoint names in main.py and script.js.
CSS and JavaScript Loading Errors: Verify paths for assets in static/ directory.
Debugging AJAX Requests: Ensure that get-response endpoint matches both in Flask and JavaScript.
Refer to the error messages in the console for more specific troubleshooting.

Future Improvements
Add More Intents: Include additional intents for other career-related queries.
Enhance NLP Model: Integrate a more sophisticated NLP model, such as BERT, for improved accuracy.
Expand Responses: Add more detailed and varied responses for each topic.
License
This project is licensed under the MIT License.
