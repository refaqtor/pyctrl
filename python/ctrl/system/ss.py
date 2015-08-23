import numpy

from .. import system

class DTSS:
    """DTSS(A, B, C, D, state)

    Model is of the form:

      x(k+1) = A x(k) + B u(k)
        y(k) = C x(k) + D u(k)

    """
    
    def __init__(self,
                 A = numpy.array([[]]),
                 B = numpy.array([[0]]),
                 C = numpy.array([[]]),
                 D = numpy.array([[1]]),
                 state = None):

        #print('A = {} ({})'.format(A, A.shape))
        #print('B = {} ({})'.format(B, B.shape))
        #print('C = {} ({})'.format(C, C.shape))
        #print('D = {} ({})'.format(D, D.shape))

        # check dimensions
        assert A.shape == (1,0) or A.shape[0] == A.shape[1]
        assert A.shape[0] == B.shape[0]
        assert C.shape[0] == D.shape[0]
        assert A.shape[1] == C.shape[1]
        assert B.shape[1] == D.shape[1]
        
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        n = A.shape[0]
        if state is None:
            self.state = numpy.zeros((n,1), dtype=float)
        elif state.shape == (n, 1):
            self.state = state.astype(float)
        else:
            raise system.SysException('Order of state must match order of denominator')

        #print('num = {}'.format(self.num))
        #print('den = {}'.format(self.den))
        #print('state = {}'.format(self.state))

    def set_output(self, yk):
        raise Exception('Not implemented yet')
    
    def update(self, uk):
        # yk = C xk + D uk
        # xk+1 = A xk + B uk
        if self.state.size > 0:
            #print('> x = {}'.format(self.state))
            yk = self.C.dot(self.state) + self.D.dot(uk)
            #print('> yk = {}'.format(yk))
            #print('> A.x = {}'.format(self.A.dot(self.state)))
            #print('> B.u = {}'.format(self.B.dot(uk)))
            self.state = self.A.dot(self.state) + self.B.dot(uk)
            #print('< x = {}'.format(self.state))
        else:
            yk = self.D.dot(uk)
            
        return yk
