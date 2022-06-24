class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        pranth_dict = {'(':')', '{':'}','[':']' }
        track_closing = []
        if len(s):
            for pranth in s:
                
                if pranth in pranth_dict:
                    track_closing.append(pranth_dict[pranth])
                if pranth not in pranth_dict:
                    print(track_closing[0])
                    if pranth == track_closing[0]:
                        track_closing.pop()
                    else:
                        return False
                print(track_closing)
            if len(track_closing) == 0:
                return True
        return False