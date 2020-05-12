from app.models import Comment,Post
from app import db
import unittest

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_post=Post(post='love posts')
        self.new_comment=Comment(comment='love posts coment',post=self.new_post)
    
    def tearDown(self):
        self.new_comment.query.delete()
        self.new_post.query.delete()

    def test_saved_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        get=Comment.get_comment(self.new_post.id)
        self.assertTrue(len(get)==1)
