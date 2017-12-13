if 1 < 2:
    print('ran if')
elif 1 == 1:
    print('ran elif')
else:
    print('no!')

seq = [1,2,3,4,5,6]

for jelly in seq:
    print(jelly)

d = {
'sam':1,
'frank':2,
'dan':3
}

for k in d:
    print(k)
    print(d[k])

my_pairs = [(1,2),(3,4),(5,6)]
for x,y in my_pairs:
    print(x)
    print(y)
    print(x + y)


#while loops
i = 1

while i <= 5:
    print("i is: {}".format(i))
    i = i + 1


#range function

x = list(range(0,20, 2))
print x


for item in range(0,11):
    print(item)


out = []
for num in x:
    out.append(num**2)

print(out)

out = [x**2 for x in range(0,20,2)]
print(out)
