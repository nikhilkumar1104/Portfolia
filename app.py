from flask import Flask, render_template

app = Flask(__name__)
# this is the main  route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

#this route for the project page
@app.route('/projects/gait')
def project_gait():
    return render_template('projects/gait.html')

@app.route('/projects/petrolpump')
def project_petrolpump():
    return render_template('projects/petrolpump.html')

@app.route('/projects/crm')
def project_crm():
    return render_template('projects/crm.html')

@app.route('/projects/stock')
def project_stock():
    return render_template('projects/stock.html')           



  
if __name__ == '__main__':
    app.run(debug=True)
