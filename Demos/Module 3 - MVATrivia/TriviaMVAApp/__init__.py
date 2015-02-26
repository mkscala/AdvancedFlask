# Get flask
from flask import Flask;

# Create the app
app = Flask(__name__);

# Load the controller
import TriviaMVAApp.views;