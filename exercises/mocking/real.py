import micro

def other_important_func():
    return "Answer: {}".format(micro.plus(1,3))


class UsingMicroInProd(object):
    
    def important (self, operand1, operand2):
        '''
        product owner said should only work for positive numbers reutnred from micro.plus
        '''
        answer = micro.plus(operand1, operand2)
        if answer < 0:
            raise ValueError     
        else:
            return "Answer: {}".format(micro.plus(operand1, operand2))
        
