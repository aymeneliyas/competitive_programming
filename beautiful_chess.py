from collections import Counter
N = int(input())
for i in range(N):
    
    start = False
    answer = False
    for j in range(9):
        
        row = input()
        
        count = Counter(row)

        if start == True and count["#"] == 1 and answer == False:
            for index in range(8):
                if row[index] == "#":
                    print(j,index+1)
            answer = True
        if count["#"] == 2:
            start = True
