from flask import Flask, redirect, render_template
from pymongo import MongoClient

import pandas as pd
import numpy as np

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)