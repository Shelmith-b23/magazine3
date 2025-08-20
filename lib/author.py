# lib/author.py
class Author:
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        # relative import to avoid circular import
        from .article import Article  
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        from .article import Article  
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({mag.category for mag in self.magazines()})
