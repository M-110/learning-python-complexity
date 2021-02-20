o=['buffalo']
list(map(lambda x: o.insert(0,x+o[-1][1:]), ['B' if int(i) else 'b' for i in bin(69)[:1:-1]]))
print(' '.join(o))