import unittest

#capital T
#bound in general class are specfic testing methods
class TestStringMethods(unittest.TestCase):
# don't instantiate a class because testing builtins 
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with 'swallows' error--/with/ used a lot w/ databases 
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
