n=int(input())
arr = list(map(str,input().split()))
 
m = int(input())
 
ans = {}
query = []
left = 0
for i in range(m):
    word = str(input())
    query.append(word)
squery = sorted(query)
for i in range(m):
    if left >= len(arr):
        ans[squery[i]] = left
    while left < len(arr):
        if squery[i] <= arr[left]:
            ans[squery[i]] = left
            break
        if left == len(arr)-1 and squery[i] >= arr[left]:
            ans[squery[i]] = left + 1
        
        left += 1
 
output = []
for i in query:
    output.append(ans[i])
for i in output:
    print(i)