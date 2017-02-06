list1 =  [[0 for col in range(5)] for row in range(5)]
for i in range(5):
    print list1[i]

print '==============='
#list1[1][1:4] = 1
list1[1][1] = 1
for i in range(5):
    print list1[i]