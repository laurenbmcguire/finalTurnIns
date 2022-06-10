from .import bp as app
from flask import render_template, request, url_for, flash, redirect
from flask_login import current_user, login_required
from app import db, mail
from flask_mail import Message
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import Post
import boto3
from flask import current_app
import time, smtplib

@app.route('/')
@login_required
def home():
    # print(current_user.followed_posts)
    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template('home.html', **context)

# profile
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    s3 = boto3.client(
        's3', 
        aws_access_key_id=current_app.config.get('AWS_ACCESS_KEY_ID'), 
        aws_secret_access_key=current_app.config.get('AWS_SECRET_ACCESS_KEY')
    )

    
    if request.method == 'POST':
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        u.bio = request.form.get('bio')

        if len(request.files) > 0:
            s3.upload_fileobj(
                request.files.get('profile-image'),
                'codingtempledelete',
                request.files.get('profile-image').filename,
                ExtraArgs={
                    'ACL': 'public-read',
                    'ContentType': request.files.get('profile-image').content_type
                }
            )
            u.image = f"{current_app.config.get('AWS_BUCKET_LOCATION')}{request.files.get('profile-image').filename}"

        db.session.commit()
        flash('Profile updated successfully', 'info')
        return redirect(url_for('main.profile'))

    context = {
        'posts': Post.query.filter_by(user_id=current_user.id).order_by(Post.date_created.desc()).all()
    }
    return render_template('profile.html', **context)

# contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form_data = {
            'email': request.form.get('email'),
            'inquiry': request.form.get('inquiry'),
            'message': request.form.get('message')
        }
        # user = current_app.config.get('MAIL_USERNAME')
        # password = current_app.config.get('MAIL_PASSWORD')
        # mailserver=smtplib.SMTP("smtp.gmail.com", 465)
        # mailserver.ehlo()
        # mailserver.starttls()
        # mailserver.login(user,password)
        # message = "It works"
        # message = "Name:{}\nEmail: {}\nAddress: {}\nSize: {}\nNote: {}\nOrder: {}".format(name, email, address, size, note, order)
        # mailserver.sendmail(user,"noreply@zaraconsulting.org",message)

        # print(form_data)
        msg = Message(
            'This is a Test Subject Line',
            sender="derekhawkins.tech@gmail.com",
            reply_to=[form_data.get('email')],
            recipients=['derekhawkins.tech@gmail.com', 'derekh@codingtemple.com'],
            # body='This works'
            html=render_template('email/contact-results.html', **form_data)
            )
        # print('Are you working??')
        mail.send(msg)
        flash('Thank you for your message. We will get back to you within 48 hours.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')