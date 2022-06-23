
#Solution is accepted 


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = set(['(','{','['])
        closing = set([')',']','}'])
        pranth_dict = {'(':')', '{':'}','[':']' }
        track_closing = []
        print('here')
        if len(s):
            print('here')
            for pranth in s:
                print(pranth)
                print(track_closing)
                if pranth in pranth_dict:
                    track_closing.append(pranth_dict[pranth])
                else:
                    if track_closing[0] == pranth:
                        track_closing.pop()
            if len(track_closing) == 0:
                return True
        return False
            