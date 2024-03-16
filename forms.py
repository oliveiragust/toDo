from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    task = StringField('Tarefa', validators=[DataRequired()])
    task_description = StringField('Descrição')
    task_status = BooleanField('Task Completion', default=False)
    submit = SubmitField('Submit')
    atualizar = SubmitField('Complete')


class TaskComplete(FlaskForm):
    task_status = BooleanField('Task Completion', default=False)



