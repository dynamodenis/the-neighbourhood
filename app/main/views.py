from . import  main
from flask import render_template,redirect,request,url_for,flash,abort
from .. import db
from ..models import Post,User,Comment
from .forms import Commentform,UpdateProfile,PostForm
from flask_login import login_required, current_user




@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts)



@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comment.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:post_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(post_id):
    post = Post.query.filter_by(id = post_id).first()
    form = Commentform()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment,user_id=current_user.id, post_id=post_id)


        new_comment.save_comment()


        return redirect(url_for('main.index'))
    title='New Comment'
    return render_template('new_comment.html',title=title,comment_form = form,post_id=post_id)


