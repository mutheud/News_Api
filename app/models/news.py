class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,author,description,url,urlToImage,category,language,country):
        # self.id = id
        # self.name = name
        self.author =author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.category = category
        self.language = language
        self.country = country