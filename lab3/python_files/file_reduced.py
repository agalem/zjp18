class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    raise NotImplementedError

class Robin(Bird):
  name = 'Robin'

  def get_speed(self):
    return 14

class GoldFinch(Bird):
  name = 'Gold Finch'

  def get_speed(self):
    return 12

class Ostrich(Bird):
  name = 'Ostrich'
  flightless = True

  def get_speed(self):
    return 15

class Pterodactyl(Bird):
  name = 'Pterodactyl'
  extinct = True

  def get_speed(self):
    return -1