import os
import secrets
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegisterationForm, LoginForm
from werkzeug.utils import secure_filename

app = Flask(__name__)

# App secret key
app.config['SECRET_KEY'] = '7b7183641e298f8210806e522b8b0abb'

UPLOAD_FOLDER = 'static/profile_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'profilePicture' not in request.files:
            flash('No file part.','danger')
            return redirect(url_for('upload'))
        
        file = request.files['profilePicture']
        if file.filename == '':
            flash('No file selected.','danger')
            return redirect(url_for('upload'))

        if not allowed_file(file.filename):
            flash('Invalid file type.','danger')
            return redirect(url_for('upload'))

        randomHex = secrets.token_hex(8)
        _, fExt = os.path.splitext(file.filename)
        picture = randomHex + fExt
        #filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], picture))
        flash(f'File uploaded successfully.','success')
        return redirect(url_for('home'))
            
    else:
        return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)