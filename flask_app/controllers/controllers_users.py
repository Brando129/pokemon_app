from flask_app import app
from flask import render_template


# Get routes
# Index route
@app.get('/')
def index():
    return render_template('index.html')
