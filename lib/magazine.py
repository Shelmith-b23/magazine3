# lib/magazine.py
class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # ---------------- Name ----------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    # ---------------- Category ----------------
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    # ---------------- Relationships ----------------
    def articles(self):
        from article import Article   # lazy import
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    # ---------------- Aggregates ----------------
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if not self.articles():
            return None
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        from article import Article
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
