import unittest
from OOP_Player.player import Player

"""
TEST CASES:
Is this class instansiable? Can we create objects from this class?
first_name, last_name -> type:str
speed -> type: int
- EXAMPLE NICKNAME: 
    - amr elmasry --? A.Elmasry
- CHECK ID COUNT 
- DATA PERSISTANCE: CHECK UNIQUE VALUES, first_name+last_name
"""

class TestPlayer(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     # This gets executed only once before the rest of the instance methods
    #     cls._player = Player('Amir', 'Tavakoli', 100)

    def setUp(self):
        # This will be executed before every single test method!
        self._player = Player('Amir' , 'Tavakoli', 100)

    def test_firstNameNotEmpty(self):
        with self.assertRaises(ValueError):
            Player('', 'Tavakoli', 50)

    def test_firstNameNotStr(self):
        with self.assertRaises(TypeError):
            Player(10, 'Tavakoli', 50)
    
    def test_lastNameNotEmpty(self):
        with self.assertRaises(ValueError):
            Player('Amir', '  ', 23)

    def test_lastNameNotStr(self):
        with self.assertRaises(TypeError):
            Player('Amir', 10.5, 50)

    def test_speedNotInt(self):
        with self.assertRaises(TypeError):
            Player('Amir', 'Tavakoli', 10.5)

    def test_speedNotNegative(self):
        with self.assertRaises(ValueError):
            Player('Amir', 'Tavakoli', -5)
        

    def test_canCreateInstance(self):
        # Sad testing path
        with self.assertRaises(TypeError):
            Player()
    
    def test_nickname(self):
        self._player.set_nickname()
        self.assertEqual(self._player.nickname, 'A.Tavakoli')

    # This is the third test that gets executed, alphabetical order,
    #.. p(playerIDNumber) is after n(nickname), but the problem is what
    #.. what if you have hundreds of tests? how can you keep track of 
    #.. alphabetical order? -> solution: pdb
    def test_playerIDNumber(self):  
        # breakpoint()    # python debugger (pdb tool) -> for lots of tests
        self.assertEqual(self._player.id, 7)
