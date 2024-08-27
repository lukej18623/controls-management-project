from flask import Flask, flash, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import ControlForm, FilterForm
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')  # don't need a GUI backend for this app
import matplotlib.pyplot as plt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///controls.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # disable modification tracking to improve performance

    db.init_app(app)

    with app.app_context():
        from models import Control

        @app.route('/')
        def index():
            # display list of internal controls and their descriptions
            controls = Control.query.all()
            return render_template('index.html', controls=controls)


        @app.route('/add_control', methods=['GET', 'POST'])
        def add_control():
            form = ControlForm()
            if form.validate_on_submit():
                # add new control to database
                new_control = Control(
                    name=form.name.data, 
                    description=form.description.data,
                    rating = form.rating.data,
                    status = form.status.data,
                    date = form.date.data
                )
                db.session.add(new_control)
                db.session.commit()
                return redirect(url_for('index'))
            return render_template('add_control.html', form=form)


        @app.route('/visualization', methods=['GET', 'POST'])
        def visualization():
            # visualize data based on selected criteria
            form = FilterForm()
            plot_url = None
            chart_type = None  # keep track of chart type; display in html template
            
            if form.validate_on_submit():
                criteria = form.criteria.data
                controls = []
                
                # sort controls based on rating in descending order
                if criteria == "rating":
                    controls = Control.query.order_by(Control.rating.desc()).all()

                elif criteria == "status":
                    controls = Control.query.all()

                # filter controls so they fall between start and end date, then sort selected controls
                elif criteria == "date":
                    start = form.start_date.data
                    end = form.end_date.data
                    if start and end:  
                        controls = Control.query.filter(Control.date >= start, Control.date <= end).order_by(Control.date.desc()).all()
                    else:
                        # alert user if start and end dates were not entered
                        return jsonify({'alert': 'Please provide both start and end dates for date filtering.'})

                
                # generate appropriate visualizations based off of selected criteria
                if controls:
                    if criteria == "rating":
                        # generate a bar chart
                        names = [control.name for control in controls]
                        ratings = [control.rating for control in controls]
                        plt.figure(figsize=(10, 6))
                        plt.bar(names, ratings)
                        plt.xlabel('Control Names')
                        plt.ylabel('Rating')
                        plt.title('Control Ratings')
                        chart_type = 'bar'

                    elif criteria == "status":
                        # generate a pie chart
                        statuses = [control.status for control in controls]
                        status_counts = {status.capitalize(): statuses.count(status) for status in set(statuses)}
                        plt.figure(figsize=(8, 8))
                        plt.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%')
                        plt.title('Control Status Distribution')
                        chart_type = 'pie'

                    elif criteria == "date":
                        # generate a timeline
                        names = [control.name for control in controls]
                        dates = [control.date for control in controls]
                        
                        plt.figure(figsize=(10, 6))
                        plt.plot(dates, names, marker='o', linestyle='-', color='b')
                        plt.gca().invert_yaxis()  # invert y-axis so the latest dates are on top
                        plt.xlabel('Date')
                        plt.ylabel('Control Names')
                        plt.title('Control Timeline')
                        plt.grid(True)  # add grid lines for better readability
                        chart_type = 'timeline'

                    # save plot to a BytesIO object and encode it as base64
                    img = BytesIO()
                    plt.savefig(img, format='png')
                    img.seek(0)
                    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
                    plt.close()
            
                    return render_template('visualization.html', form=form, plot_url=plot_url, chart_type=chart_type)
                            
            return render_template('visualization.html', form=form)
        
        return app