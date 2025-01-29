from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        # ... [keep all your existing data here] ...
        profile_image="static/img/profile.jpg"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')