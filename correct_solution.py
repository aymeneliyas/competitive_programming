import heapq
n = str(input())

res = [int(x) for x in n]

heapq.heapify(res)
flag = False
ans = []
while res:
    a = heapq.heappop(res)
    c = 0
    while res and a == 0:
        a = heapq.heappop(res)
        c += 1
    ans.append(a)

    while c:
        ans.append(0)
        c -= 1
    
answer = ""
for i in ans:
    answer += str(i)
 
bob = str(input())

if answer == bob:
    print("OK")
else:
    print("WRONG_ANSWER")
