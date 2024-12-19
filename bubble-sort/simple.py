my_list=[6,2,4,5,1]
new_list=[]

# for i=0;i<len(my_list) - 1;i++:
i=0
while i < len(my_list) - 1:
    j=0
    while j < len(my_list) - 1 - i:
        if(my_list[j] > my_list[j + 1]):
            tmp=my_list[j]
            my_list[j]=my_list[j + 1]
            my_list[j + 1]=tmp
        j +=1
    i +=1


print(my_list)
