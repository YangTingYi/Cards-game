from operator import attrgetter

class Flower:
   SPADE = 4
   HEART = 3
   DIAMOND = 2
   CLUBS = 1

class callback:
   OK = 0
   NO_VALUE = 1
   OVER_VAL = 2

class Cards:
   def __init__(self, flower, number):
      self.flower = flower
      self.number = number

   def __repr__(self):
      return repr((self.flower, self.number))

class Process:
   def __init__(self, cards:Cards):
      self.__callback = False
      self.__cards = sorted(cards, key=attrgetter('number', 'flower'))
      self.table = [Cards(0,0), Cards(0,0)]
      self.is_bigger_pair = False
   
   def __repr__(self):
      self.__callback = False
      if len(self.__cards) > 0:
         self.__callback = True
      return repr((self.__cards))

   def get_callback(self):
      return self.__callback

   def counter(self):
      self.__count = [0] * 13

      if self.__callback:
         for x in range(len(self.__cards)):
            # For now, only here should be check. If many, should write to '__repr__'.
            if self.__cards[x].flower < 1 or self.__cards[x].flower > 4 or self.__cards[x].number < 1 or self.__cards[x].number > 13:
               self.__callback = False
               self.__count = [0] * 13
               break
            else:
               count_id = self.__cards[x].number - 1
               self.__count[count_id] += 1
               
               if self.__count[count_id] >= 2 and self.table[1].flower > 0 and self.table[1].number > 0 and self.table[1].number <= 13:
                  if self.__cards[count_id].number > self.table[1].number:
                     self.is_bigger_pair = True
                  elif self.__cards[count_id].number == self.table[1].number and self.__cards[count_id].flower > self.table[1].flower:
                     self.is_bigger_pair = True
                  else:
                     self.is_bigger_pair = False

         
      return self.__count

   # def pairer(self):
   #    if self.__callback:
   #       for x in range(len(self.__count)):
   #          if self.__count[x] >= 2:
   #             pass

# class Compare:
   # pass


cards = [
   Cards(Flower.SPADE, 12),
   Cards(Flower.DIAMOND, 6),
   Cards(Flower.HEART, 12),
   Cards(Flower.CLUBS, 8)
]

process = Process(cards)

process.table = [
   Cards(Flower.DIAMOND, 7),
   Cards(Flower.HEART, 7)
]

count = process.counter() 