class Solution:

    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        opener = []

        for i in s:

            if i == "{":
                opener.append(i)

            if i == "[":
                opener.append(i)

            if i == "(":
                opener.append(i)

            if i == "}":
                if not opener or opener[-1] != "{":
                    return False
                opener.pop()

            if i == "]":
                if not opener or opener[-1] != "[":
                    return False
                opener.pop()

            if i == ")":
                if not opener or opener[-1] != "(":
                    return False
                opener.pop()

        if opener:
            return False
        else:
            return True