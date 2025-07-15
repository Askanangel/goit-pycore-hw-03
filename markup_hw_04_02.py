import random

def get_numbers_ticket(min_num, max_num, quantity):
   if min_num >=1 and max_num <= 1000 and quantity >= 1: 
         random_numbers = random.sample(range(min_num, max_num), quantity) 
         print(random_numbers)

get_numbers_ticket(1, 49, 6)
       
       