from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import FileField, StringField
# from flask_uploads import configure_uploads, UploadSet, ALL
from datetime import timedelta


# app.config['SECRET_KEY'] = 'Key'
# app.config['UPLOADED_FILES_DEST'] = 'uploads/files'
app = Flask(__name__)
# files = UploadSet('files', ALL)
# configure_uploads(app, files)

class PDFForm(FlaskForm):
    pdf  = FileField('pdf')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# ----------------------------------------------------------------  

@app.route('/login')
def login():
    return render_template('login-page.html')

@app.route('/resume-content')
def resumeContent():
    return render_template('resume-content.html')

@app.route('/icons')
def icons():
    return render_template('nucleo-icons.html')

@app.route('/profile')
def profile():
    return render_template('profile-page.html')

@app.route('/landing')
def landing():
    return render_template('landing-page.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_files():
#     form = PDFForm()
#     filename = 'No file submitted...'
#     if form.validate_on_submit():
#         session.permanent = True
#         filename = files.save(form.pdf.data)
#         session['filename'] = filename
#         return redirect(url_for('reader'))
#     else:
#         return render_template('upload.html', form=form)



# @app.route('/reader', methods=['GET', 'POST'])
# def reader():
#     if 'filename' in session:
#         filename = session['filename']
#         session['list'] = conv.readFile('uploads/files/' + filename)
#     else:
#         filename = 'No file selected...'

#     if 'list' in session:
#         list = session['list']
#     else:
#         list = ['Need', 'to', 'upload', 'a', 'file!']

#     return render_template('reader.html', list=list, filename=filename)


if __name__ == "__main__":
    app.run(debug=True)