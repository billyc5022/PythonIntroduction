animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)

animals += ["monkey", 'dog']    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)

animals = animals[0:5]
animals.append("dinosaur")
print(animals)