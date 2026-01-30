from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/amenities')
def amenities():
    return render_template('amenities.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle booking form submission
        # Add your booking logic here
        pass
    return render_template('booking.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        # Add your login logic here
        pass
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        # Add your contact logic here
        pass
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)