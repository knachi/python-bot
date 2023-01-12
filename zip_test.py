city = ["Mumbai ", "Delhi", "Bangalore"]
state = ["Maharashtra", "Delhi", "Karnataka"]
population = ["12,442,373", "11,007,835", "8,425,970"]

for c, s, p in zip(city, state, population):
    print('Name of the city: ', c)
    print('State of the city: ', s)
    print('Population of the city: ', p)
