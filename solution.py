#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr, n, m):
        # code here
        li=[]
        for i in arr:
            k=i.count(1)
            li.append(k)
        if(max(li)==0):
            return -1
        else:
            return(li.index(max(li)))
