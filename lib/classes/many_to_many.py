class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, '_title'):
            print("title is already set")
            return
        if not isinstance(new_title, str):
            print("must be a string")
            return
        if not (5 <= len(new_title) <= 50):
            print("must be between 5 and 50 characters")
            return
        self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else: 
            print("invalid author")
        self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance (new_magazine, Magazine):
            self._magazine = new_magazine
        else: 
            print("invalid magazine")


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            print("name already exists")
            return
        if not isinstance(new_name, str) and len(new_name) > 0:
            print("name must be a string")
            return 
        self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            return Article(self, magazine, title)
        
    def topic_areas(self):
        if not self.magazines():
            return None
        else:
            return list(set(item.category for item in self.magazines()))
        

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print("must be a string")
            return 
        if not 2 <= len(new_name) <= 16:
            print("must be 2-16 characters")
            return
        self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            print("category must be a string")
            return
        if not len(new_category) > 0:
            print("string must be more than 0")
            return
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        else: 
            return [item.title for item in self.articles()]

    def contributing_authors(self):
        list = []
        for item in self.articles():
           if len(self.articles()) <= 2:
               return None
           else: 
               list.append(item.author)
        return list