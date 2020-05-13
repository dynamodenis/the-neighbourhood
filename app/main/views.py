from . import  main
from flask import render_template,redirect,request
from .. import db
from ..models import Post


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts)