from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time
app = Flask(__name__)

@app.route('/')
def index2():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index2.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002,debug=True)
