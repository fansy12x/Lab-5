my_list = [1, 2, 5, 4, 3, 2, 5, 1, 2, 3, 9]
summa = sum(my_list[1::2])
for i in range (len (my_list[::2])):
    my_list[i*2] = summa
print (my_list)