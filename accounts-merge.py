class unionFind:
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}

    def find(self,x):
        if self.rep[x] == x:
            return x
        val = self.find(self.rep[x])
        self.rep[x] = val
        return val

    def union(self,x,y):
        rep_x = self.find(x)
        rep_y = self.find(y)

        self.rep[rep_y] = rep_x       

    def connected(self,x,y):
        x = self.find(x)
        y = self.find(y)
        
        return x == y
    
    def represent(self,x):
        self.rep[x] = x

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        un = unionFind(len(accounts))

        arr = dict()
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in arr:
                    un.union(arr[email], i)
                    continue
                
                arr[email] = i
    
        ans = dict()
        for email in arr:
            acc = un.find(arr[email])
            
            if acc in ans:
                ans[acc].append(email)
            else:
                ans[acc] = [email]
             
        res = []   
        for p in ans:
            res.append([accounts[p][0]] + sorted(ans[p]))
            
        return res
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for account in accounts:
        #     for word in account:
        #         un.represent(word)
        # for account in accounts:
        #     if account[0] not in visited:
        #         un.union(account[0],account[1])
        #         visited.add(account[0])
        #     for i in range(1,len(account)-1):
        #         un.union(account[i],account[i+1])
    
        # dic = defaultdict(list)
        # emails = set()
        # for key,val in un.rep.items():
        #     dic[val].append(key)