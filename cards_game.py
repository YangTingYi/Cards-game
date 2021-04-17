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
   def __init__(self, flower=[], number=[]):
      self.__callback = False
      self.__flower = []
      self.__number = []
      self.table = [[],[]]
   
   def get_callback(self):
      return self.__callback

   def set_card(self, flower:list, number:list):
      self.__callback = False
      self.__flower = flower
      self.__number = number

      if len(self.__flower) > 0 or len(self.__number) > 0 or len(self.__flower) == len(self.__number):
         self.__callback = True
      
      return [self.__flower, self.__number]

   def owncards(self):
      self.__callback = False
      
      if len(self.__flower) > 0 or len(self.__number) > 0 or len(self.__flower) == len(self.__number):
         self.__callback = True

      return [self.__flower, self.__number]

   def counter(self):
      self.__count = [0] * 13

      if self.__callback:
         for x in range(len(self.__number)):
            if self.__flower[x] < 1 or self.__flower[x] > 4 or self.__number[x] < 1 or self.__number[x] > 13:
               self.__callback = False
               self.__count = [0] * 13
               break
            else:
               self.__count[self.__number[x]-1] += 1
         
         return self.__count

   def pairer(self):
      if self.__callback:
         for x in range(len(self.__count)):
            if self.__count[x] >= 2:
               pass

class Compare:
   pass


mike = Cards()

if mike.get_callback():
   print(mike.counter())
   print(mike.owncards())
else:
   print(">>>No Cards.>>>")

mike.set_card(
   [  Flower.SPADE,
      Flower.DIAMOND,
      Flower.CLUBS,
      Flower.CLUBS,
      Flower.HEART,
      Flower.SPADE   ],
   [11, 3, 8, 5, 6, 8]
)

if mike.get_callback():
   print(mike.counter())
   print(mike.owncards())
else:
   print(">>>No Cards.>>>")

mike.table = [
   [  Flower.SPADE,
      Flower.DIAMOND ],
   [9, 9]
]
print(mike.table)

'''學習class Private變數怎麼取值,還有其特性
# print(mike.__count) #Private變數,不能直接讀
print(mike.counter()) #可以透過return讀Private變數

mike.__count = [1, 2] #可以在class外新增變數和給值
print(mike.__count)

print(mike.counter()) #但注意mike.__count != mike.counter()
'''