#METHODS OF SETS

#UNION

cricket:set = {'bat','ball','wickets'}
badminton:set = {'rocket','cock','net'}
print(cricket.union(badminton))

#INTERSECTION

cricket:set = {'bat','ball','wickets'}
badminton:set = {'ball','cock','net'}
print(cricket.intersection(badminton))

#INTERSECTION UPDATE

cricket:set = {'bat','ball','wickets'}
badminton:set = {'ball','cock','net'}
print(cricket.intersection_update(badminton))
print(cricket)
print(badminton)

#ISDISJOINT
cricket:set = {'bat','ball','wickets'}
badminton:set = {'rocket','cock','net'}
print(cricket.isdisjoint(badminton))

#DIFFERENCE

a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.difference(b))

#SYMMETRIC DIFFERENCE
a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.symmetric_difference(b))

#SYMMETRIC DIFFERENCE UPDATE

a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#IS SUBSET

a:set = {'a','b','c'}
b:set = {'b','c','d'}
print(a.issubset(b))

#IS SUPERSET

a:set = {'a','b','c'}
b:set = {'b','c'}
print(a.issuperset(b))

