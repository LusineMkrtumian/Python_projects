set()   # пустое множество
print(set([1, 2, 6]))   # множество, полученное из списка
print(set([1, 2, 6, 6, 1, 2]))   # исключили повторы

A = set([1, 2, 4, 6])
B = set([2, 3, 6, 8])
print(A.intersection(B))  # {2, 6}
print(A.union(B))  # {1, 2, 3, 4, 6, 8}
print(A.difference(B))  # {1, 4}
print(B.difference(A))  # {8, 3}
print(A.symmetric_difference(B))  # {1, 3, 4, 8} т.к. 2 и 6 входят в оба множества
print(A.isdisjoint(B))  # joint - пересекающиеся, disjoint - непересекающиеся; false
print(A.issubset(B))  # false - А не является подмножеством B
