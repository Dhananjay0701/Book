import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)



# Check for environment variable
"""if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")"""

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://webyalyelxxaes:e4bccceb23edbafea866f15af8e9d89a453f1916b2967768dda5cc6d7074d656@ec2-52-207-25-133.compute-1.amazonaws.com:5432/d6i0qfpnql94j7")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    name = []
    name.append(request.form.get('name'))
    print(name)

if __name__ == "__main__":
    app.run(debug = True)