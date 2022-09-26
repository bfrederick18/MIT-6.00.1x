"""
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
  

Click to expand Hint: How to think about this problem
Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.


Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened = []
    for element in aList:
        if type(element) == list:
            flattened += flatten(element)
        else:
            flattened.append(element)
    return flattened

print('Answer:', flatten([]))
print('Answer:', flatten([1, 2, 3, 4]))
print('Answer:', flatten([1, [2], 3, 4]))
print('Answer:', flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))  # [1,'a','cat',2,3,'dog',4,5]