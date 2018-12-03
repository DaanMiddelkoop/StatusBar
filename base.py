class Base:
    def output(self):
        return '{"name":"' + self.name() + \
             '", "full_text": "' + self.full_text() + \
             '", "color": "' + self.color() + \
             '", "min_width": "' + self.min_width() + \
             '", "background": "' + self.background() + '"}'

    def name(self):
        return ""

    def full_text(self):
        return ""

    def color(self):
        return "#FFFFFF"

    def min_width(self):
        return ""

    def background(self):
        return "#000000"