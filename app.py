from flask import Flask, render_template, redirect, request
from models import db, Task
from flask_sqlalchemy import SQLAlchemy
from forms import TaskForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/to_do'

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm(request.form)
    date = datetime.now()
    data = date.strftime('%d/%m/%Y as %H:%M')
    if form.validate_on_submit():
        task = Task(task=form.task.data, task_description=form.task_description.data, task_status=False)
        db.session.add(task)
        db.session.commit()
        return redirect('/')

    tasks = Task.query.all()

    return render_template('index.html', form=form, tasks=tasks, data=data)


@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    task = Task.query.get_or_404(task_id)
    task.task_status = not task.task_status
    db.session.commit()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    tasks = Task.query.all()
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    return redirect('/')




if __name__ == '__main__':
    db.create_all()
    app.run()
