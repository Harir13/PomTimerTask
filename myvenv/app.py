from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    mermaid_code = ""
    steps=""
    if request.method == 'POST':
        steps = request.form.get('steps')
        mermaid_code = generate_mermaid_code(steps)
    return render_template('index.html', tasks=tasks, mermaid_code=mermaid_code,steps=steps)

@app.route('/add_task', methods=['POST'])
def generate_mermaid_code(steps):
    steps_list = [step.strip() for step in steps.split('\n') if step.strip()]
    mermaid_code = "graph LR\n"
    for i, step in enumerate(steps_list):
        mermaid_code += f"    step{i}[{step}]\n"
        if i < len(steps_list) - 1:
            mermaid_code += f"    step{i} --> step{i+1}\n"
    return mermaid_code

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
