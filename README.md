# Internal Controls
#### Demo: https://youtu.be/aAzwdLzFqH0
#### Description: 
This project is a full-stack web application designed to manage a company's internal controls. Users can add a control, specifying its name, description, rating, status, and date added. This application provides interactive filtering and data visualization by allowing users to visualize data by dynamically generating the appropriate visualization based on selected criteria. I used Bootstrap to make the user interface responsive and user-friendly. Other technologies used include: Flask, SQLAlchemy, SQLite, Matplotlib, and HTML/CSS/JS. 

env/ : This directory contains my virtual environment. Its purpose is to manage project dependencies. 

instance/ : This directory manages instance-specific configurations and data

static/ : This directory contains my custom CSS and JS. In this project, I wrote a CSS class to center images (static/css/styles.css), and used JavaScript to handle alerts and form validation (static/js/script.js). 

templates/ : This directory contains all of my HTML templates. I utilized inheritance by making a layout.html template, which links my custom CSS and JS, links Bootstrap CSS and JS, and provides a general structures for its child templates. add_control.html is a template displaying a form so that a user can add a control. index.html lists control names along with their descriptions. visualization.html provides a form so that a user can filter between criteria, then renders an image to visualize data.

app.py : This file serves as the main entry point for this application, defining routes, handling form submissions, and rendering templates. It allows users to add internal controls to a database, filter them based on criteria like rating, status, or date, and then visualize the filtered controls using various types of charts. The application uses SQLAlchemy to interact with a SQLite database, and Matplotlib to generate and display visualizations.

forms.py : This file defines the forms used in this application, specifically for adding new internal controls and filtering them for visualization. I used Flask-WTF to create classes for these forms. 

models.py : This file defines the database model for my application, and manages how data is structured.

requirements.txt : This file lists required packages necesasry for this application to run. Download by executing pip install -r requirements.txt

run.py : This file runs the application

Design contemplation: Initially, I wanted to use a bar graph to visualize all criteria (rating, status, date). After implementing this, I relaized that it didn't make much sense, as a bar graph only really makes sense for the rating criteria. So, I modified my app.py to render different visualizations depending on which criteria the user selects (bar graph for rating, pie chart for status, and timeline for date). In regards to the FilterForm, I realized that I did not want the start and end date fields displayed all the time, since these are only necessary when the user selects date as the criteria. So, I wrote some JS to manage the visibility of these fields, so that they only appear on the web page when the user has selected date as the criteria.

Usage: Naviate to the "Add Control" page to input new data. Navigate to the "Visualization" page to select filter criteria and visualize data. Navigate to the home page (Internal Controls) to see a list of all controls in the database accompanied by their descriptions.