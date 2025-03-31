from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Tomato Disease Classifier</h1><p>The app is currently under setup. Please check back soon.</p>"

if __name__ == '__main__':
    app.run(port=5001, debug=True)
