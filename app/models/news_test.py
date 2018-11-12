import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News('Emily Dreyfuss','breaking news','was hurtful','https://www.wired.com/story/donald-trump-dating-app-exposed-data/','https://media.wired.com/photos/5bca5bfab1e96429a704b9d9/191:100/pass/TrumpCouple-1009882898.jpg','2018-10-20T13:00:00Z','As has become an unwelcome tradition, as Friday wound down and the weekend was so close we could nearly taste it, breaking news hit. The biggest Friday night bombshell came in the form of an indictment of a Russian national engaged in a massive conspiracy to … [+5433 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()