import micro  # import sqlite


def another_important_func():
    return "Answer: {}".format(micro.plus(1, 3))


class UsingMicroInProd(object):

    def important(self, operand1, operand2):
        '''
        Hey. Product owner said, this should only work for
        positive numbers returned from micro.plus
        '''
        try:
            answer = micro.plus(operand1, operand2)
        except ValueError:  # print nice message if micro.plus flips a table
            return "Plus method failed for undefined reason"

        if answer < 0:
            raise ValueError()  # this method Flip table if the answer is negative
        else:
            return "Answer: {}".format(answer)
