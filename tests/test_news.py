import unittest
from app.models import news,Sources,Articles

News=news.News

class newsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','https://abcnews.go.com/abcnews/image/9371043','2018-09-23T21:00:00Z','Breaking News, Latest News and Videos',[])

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    def test_init(self):
        self.assertEqual(self.new_news.id,'abc-news')
        self.assertEqual(self.new_news.name,'ABC News')
        self.assertEqual(self.new_news.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEqual(self.new_news.url,'https://abcnews.go.com')
        self.assertEqual(self.new_news.urlToImage,'https://abcnews.go.com/abcnews/image/9371043')
        self.assertEqual(self.new_news.publishedAt,'2018-09-23T21:00:00Z')
        self.assertEqual(self.new_news.content,'Breaking News, Latest News and Videos')
        self.assertEqual(self.new_news.articles,[])

    def test_save_news(self):
        self.new_news.save_news()
        self.assertEqual(len(News.all_news),1)
    
    

