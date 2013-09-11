class Person(object):

    def name_is_empty(self, name):
        if not name:
            raise ValueError('Name can\'t be empty!')

    def name_is_too_short(self, name):
        if len(name) < 4:
            raise ValueError('Name is too short!')

    def name_is_not_string(self, name):
        if not isinstance(name, basestring):
            raise ValueError('Invalid name!')
