from ._anvil_designer import Form1Template
from anvil import *
import random
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



def button_1_click(self, **event_args):
  self.image_1.source = None
  coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg']
  coin = random.choice(coins)
  time.sleep(1)
  self.image_1.source = URLMedia(coin)

