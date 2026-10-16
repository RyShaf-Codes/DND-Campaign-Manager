from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def home():
    campaigns = database.get_campaigns()
    return render_template("index.html", campaigns=campaigns)

@app.route("/campaign/<int:campaign_id>")
def campaign_page(campaign_id):
    campaign = database.get_campaign(campaign_id)
    players = database.get_players(campaign_id)
    npcs = database.get_npcs(campaign_id)
    locations = database.get_locations(campaign_id)
    notes = database.get_notes(campaign_id)

    return render_template(
        "campaign.html", 
        campaign = campaign,
        players = players,
        npcs = npcs,
        locations = locations,
        notes = notes
        )

if __name__ == "__main__":
    app.run(debug=True)

