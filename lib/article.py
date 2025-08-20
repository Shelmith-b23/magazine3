# lib/article.py
class Article:
    all = []

    def __init__(self, author, magazine, title):
        # use relative imports to avoid ModuleNotFoundError
        from .author import Author
        from .magazine import Magazine

        # validate author
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")

        # validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")

        # validate title
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title
