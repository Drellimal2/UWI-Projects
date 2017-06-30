"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, jsonify, Response
from .forms import ProfileForm
import time
from app.models import Profile
from werkzeug import secure_filename

###
# Routing for your application.
###
app.secret_key = "I LIKE THIS COURSE"
@app.route('/profile', methods=['GET','POST'])
def profile():
    
    form = ProfileForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        print request.headers
        upfile = request.files['image']
        if upfile:
            upfilename = form.firstname.data + '_' + secure_filename(upfile.filename)
            filepath = "uploads/" + upfilename
            filepath2 = os.path.join(os.getcwd() + '/app/static/' + filepath)
            upfile.save(filepath2)
        print "Yay"        
        profile = Profile(form.firstname.data, form.lastname.data, form.age.data, filepath, form.sex.data, getTime())
        db.session.add(profile)
        db.session.commit()
        return redirect('/profile/'+str(profile.id))
    return render_template('newprofile.html',form=form)

def getTime():
    now = time.strftime("%a, %d %b %Y")
    return now
    
@app.route('/profiles', methods=['GET','POST'])
def profiles():
    
    profiles = db.session.query(Profile)
    if request.method == 'POST':
        users = []
        for profile in profiles:
            users+=[{'userid':profile.id, 'username':profile.firstname +"_"+profile.lastname}]
        return jsonify(profiles=users)
    return render_template('profiles.html',profiles=profiles)
    
@app.route('/profile/<user_id>', methods=['GET','POST'])
def userprofile(user_id):
    print user_id
    profile = db.session.query(Profile).filter_by(id=user_id).first()

    json_header ='Content-Type: application/json'
    if json_header in request.headers or request.method == 'POST':
        return jsonify( userid=user_id, username=profile.firstname +"_"+profile.lastname,
                        image=profile.image, sex=profile.sex, age=profile.age, 
                        profile_add_on=profile.created_on, 
                        high_score=profile.highest_score,
                        tdollars=profile.tdollars)
    
    return render_template('profile.html', profile=profile)
    
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


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
