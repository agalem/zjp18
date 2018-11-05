class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
      if self.flightless:
        if self.name == 'Ostrich' and self.extinct == False : 
          return 15 
        elif self.name == 'Chicken' and self.extinct == False:
          return 7
        elif self.name == 'Flamingo'and self.extinct == False:
          return 8
        else:
          return -1 # bird name not implemented
      else:
        if self.name == 'Gold Finch' and self.extinct == False:
          return 12
        elif self.name == 'Bluejay' and self.extinct == False:
          return 10
        elif self.name == 'Robin' and self.extinct == False:
          return 14
        elif self.name == 'Hummingbird' and self.extinct == False:
          return 16
        else:
          return -1 # bird not implemented