
"""
This is Code TO print pascal triangle in Python by using Dynamic Programming
"""
def generate(num):
    DP=[]
    """
    as there are i elements in ith row of triangle so we will add lst of i length
    """
    for i in range(num):
        lst=[0 for k in range(i+1)]
        DP.append(lst)
    
    for i in range(num):
        DP[i][0]=1 # as every first and last element of row is 1 
        DP[i][i]=1
        for j in range(1,i): 
            DP[i][j]=DP[i-1][j-1]+DP[i-1][j]  # any element  of row is sum of its previous row previous index element and same index element
    printtriangle(DP)                         # for example 5th row 2 element i.e 4 .4 prevoius row previous index  element is 1. 4 preivous row same index element is 1
                                              # so theri sum is  3+1=4 that is 5th row 2nd element
def printtriangle(DP):
    n=len(DP)
    k=n-1
    for lst in DP:
        for j in range(k):
            print(end=" ")
        k-=1
        for ele in lst:
            print(ele,end=" ")
        print()

# Driver Code
n = 5
generate(n)
#     1 
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1


