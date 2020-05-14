from . import  main
from flask import render_template,redirect,request,url_for,flash,abort
from .. import db
from ..models import Post,User,Comment
from .forms import Commentform,UpdateProfile,PostForm


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts)

@main.route('/account' ,methods = ['GET','POST'])
@login_required
def account():
    form=UpdateProfile()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email =form.email.data
        current_user.bio =form.bio.data
        current_user.contact =form.contact.data
        current_user.address =form.address.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
        form.contact.data = current_user.contact
        form.address.data = current_user.address
    return render_template('profile/profile.html', title='Update Account', form=form)


