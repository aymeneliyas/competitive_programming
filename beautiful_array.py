N = int(input())
arr = list(map(int,input().split()))
neg_list = []
pos_list = []
zero_list = []
 
for i in range(N):
    if arr[i] < 0:
        neg_list.append(arr[i])       
    if arr[i] > 0:
        pos_list.append(arr[i])
    if arr[i] == 0:
        zero_list.append(arr[i])
 
 
if len(neg_list) %2 == 0:
    n = neg_list.pop()
    zero_list.append(n)
if len(pos_list) == 0:
    n = neg_list.pop()
    m = neg_list.pop()
    pos_list.append(n)
    pos_list.append(m)
pos_list.insert(0,len(pos_list))
neg_list.insert(0,len(neg_list))
zero_list.insert(0,len(zero_list))
 
for i in range(len(neg_list)):
    print(neg_list[i],end = " ")
print('')
for i in range(len(pos_list)):
    print(pos_list[i],end = " ")
print('')
for i in range(len(zero_list)):
    print(zero_list[i],end = " ")
print('')

