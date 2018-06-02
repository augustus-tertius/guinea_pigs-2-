
class Message:

    def __init__(self, author_name, date, text):
        self.author_name = author_name
        self.date = date
        self.text = text

    def __str__(self):
        s = "author name: " + self.author_name + \
            "date " + self.date + " text " + self.text
        return s

    __repr__ = __str__
