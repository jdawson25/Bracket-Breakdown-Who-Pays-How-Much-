from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html', current_page='index')

@app.route('/micro/')
def micro():
    
    
    return render_template('micro.html', current_page='micro', )

@app.route('/about')
def about():
    return render_template('about.html', current_page='about')

app.run(debug=True)
