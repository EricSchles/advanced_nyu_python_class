# sets get us uniqueness!
set([5,5,4,4,3,3,2,1])
# returns {1, 2, 3, 4, 5}
import random
[random.randint(0,100) for _ in range(50)]
# returns [71, 94, 53, 39, 47, 0, 28, 88, 99, 6, 29, 0, 40, 11, 30, 47, 48, 90, 53, 32, 32, 73, 67, 57, 4, 65, 10, 13, 5, 10, 88, 45, 15, 85, 19, 53, 14, 80, 16, 39, 41, 51, 17, 47, 82, 68, 54, 83, 98, 9]
set([random.randint(0,100) for _ in range(50)])
# returns {0, 2, 3, 8, 10, 11, 12, 14, 15, 20, 24, 26, 29, 32, 33, 35, 37, 38, 40, 42, 43, 44, 50, 53, 54, 58, 60, 63, 65, 67, 72, 73, 75, 76, 77, 78, 81, 82, 83, 85, 88, 91, 93, 96}
listing = [random.randint(0,100) for _ in range(50)]
len(listing)
# returns 50
len(set(listing))
# returns 40

# running a natural experiment to see how unique random
# numbers are when you increase your range every iteration
result = {random.randint(0,maximum) for maximum in range(10,1000)}
len(result)
# returns 483
result = {random.randint(0,maximum) for maximum in range(10,100)}
len(result)
# returns 56
result = {random.randint(0,maximum) for maximum in range(10,10000)}
len(result)
# returns 4969
result = {random.randint(0,maximum) for maximum in range(10,100000)}
len(result)
# returns 50113
