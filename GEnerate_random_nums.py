
import random

value = random.random()

value1 = random.uniform(1,10) # not used much

value2 = random.randint(1,6)



greetings = ['Hello' ,'Hi', 'Hey', 'Howdy']

value3 = random.choice(greetings)

#print(value3, 'tani')



colors = ['pink','green','yellow','red','blue']

value4 = random.choices(colors, k=10)

#print(value4)



colors = ['pink','green','yellow']

value5 = random.choices(colors, weights=[18,1,2], k=10)

#print(value5)



deck = list(range(1,53))

random.shuffle(deck)

#print(deck)

hand = random.sample(deck, k=5)

print(hand)
