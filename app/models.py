class News:

    '''
    News class to define News objects
    '''
    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        
class Reviews:
    '''
    Reviews class to define Reviews objects
    '''

    def __init__(self,id,name,description,url,urlToImage,publishedAt,content,review):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.review = review
    
    def save_review(self):
        '''
        Function to save reviews
        '''
        Reviews.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        '''
        Function to clear reviews
        '''
        Reviews.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):
        
        response = []

        for review in cls.all_reviews:
            if review.id == id:
                response.append(review)
        return response



    
