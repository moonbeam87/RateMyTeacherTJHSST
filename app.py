#!bin/python
#Code and Styling heavily based off - https://github.com/Neo-Hao/wtf-registration-form
from flask import Flask, request, render_template
from model import RegForm
from flask_bootstrap import Bootstrap
from write_to_table import write

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        department = form.name_first.data
        last_name = form.name_last.data
        rating = form.rating.data
        description = form.description.data
        return write(department, last_name, rating, description)
    return render_template('registration_custom.html', form=form)

if __name__ == '__main__':
    app.run()
