import unittest

from person import Person


class TddInPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person()

    def test_person_return_error_message_if_name_is_empty(self):
        self.assertRaises(ValueError, self.person.name_is_empty, '')

    def test_person_name_too_short(self):
        self.assertRaises(ValueError, self.person.name_is_too_short, 'Ita')

    def test_person_name_is_not_string(self):
        self.assertRaises(ValueError, self.person.name_is_not_string,
                          ['Uchiha', 'Itachi'])

if __name__ == '__main__':
    unittest.main()
