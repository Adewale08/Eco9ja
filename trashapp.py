'''
from flask import Flask, render_template_string, request, redirect, url_for
app = Flask(__name__)

# Simulated in-memory database for the hackathon demo
db = {
    "user_points": 0,
    "transactions": []
}



@app.route('/')
def index():
    # It MUST be render_template (no "_string" at the end!)
    # It MUST NOT be just return 'index.html'
    return render_template_string('index.html', db=db)

@app.route('/log_waste', methods=['POST'])
def log_waste():
    # Get data from the collector form
    material = request.form.get('material')
    weight = float(request.form.get('weight', 0))
    
    # Logic to calculate points
    multiplier = 50 if material == "Plastic" else 20
    points_earned = int(weight * multiplier)
    
    # Update the database
    db["user_points"] += points_earned
    db["transactions"].insert(0, {
        "action": f"Logged {weight}kg of {material}", 
        "points": points_earned
    })
    
    # Refresh the page
    return redirect(url_for('index'))

@app.route('/redeem', methods=['POST'])
def redeem():
    # Logic to simulate an API payout if the user has enough points
    if db["user_points"] >= 500:
        db["user_points"] -= 500
        # In a production app, you would fire your fintech/airtime API here
        db["transactions"].insert(0, {
            "action": "Redeemed ₦500 Airtime", 
            "points": -500
        })
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Adding host='0.0.0.0' tells Flask to broadcast to your local Wi-Fi network
    app.run(host='0.0.0.0', debug=True, port=5000)
    '''