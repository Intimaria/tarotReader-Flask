import random

class Spread():
  tarot = { 1:"The Magician", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit", 10:"Wheel of Fortune", 11:"Justice", 12:"The Hanged Man", 13:"Death", 14:"Temperance", 15:"The Devil", 16: "The Tower", 17:"The Star", 18:"The Moon", 19:"The Sun", 20:"Judgement", 21:"The World", 22:"The Fool"}
  question = ['']
  spread = {}
  def __init__(self):
    return
  def get_spread(self):
    self.spread["past"] = self.tarot.pop(random.randint(1, 22))
    self.spread["present"] = self.tarot.pop(random.randint(1, 22))
    self.spread["future"] = self.tarot.pop(random.randint(1, 22))
    return self.spread

my_reading = Spread().get_spread()
for key, item in my_reading.items():
  print("Your "+key+" is the "+item+" card.")
		
