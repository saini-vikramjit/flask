from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

# App secret key
app.config['SECRET_KEY'] = '7b7183641e298f8210806e522b8b0abb'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@studentblog.com' and form.password.data == 'admin':
            flash(f'You are logged in successfull.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessfull. Please check your credentials.', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)