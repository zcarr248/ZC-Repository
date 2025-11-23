class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3


 def __init__(self):
    """Initialize the TV with default settings."""
   self.__status = False
   self.__muted = False
   self.__volume = Television.MIN_VOLUME
   self.__channel = Television.MIN_CHANNEL

def power(self)-> None:
  """Turn TV on/off."""
  self.__status = not self.__status


def mute(self) -> None
  """Toggle mute only when TV is on."""
  if self.__status:
    self.__muted = not self.__muted

def channel_up(self):
  """Increase channel when TV is on, wrap is needed."""
  if self.__status:
      if self.__channel == Televison.MIN_CHANNEL:
          self.__channel = Television.MAX_CHANNEL
      else:
      self.__channel -= 1

def channel_down(self) -> None:
    """ Decrease channel when TV is on (wrap around)."""
    if self.__status:
        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1
    
      
    

def volume_up(self):
  """Increase volume when TV is on. Unmute if muted."""
  if self.__status:
    if self.__muted:
        self.__muted = False
    if self.__volume < Television.MAX_VOLUME:
      self.__volume += 1
      
def volume_down(self): -> None:
  """Decrease volume when TV is on. Unmute if muted."""

  if self.__status:
    if self.__muted:
        self.__muted = False
    if self.__volume > Television.MIN_VOLUME:
      self.__volume -= 1


def __str__(self):
  """Return details of TV for testing."""
  volume_display = 0 if self.__muted else self.__volume
  return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume__display}"
