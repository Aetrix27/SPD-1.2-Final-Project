import jinja2

from pprint import PrettyPrinter
from flask import Flask, request, render_template

################################################################################
## SETUP
################################################################################

app = Flask(__name__)

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

    sampleData = ["This is Medical Document 1", "This is Medical Document 2"]

    context = {
        'sampleData' : sampleData
    }

    return render_template('uploaddocs.html', **context)


@app.route('/features')
def features():
    """Displays the homepage with forms for current or historical data."""

    return render_template('features.html')


if __name__ == '__main__':
    app.run(debug=True)