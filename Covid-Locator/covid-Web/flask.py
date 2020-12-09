#import files
from flask import Flask, render_template, request, redirect, url_for
import requests
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)

@app.route("/")
def home():    
    return redirect(url_for('covid19'))

@app.route("/covid19", methods=["POST", "GET"])
def covid19():
  worldwide_data_url = "https://corona.lmao.ninja/v2/all"
  worldwide_content = requests.get(worldwide_data_url)
  worldwide_data = worldwide_content.json()
  return render_template("home.html", data=worldwide_data)

if __name__ == "__main__":    
    app.run(debug=True)
