from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'q2ep$25Swyct(H@kF9P2hrdKoXBT(Iy1MAZHFWWAM(M)9VNXiO6GY5$i443CM!SI'

posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post contet',
		'date_posted': 'April 20th, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post contet',
		'date_posted': 'April 21st, 2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		successMessage = 'Account created for %s!' %(form.username.data)
		flash(successMessage, 'success')
		return redirect(url_for('home'))

	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and password.', 'danger')

	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)