from collections import OrderedDict
from enum import Enum


def RepeatedNumbers(a):
    # Write your code here
    tracker = OrderedDict()
    res = list()
    for i in a:
        if i in tracker:
            tracker[i] += 1
        else:
            tracker[i] = 1
    for i in tracker:
        if tracker[i] > 1:
            res.append(i)
    return res


"""
tracker = defaultdict(int) # Hashtable == time
hold = set() # set 
res = list() # list 


for i in a:
    tracker[i] += 1
    if tracker[i] > 1:
        hold.add(i) # O(N)
for i in a:
    if i in hold and i not in res:
        res.append(i) # O (N^2)
return res
"""


class Operations(Enum):
    ADD = 0
    SUBTRACT = 1
    SET = 2
    ROUND_TO_CLOSEST_MULTIPLE_OF_FIVE = 3
    REPEAT_LAST_OPERATION = 4


class Calculator:
    def __init__(self):
        self.total = 0
        self.prev = None

    def performOperation(self, op, value):
        # Write your code here
        if op == Operations.REPEAT_LAST_OPERATION:
            if self.prev is None:
                self.total = 0
            self.performOperation(self.prev[0], self.prev[1])
            return
        self.prev = tuple((op, value))
        if op == Operations.ADD:
            self.total = self.total + value
        if op == Operations.SUBTRACT:
            self.total = self.total - value
        if op == Operations.SET:
            self.total = value
        if op == Operations.ROUND_TO_CLOSEST_MULTIPLE_OF_FIVE:
            x = self.total % 5
            print(self.total, x)
            if x >= 3:
                self.total = int(self.total / 5) * 5 + 5
            else:
                self.total = int(self.total / 5) * 5
            self.total = int(self.total)
            print(self.total)


#
# Complete the 'SmallestDictionaryOrderedArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def SmallestDictionaryOrderedArray(a, b):
    print((a, b))
    # Write your code here
    for i, j in zip(a, b):
        if i != j:
            return a if i < j else b
    return a if len(a) < len(b) else b
