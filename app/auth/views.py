from . import main
from ..models import User, Post

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts)