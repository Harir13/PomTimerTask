from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        tasks.append({'task': task, 'start_time': datetime.now()})
    return redirect(url_for('index'))

@app.route('/get_timer')
def get_timer():
    if tasks:
        elapsed_time = datetime.now() - tasks[-1]['start_time']
        remaining_time = max(timedelta(minutes=25) - elapsed_time, timedelta(0))
        total_seconds = int(remaining_time.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        remaining_time_str = f"{minutes:02d}:{seconds:02d}"
        return jsonify({'remaining_time': remaining_time_str})
    else:
        return jsonify({'remaining_time': '25:00'})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
