from flask import Flask, render_template # Import the Flask class from the flask module

app = Flask(__name__) # Create an instance of the Flask class

@app.route('/') # Create a route decorator
def home():
    return render_template('home.html') # Return the home.html template

# Add more routes here as the app expands

if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode
