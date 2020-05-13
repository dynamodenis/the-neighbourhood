from . import  main
from flask import render_template

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts)

@main.route('/<uname>/blog',methods = ['GET','POST'])
@login_required
def blog(uname):
    user = User.query.filter_by(username = uname).first()
    form = PostForm()

    if not user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('auth.login'))
   
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
                
        posts = Post(user_id=users.id, title=title, post=post)
        db.session.add(posts)
        db.session.commit()

        flash('your Blog has been added successfuly!', 'success')
        return redirect(url_for('main.index',uname=users.username))

    return render_template('post.html', uname=user.username ,form =form)


# add this 
@main.route('/post/<int:post_id>',methods = ['POST'])
@login_required
def delete(post_id):
    posts = Post.query.filter_by(id=post_id).first()

    if posts.user != current_user:
        abort(403)
    
    db.session.delete(posts)
    db.session.commit()

    flash('your post has been deleted!', 'success')
    
    return redirect(url_for('main.index',post_id=posts.id))