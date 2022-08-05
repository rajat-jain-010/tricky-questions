# to find that if there exist any two numbers in a list whose summation leads to another number given by user
def adder():
    a = input("enter all numbers seprated by a space :: ").split()
    b = int(input("enter the number which u want to find using summation of two elements from list ::"))
    l = []
    for i in a:
            l1 = []
            for i1 in range(1,a.count(i)):
                l1.append(i)
        
            l2 = list((set(a) - {i}))
            l2 = l2 + l1
            for j in l2:
                if  (int(i)+int(j)) == b:
                    if (j,i)  in l:
                        break
                    print("{} + {} = {}".format(i,j,int(i)+int(j)))
                    l.append((i,j))

adder()

    










  