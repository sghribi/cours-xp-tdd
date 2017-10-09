import unittest

def return_true():
    return True

def return_false();
    return False

class Test(unittest.TestCase):
    def setUp(self):
        """Initialisation des tests."""
        pass

    def test_return_true(self):
        value = return_true()
        self.assertTrue(value)
 
if __name__ == '__main__':
    unittest.main()
 
