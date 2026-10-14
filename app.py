from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def home():
    campaigns = database.get_campaigns()
    return render_template("index.html", campaigns=campaigns)

@app.route("/campaign/<int:campaign_id>")
def campaign_page(campaign_id):
    return f"Campaign ID: {campaign_id}"

if __name__ == "__main__":
    app.run(debug=True)

