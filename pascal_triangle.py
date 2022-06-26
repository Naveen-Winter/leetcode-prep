class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #pascal triangle 
        P_t = [[1]]
        
        if numRows == 1:
            return P_t
        for n in range(1,numRows):
            # every row in pascal triangle starts and ends with 1
            P_t.append([1])
            
            if n>1:
                for i in range(1,n):
                    P_t[n].append(P_t[n-1][i-1] + P_t[n-1][i])
            P_t[n].append(1)
        
        return P_t
                
