###########
#### All the pure python code from the class_02 slides. 
###########

word = "Soliloquy"
if len(word) > 8:
    print(word + " is a long word.")
else: 
    print(word + " is NOT a long word.")

############

if len(word) > 8:
print(word + " is a long word.")

############

X = [True, True, False, False]
Y = [True, False, True, False]
print([i and j for i, j in zip(X, Y)]) # The "and" (&) truth table

############

print([i or j for i, j in zip(X, Y)]) # The "or" (|) truth table

############

print (not True)

############

print(not False)

############

a, b, c, d = 5.1, 12.2, -4, 12.2 # Assign four numbers at once. The right-hand side is a 4-tuple
print(a == b)
print(a != c)
print(b > d)
print(b >= d)
print(c < a)
print(d <= c)

############

word = "Reasonable"
if (len(word) > 8) and (word[0] == "Y"):
    print("A long word beginning with Y")
elif  (len(word) > 8) and (word[0] != "Y"):
    print("A long word not beginning with Y")
else:
    print("Not a long word")

############

word = 'supercalifragilisticexpialidocious'
'long word' if len(word) > 10 else 'short word'

############

word = 'super'
'long word' if len(word) > 10 else 'short word'

############

data = [7, 13, 21, 3, 8, 12] # Data contained in a list
transformed_data = []        # An empty container to accept the transformed data
for i in range(len(data)):   # i will take on integer values, 0, 1, ... 5
    transformed_data.append(data[i] ** 0.5) # This is the square root transformation
print(transformed_data) # Take a look at what we have created.

############

data = [7, 13, 21, 3, 8, 12] # Data contained in a list
transformed_data = []
for i, value in enumerate(data): # note that two components are being returned, i and value.
    print ("Looking at " + str(value) + " in position " + str(i))
    transformed_data.append(value ** 0.5 )
print(transformed_data)

############

import numpy as np # We will use numpy to help shuffle the deck

# Build a card deck (not worrying about the suit)
card_deck = [2, 3, 4, 5, 6, 7 ,8 , 9, 10, 'J','Q','K', 'A'] * 4

# A variable for the number of iterations in the simulation.
num_its = 10000
# A counter to track the number of times the condition (the first two cards are both aces) is true.
counter = 0

# The for loop
for i in range(num_its):
    new_deck = np.random.permutation(card_deck) # shuffle the deck. 
    if ((new_deck[0] == "A") and (new_deck[1] == "A")):
        counter = counter + 1 

print("The estimated probability of two aces is ", counter/num_its)


############



############

for i in range(1,5): # The numbers 1 through 4 (outer loop)
    for j in range(1,5): # The inner loop.
        total = i + j 
        if total > 4: # break out of the inner loop if the total is greater than 4
            break
        print ("Outer is {0}, inner is {1}, total is {2}".format(i,j,total)) # More on string formats later.

############

for i in range(9):
  if (i % 2) == 0: # Skip the even numbers.
    continue
  print(i)

############

x = 0
while x < 6:
    print('Keep going, i rolled a {}!'.format(x)) # Note the .format method for the string.
    x = np.random.randint(1,7) # This line of code rolls a six-sided die.

############

results = [] # start with an empty list to store the results of the experiment.
num_its = 10000 # The number of simulation iterations
for i in range(num_its):
    new_deck = np.random.permutation(card_deck) # shuffle the deck. 
    counter = 1 # a counter for how many cards until the ace is first seen.
    while new_deck[counter - 1] != 'A':
        counter = counter + 1
    results.append(counter)
print("The expected waiting time to the first ace is ", sum(results)/num_its, " cards")


############

result_1 = [i**2 for i in range(10)] # The first 10 square numbers.
print(result_1)
result_2 = [i**2 for i in range(10) if (i % 2 == 0)] # Squares of even numbers.
print(result_2)

############

words = ["This", "is", "a", "list", "of", "key", "words"]
print([word[::-1] for word in words if len(word) > 3])

############

