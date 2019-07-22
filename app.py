from flask import Flask, render_template, url_for

app = Flask(__name__)


# Static data
students = [
    {
        'name': "Jim Bin",
        'rollno': 941,
        'major': "Social",
        'isOnProbation': False
    },
    {
        'name': "Martin",
        'rollno': 923,
        'major': "Maths",
        'isOnProbation': True
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', students=students)

@app.route("/about")
def about():
    return render_template('about.html', title="About Us")

if __name__ == "__main__":
    app.run(debug=True)