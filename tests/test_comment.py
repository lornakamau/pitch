import unittest
from app.models import Pitch, User, Comment
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment_content = 'content', author_id = 1, pitch_id =1 )
        self.new_pitch = Pitch(title = "title", pitch_content= "description", upvotes = 1, downvotes = 1, category_id =1, pitcher_id = 1)
        self.new_user = User(username = "lorna", email ="lorna@gmail.com", bio = "I am cool", profile_pic_path = "image_url", password = 'lorna')

        db.session.add(self.new_pitch)
        db.session.add(self.new_user)
        db.session.add(self.new_comment)
        db.session.commit()
        

    def tearDown(self):
        Comment.query.delete()
        Pitch.query.delete()
        User.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content, 'content')
        self.assertEquals(self.new_commrent.author_id,1 )
        self.assertEquals(self.new_comment.pitch_id,1)

    def test_get_comments(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(1)
        self.assertEqual(len(get_comments) == 1)