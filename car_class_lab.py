class Car(object):

  #Initialization method
  def __init__(self, name='General', model='GM', vehicle_type=None):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = 0

    #Check vehicle's number of doors
    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4

  #check if vehicle is saloon
  def is_saloon(self):
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False
  #Check driving state and speed
  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

    return self
