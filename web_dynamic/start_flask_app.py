# Script: start_flask_app.py

import os
import shutil
from uuid import uuid4
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/0-hbnb/')
def hbnb():
    cache_id = str(uuid4())
    return render_template('0-hbnb.html', cache_id=cache_id)

if __name__ == '__main__':
    # Check if the source directory exists before copying
    if os.path.exists('web_flask/static'):
        # Copy files to web_dynamic folder
        shutil.copytree('web_flask/static', 'web_dynamic/static')

    # Check if the source file exists before copying
    if os.path.exists('web_flask/templates/100-hbnb.html'):
        shutil.copy('web_flask/templates/100-hbnb.html', 'web_dynamic/templates/0-hbnb.html')

    # Check if the source file exists before copying
    if os.path.exists('web_flask/__init__.py'):
        shutil.copy('web_flask/__init__.py', 'web_dynamic/')

    # Check if the source file exists before copying
    if os.path.exists('web_flask/100-hbnb.py'):
        shutil.copy('web_flask/100-hbnb.py', 'web_dynamic/0-hbnb.py')

    # Set environment variables
    os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
    os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
    os.environ['HBNB_MYSQL_HOST'] = 'localhost'
    os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
    os.environ['HBNB_TYPE_STORAGE'] = 'db'

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)

