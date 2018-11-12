class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,author,description,url,urlToImage,category,language,country):
        self.author = author
        # self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.category = category
        self.language = language
        self.country = country