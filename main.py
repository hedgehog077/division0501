
class Solution(object):

    def Divide(self, divided, divisor):
        #validation
        status = self.Validation(divisor)
        if status == False:
            return status

        answer = 0
        dividedAbs, divisorAbs = abs(divided), abs(divisor)
        for i in range(32, -1, -1):
            if dividedAbs >= (divisorAbs << i):
                dividedAbs -= (divisorAbs << i)
                answer += (1 << i)

        if (divided > 0 and divisor < 0) or (divided < 0 and divisor > 0):
            answer = answer*-1

        return min(2 ** 31 - 1, max(-2 ** 31, answer))


    def Validation(self, divisor):
        status = True
        if divisor == 0:
            status = False

        return status

if __name__ == '__main__':
    f3 = Solution()
    print(Solution.Divide(f3,-7,3))

