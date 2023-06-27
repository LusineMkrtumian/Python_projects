d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

print(d)
for v in d.values():
    print(v)

print(d)
for v in d.keys():
    print(v)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)