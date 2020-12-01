import jinja2
import os

from pprint import PrettyPrinter
from flask import Flask, request, render_template

################################################################################
## SETUP
################################################################################

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('data'),
])
app.jinja_loader = my_loader

pp = PrettyPrinter(indent=4)

################################################################################
## ROUTES
################################################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""

    return render_template('index.html') 


@app.route('/uploaddocs')
def uploaddocs():
    """Displays the homepage with forms for current or historical data."""
    
    sampleDataTitle = ["Medical Document 1", "Medical Document 2", "Medical Document 3",
                        "Medical Document 4", "Medical Document 5", "Medical Document 6"]

    sampleData = ["This is Medical Document 1", "This is Medical Document 2", 
                "This is Medical Document 3", "This is Medical Document 4", 
                "This is Medical Document 5", "This is Medical Document 6"]

    counter = 0 
    context = {
        'sampleData' : sampleData,
        'counter' : counter,
        'sampleDataTitle' : sampleDataTitle
    }

    return render_template('uploaddocs.html', **context)


@app.route('/features')
def features():
    """Displays the homepage with forms for current or historical data."""

    return render_template('features.html')


if __name__ == '__main__':
    app.run(debug=True)