# Random Name Generator

A simple web application that generates names randomly using a **Markov** model, based on existing lists of first and last names.

## Requirements

- Python  
- flask
- NLTK

## Installation
  # Step 1: Create a virtual environment (recommended)
  python -m venv venv  
  source venv/bin/activate        # On macOS/Linux  
  venv\Scripts\activate.bat       # On Windows  
  
  # Step 2: Install Flask
  pip install flask

  # Step 2: Install nltk
  pip install nltk

## Running the Application
  python run.py  
  Then open your browser in your termminal:  
        http://127.0.0.1:5003/  

## Project Structure
  random_name/  
  │  
  ├── app/                    # Core application logic  
  │   ├── __init__.py         # Flask app initialization  
  │   ├── data_loader.py      # Loads name data  
  │   ├── generator.py        # Random name generation  
  │   ├── routes.py           # Flask routes (web pages)  
  │   └── syllables.py        # Syllable handling  
  │  
  ├── data/                   # Name data files  
  │   ├── noms_famille.txt  
  │   ├── prenoms_filles.txt  
  │   └── prenoms_garcons.txt  
  │  
  ├── static/                 # CSS and JS assets  
  │   ├── css/style.css  
  │   └── js/script.js  
  │  
  ├── templates/              # HTML templates  
  │   └── index.html  
  │  
  ├── run.py                  # Main entry point  
  ├── scrap.py                # Name and family name scraping script  
  └── README.md  
