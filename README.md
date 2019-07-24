# graph_study

apparantly list.append() and the += modify the list in place, changes persist across recursive calls when used in a class

either use list1 = list + something or make a copy and then append every time

The official essay on graphs says:

'''The 'path' argument is not modified: the assignment "path = path + [start]" creates a new list. If we had written "path.append(start)" instead, we would have modified the variable 'path' in the caller, with disastrous results. (Using tuples, we could have been sure this would not happen, at the cost of having to write "path = path + (start,)" since "(start)" isn't a singleton tuple -- it is just a parenthesized expression.)'''
