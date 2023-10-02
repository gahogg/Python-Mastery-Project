from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_types/')
def data_types():
    return render_template('data_types.html')

@app.route('/data_structures/')
def data_structures():
    return render_template('data_structures.html')

@app.route('/conditionals/')
def conditionals():
    return render_template('conditionals.html')

@app.route('/loops/')
def loops():
    return render_template('loops.html')

@app.route('/functions/')
def functions():
    return render_template('functions.html')

@app.route('/classes/')
def classes():
    return render_template('classes.html')

@app.route('/advanced_topics/')
def advanced_topics():
    return render_template('advanced_topics.html')