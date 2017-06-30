"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import smtplib
from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import ContactForm

###
# Routing for your application.
###
app.secret_key = "s3cr3t"


def send_mail(name, email, subject, messg):
    fromaddr = 'dane.miller.info3180@gmail.com'
    fromname = name
    toaddr  = 'dane.miller.info3180@gmail.com'
    msg = messg
    eemail = [toaddr, email]
    subject = subject
    message = "To: %s\r\nCC: %s\r\nSubject: %s\r\n%s\r\n\n%s\r\n%s" %(toaddr, email, subject, msg, fromname, email)
        
    messagetosend = message
    
    
    # Credentials (if needed)
    username = 'dane.miller.info3180@gmail.com'
    password = 'ubsjbwmxmqsxufyl'
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, eemail, messagetosend)
    server.quit()

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/contact/', methods=["GET", "POST"])
def contact():
    # if form.validate():
    #     print "hooha"
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        send_mail(request.form['name'], request.form['email'],request.form['subject'], request.form['msg'])
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
