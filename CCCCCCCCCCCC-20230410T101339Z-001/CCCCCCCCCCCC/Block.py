'''
for IF ... ELSE...
Grammar: S->if E then M1S1 else M2S2
E.true = M1->S1 //S1
E.false = M2->S2 //S2
'''
class Block:
    def __init__(self, code, true, false):
        self.code = code
        if true is not None and false is not None:
            self.true = true
            self.false = false
        self.next = None


