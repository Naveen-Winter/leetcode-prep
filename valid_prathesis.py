
class IsValidSolution(object):
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
                elif len(track_closing) > 0 and track_closing[len(track_closing) - 1] == pranth:
                    track_closing.pop()
                else:
                    # this is a faulty string "{", "{@WEQDS}}" etc
                    return False
            if len(track_closing) == 0:
                return True
        return False