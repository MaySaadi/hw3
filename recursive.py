#questsion1
def find_subsets(lst):
    if not lst:
        return [[]]
    
    smaller_subsets = find_subsets(lst[1:])
    
    element = lst[0]
    new_subsets = []
    for subset in smaller_subsets:
        new_subsets.append(subset + [element])    
    return smaller_subsets + new_subsets


#question2
def find_nth(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return find_nth(n - 1) + find_nth(n - 2)

