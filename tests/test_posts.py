from app.models import Post,User
from app import db
class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.user_brian = User(username = 'brian',password = '123', email = 'brian@demo.com')
        self.new_post = Post(title='Programming',content="programmin is fun!",author = self.user_brian )

    def test_check_instance_variables(self):
        self.assertEquals(self.new_id,1)
        self.assertEquals(self.new_title,'Programming')
        self.assertEquals(self.new_date_posted,"2019-02-13")
        self.assertEquals(self.new_content,'Programming is fun')
        self.assertEquals(self.new_user.id,'2')        

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)
