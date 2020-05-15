from . import  main
from flask import render_template,redirect,request,url_for,flash,abort
from .. import db
from ..models import Post,User,Comment
from .forms import Commentform,UpdateProfile,PostForm
from flask_login import login_required,current_user
from ..utils import save_picture,post_image

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts,pages='index')

@main.route('/test')
def test():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=8)
    return render_template('test.html', posts=posts,pages='index')

#USER PROFILE 
@main.route('/user/<string:user>' ,methods=['GET','POST'])
@login_required
def profile(user):
    image=url_for('static',filename='profile/'+current_user.profile_pic_path)
    user=User.query.filter_by(username=user).first_or_404()
    page=request.args.get('page',1,type=int)
    post=Post.query.filter_by(user=user)\
        .order_by(Post.posted_date.desc())\
        .paginate(page=page,per_page=10)
    return render_template('user_profile.html',page='profile',image=image,user=user,posts=post,pages='profile')

#USER PROFILE 
@main.route('/<string:user>/posts' ,methods=['GET','POST'])
@login_required
def post_profile(user):
    image=url_for('static',filename='profile/'+current_user.profile_pic_path)
    user=User.query.filter_by(username=user).first_or_404()
    page=request.args.get('page',1,type=int)
    post=Post.query.filter_by(user=user)\
        .order_by(Post.posted_date.desc())\
        .paginate(page=page,per_page=10)
    return render_template('user_post.html',image=image,user=user,posts=post)



#UPDATE USER PROFILE
@main.route('/<string:uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    form=UpdateProfile()
    user=User.query.filter_by(username=uname).first_or_404()

    if user.username !=current_user.username:
        abort(403)


    if form.validate_on_submit():
        if form.picture.data:
            profile_pic=save_picture(form.picture.data)
            user.profile_pic_path=profile_pic
        user.bio=form.bio.data
        user.username=form.username.data
        user.email=form.email.data
        user.contact=form.contact.data
        user.address=form.address.data
        db.session.commit()
        return redirect(url_for('main.profile',user=user.username))
        flash('Update Successful!')

    elif request.method=='GET':
        form.bio.data=user.bio
        form.username.data=user.username
        form.email.data=user.email
        form.contact.data=user.contact
        form.address.data=user.address
    
    return render_template('updates/update_profile.html' ,title='Update | Profile',form=form,legend='Update Profile')


#UPLOADING POST FUCTION
@main.route('/<string:uname>/blog',methods = ['GET','POST'])
@login_required
def post(uname):
    user = User.query.filter_by(username = uname).first()
    form = PostForm()

    if not user.is_authenticated:
        flash('Please Login', 'danger')
        return redirect(url_for('auth.login'))
   
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        if form.picture.data:
            picture=post_image(form.picture.data)
            posts = Post(title=title, post=post,user_id=user.id,picture=picture)
            db.session.add(posts)
            db.session.commit()

        elif form.picture.data is None:        
            posts = Post(title=title, post=post,user_id=user.id)
            db.session.add(posts)
            db.session.commit()

        flash('Posted Successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('post.html',form =form,pages='post',legend='Upload Post')


#COMMENT ON A POST
@main.route('/<int:post_id>/comment', methods=['GET','POST'])
@login_required
def comment(post_id): 
    post=Post.query.filter_by(id=post_id).first()
    comment_query=Comment.query.filter_by(post_id=post.id).all()
    form_comment=Commentform()
    # if not user.is_authenticated:
    #     flash('please login', 'danger')
    #     return redirect(url_for('main.login')) 
    if form_comment.validate_on_submit():
        comment=Comment(comment=form_comment.comment.data,post_id=post.id,user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.comment',post_id=post.id))
    return render_template('comments.html',form=form_comment,post=post,comments=comment_query,title='Comments')


#DELETE A POST
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


#UPDATE A POST
@main.route('/update/post/<int:post_id>', methods=['GET','POST'])
@login_required
def update_post(post_id):
    update=PostForm()
    post=Post.query.filter_by(id=post_id).first_or_404()
    if post.user !=current_user:
        abort(403)

    if update.validate_on_submit():
        post.title=update.title.data
        post.post=update.post.data
        db.session.commit()
        return redirect(url_for('main.profile',user=post.user.username))
        flash('Post updated!','success')

    elif request.method=='GET':
        update.title.data=post.title
        update.post.data=post.post
        
    return render_template('updates/update_post.html',update=update,legend='Update post',title='Update post')

#PAGINATION INT THE BLOGGER PROFILE


@main.route('/profile/user/<string:username>')
def posted(username):
    user=User.query.filter_by(username=username).first_or_404()
    image=url_for('static',filename='profile/'+ user.profile_pic_path)
    page=request.args.get('page',1,type=int)
    posts=Post.query.filter_by(user=user)\
            .order_by(Post.posted_date.desc())\
            .paginate(page=page,per_page=10)

    return render_template('blogger_profile.html',posts=posts,title=user.username,user=user,image=image)

@main.route('/about')
def about():
    return render_template('about.html',pages='about')

@main.route('/delete/comment/<int:comment_id>', methods=['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment=Comment.query.filter_by(id=comment_id).first_or_404()
    post= Post.query.filter_by(id=comment.post.id).first()

    db.session.delete(comment)
    db.session.commit()
    flash('Blog deleted!')
    return redirect(url_for('main.comment',post_id=post.id))