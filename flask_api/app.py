from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)


@app.route('/api/about', methods=['GET'])
def about():
    team_data = {
        "company": "District Events",
        "mission": "To revolutionize technology through innovation",
        "team": [
            {
                "name": "Moksh Aggarwal",
                "role": "Team Leader",
                "id": "2410993239",
                "bio": "Computer Science Engineering with specialization in AI",
                "avatar": "/static/avatars/moksh.jpg"
            },
            {
                "name": "Mayur Mittal", 
                "role": "Team Member",
                "id": "2410993231",
                "bio": "Computer Science Engineering with specialization in AI",
                "avatar": "/static/avatars/mayur.jpg"
            },
            {
                "name": "Mayank Singh", 
                "role": "Team Member",
                "id": "2410993230",
                "bio": "Computer Science Engineering with specialization in AI",
                "avatar": "/static/avatars/mayank.jpg"
            },
            {
                "name": "Madhav Sharma", 
                "role": "Team Member",
                "id": "2410993220",
                "bio": "Computer Science Engineering with specialization in AI",
                "avatar": "/static/avatars/madhav.jpg"
            },
        ],
        "stats": {
            "projects": 2,
            "clients": 4,
            "countries": 1
        }
    }
    return jsonify(team_data)


@app.route('/api/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.json
        print(f"New contact submission: {data}")
        return jsonify({"status": "success", "message": "We'll contact you soon!"})
    
    contact_info = {
        "email": "contact@district.events.com",
        "phone": "+91 123-4567-890",
        "address": "Chitkara University, Rajpura",
        "hours": "Mon-Fri: 9AM-6PM PST",
        "social": {
            "twitter": "@DistrictEvents",
            "linkedin": "company/district-events"
        }
    }
    return jsonify(contact_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)