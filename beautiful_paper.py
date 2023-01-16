N = int(input())
 
for i in range(N):
    first_rec = input().split()
    second_rec = input().split()
    minimum1 = min(int(first_rec[0]),int(first_rec[1]))
    minimum2 = min(int(second_rec[0]),int(second_rec[1]))
    
 
    
    max1 = max(int(first_rec[0]),int(first_rec[1]))
    max2 = max(int(second_rec[0]),int(second_rec[1]))
    
    if max1 != max2:
        print("No")
    elif int(minimum1) + int(minimum2) == int(max1):
        print("Yes")
    else:
        print("No")
