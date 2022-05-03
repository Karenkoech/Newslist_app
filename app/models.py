class News:

    '''
    News class to define News objects
    '''
    def __init__(self, title, content, author, date):
        self.title = title
        self.content = content
        self.author = author
        self.date = date

class Review:

    all reviews = []

    def __init__(self, title, content, author, date,review):
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
            
            response = []
    
            for review in cls.all_reviews:
                if review.id == id:
                    response.append(review)
    
            return response



