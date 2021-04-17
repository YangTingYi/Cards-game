class Cards:
   callback = False

   def __init__(self, flower=[], number=[]):
      self.flower = flower
      self.number = number
   
   def mycard(self):
      return [self.flower, self.number]

   def counter(self):
      #callback = False

      if len(self.flower) == 0 or len(self.number) == 0 or len(self.flower) != len(self.number):
         callback = False
      else:
         count = [0] * 13
         for x in range(len(self.number)):
            if self.flower[x] < 1 or self.flower[x] > 4 or self.number[x] < 1 or self.number[x] > 13:
               break
            else:
               count[self.number[x]] = count[self.number[x]] + 1
         
         return count


cards = Cards()
print(cards.mycard())

cards.flower = [4, 3, 1, 2, 2, 4]
cards.number = [10, 4, 6, 7, 9, 5]
print(cards.mycard())
print(cards.counter())

#print(cards.counter())
#if cards.callback == True:
   #print(cards.counter)
