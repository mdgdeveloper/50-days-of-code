# You want to implement a code that will search for a number in
# a range. You have a decision to make as to whether to store the
# number in a set or a list. Your decision will be based on time.
# You have to pick a data type that executes faster.
# You have a range and you can either store it in a set or a list
# depending on which one executes faster when you are searching
# for a number in the range. See below:
# a = range(10000000)
# x = set(a)
# y = list(a)
# Let’s say you are looking for a number 9999999 in the range
# above. Search for this number in the list and the set. Your
# challenge is to find which code executes faster. You will pick the
# one that executes quicker, lists, or sets. Run the two searches
# and time them.

import time

a = range(10000000)
setStore = set(a)
listStore = list(a)

ts1 = time.time()
matchesSet = [x for x in setStore if x == 99999]
ts2 = time.time()
setTime = ts2 - ts1
ts1 = time.time()
matchesList = [x for x in listStore if x == 99999]
ts2 = time.time()
listTime = ts2 - ts1
print("setTime:", setTime)
print("listTime", listTime)
