
class Player():

    count = 0
    def __init__(self, first_name, last_name, speed):
        self.first_name = first_name
        self.last_name = last_name
        self.speed = speed
        self.nickname = None
        Player.count += 1
        self.id = Player.count
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First name must be of type string!')
        if value is None or len(str(value).strip()) == 0:
            raise ValueError('First name cannot be empty')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First name must be of type string!')
        if value is None or len(str(value).strip()) == 0:
            raise ValueError('Last name cannot be empty')
        self._last_name = value

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if not isinstance(value, int):
            raise TypeError('Speed must be an integer number!')
        if value < 0:
            raise ValueError('Speed cannot be a negative number!')
        self._speed = value

    def set_nickname(self):
        self.nickname = self.first_name[0].capitalize() + '.' + \
        self.last_name[0].capitalize() + self.last_name[1:]