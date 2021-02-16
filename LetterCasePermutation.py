class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []

        def perm(s, rem):
            if len(rem) == 0:
                res.append(s)
                return

            if rem[0].isalpha():
                if rem[0].islower():
                    perm(s + rem[0].upper(), rem[1:])

                elif rem[0].isupper():
                    perm(s + rem[0].lower(), rem[1:])

            perm(s + rem[0], rem[1:])

        perm('', S)
        return res

