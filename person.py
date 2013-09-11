class Person(object):

    def name_is_empty(self, name):
        if not name:
            raise ValueError

    def name_is_too_short(self, name):
        if len(name) < 4:
            raise ValueError

    def name_is_not_string(self, name):
        if not isinstance(name, basestring):
            raise ValueError
