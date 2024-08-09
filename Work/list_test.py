""" s = [ 1, 2, 3]
t = ['a', 'b']
print(s + t) """
""" 
def print_list(names):
    for name in names:
        print(name)

names = [ 'Elwood', 'Jake', 'Curtis' ]

print_list(names)

names[1] = 'Joliet Jake'
print("-"*80)

print_list(names)
print(len(names))
 """

symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']

for s in symlist:
    print('s =', s)

print('AIG' in symlist)
print('AA' in symlist)
print('CAT' in symlist)

symlist.append('RHT')
print(symlist)

symlist.insert(1, 'AA')
print(symlist)

symlist.remove('MSFT')

print(symlist)

symlist.append('YHOO')
print(symlist)

print(symlist.count('YHOO'))

symlist.remove('YHOO')
print(symlist)

symlist.sort()
print(symlist)

symlist.sort(reverse=True)
print(symlist)

a = ','.join(symlist)
print(a)

b = ':'.join(symlist)
print(b)

c = ''.join(symlist)
print(c)

nums = [101, 102, 103]

items = ['spam', symlist, nums]
print(items)

print(items[0])
print(items[0][0])

print(items[1])
print(items[1][1])
print(items[1][1][2])

print(items[2])
print(items[2][1])
