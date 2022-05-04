import unittest
from app.models import news,Sources,Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','https://abcnews.go.com/abcnews/image/9371043','2018-09-23T21:00:00Z','Breaking News, Latest News and Videos')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_init(self):
        self.assertEqual(self.new_article.id,'abc-news')
        self.assertEqual(self.new_article.name,'ABC News')
        self.assertEqual(self.new_article.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEqual(self.new_article.url,'https://abcnews.go.com')
        self.assertEqual(self.new_article.urlToImage,'https://abcnews.go.com/abcnews/image/9371043')
        self.assertEqual(self.new_article.publishedAt,'2018-09-23T21:00:00Z')
        self.assertEqual(self.new_article.content,'Breaking News, Latest News and Videos')

    def test_save_article(self):
        self.new_article.save_article()
        self.assertEqual(len(Articles.all_articles),1)

    def test_get_all_articles(self):
        self.assertEqual(Articles.get_all_articles(),Articles.all_articles)

    def test_delete_article(self):
        self.new_article.save_article()
        self.new_article.delete_article()
        self.assertEqual(len(),0)


