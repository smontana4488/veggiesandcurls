from flask import Flask, render_template

app = Flask(__name__,  template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/recipes')
def receipes():
    return render_template('recipes.html')

@app.route('/meal_planner')
def meal_planner():
    return render_template('meal_planner.html')

@app.route('/beauty')
def beauty():
    return render_template('beauty.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run()
