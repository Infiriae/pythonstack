import random
def randInt(min=0, max=100):
    if (min > max or max < 0):
        return 'Impossible request has been made'
    else:
        num = random.random() * (max-min) + min
        return round(num)

print(randInt())
print(randInt(max=-50))
print(randInt(min=50))
print(randInt(50,500))