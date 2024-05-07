# OurGreenPlace_SeniorCapstone

## Contributors: 
This is a CS496 Capstone Project at Loyola University Maryland created by Alexandra Gardner and Aliyah Smith-Bradley. Our client is Professor David Gordon of Loyola University Maryland.

## Project Description
Our client, David Gordon’s, main concern for the project centers around deforestation. As an environmentalist, Professor Gordon emphasized the importance of spreading awareness about deforestation and
the struggle to find locations that are considered ”green”. Our web application will focus on raising
awareness about deforestation and highlighting areas in Maryland that are green, such as hiking trails,
parks, gardens, and more.

## Installation Instructions
Our project is run utilizing Visual Studio. You must download the app and clone this git repository. Python and Flask must also be correctly installed.   

In the terminal of VS Code (Link: https://code.visualstudio.com/), type the following commands to create and activate the virtual environment, and install Flask: 

  $ python -m venv venv

  $ .\venv\Scripts\activate

  (venv) $ python -m pip install Flask 

If Flask does not work immediately, press cmd+p and type "Select Interpreter". Choose the correct interpreter and continue.   

The following software must be installed to run the program. For each installment, navigate to the terminal and enter the command: $ pip install [ your software ]. Please refer to the Requirements.txt file within the project for the most up-to-date information on installments. 

- Flask-Login
- Flask-SQLAlchemy
- folium
- python-dotenv
- requests
- Werkzeug

OurGreenPlace relies on an API, called TrailAPI (Link: https://rapidapi.com/trailapi/api/trailapi), to run successfully. To utilize this API, you must create an account on RapidAPI.com and input your personal information. Once you have created your account, you will need to put the specific API key that is attached to your account in a .gitignore file within VSCode. The key must be held in a variable called 'API_KEY'. Afterward, OurGreenPlace should run as expected.   

## How to Run
The web application can only be run by navigating to the file main.py under the main directory and clicking the play button in the top right corner of the screen. You may access the web application by cmd+clicking on the link in the terminal (most likely: http://127.0.0.1:5000). You should be automatically directed to the web application in your browser.    

## How to Test
To test the web application, make sure that Pytest has been properly installed on VS Code. This can be done by entering the following command into the terminal: $ pip install pytest. To test the code, simply type "pytest" into the terminal. This should automatically load the tests stored in the tests.py file and test the code within the web application. 

To test the line coverage within VS Code, you must download the Python library, Coverage.py. Install the library by entering the following commands into the terminal: 

  $ pip install coverage
  
  $ pip install pytest-cov
  
  $ pytest --cov=website 

The last command should test your web application and return a table within the terminal that breaks down the tests and how much of the code has been covered. If you would like to see a more detailed report of the test coverage, you can generate an HTML file that will show you exactly which lines are not covered within the web app. A new folder will be generated containing the report by entering the following command into the terminal: $ pytest --cov=website --cov-report html. Open the index.html file within this folder to see which lines the tests have not covered. 
