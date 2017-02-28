from turing import *
'''
Maquina de Turing 1
L = (a^n)(b^n)
'''

DIR = True
ESQ = False

alfabeto = ['a','b']
alfabeto_aux = ['A','B']

trans_q0 = [["#","#",DIR,"q0"],['a','A',DIR,"q1"],['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
trans_q1 = [['b','B',ESQ,"q2"],['a','a',DIR,"q1"],['B','B',DIR,"q1"]]
trans_q2 = [['A','A',DIR,"q0"],['a','a',ESQ,"q2"],['B','B',ESQ,"q2"]]
trans_q3 = [['B','B',DIR,"q3"],[' ',' ',DIR,"q4"]]
trans_q4 = []

q0 = estado("q0",trans_q0)
q1 = estado("q1",trans_q1)
q2 = estado("q2",trans_q2)
q3 = estado("q3",trans_q3)
q4 = estado("q4",trans_q4,is_final=True)

turing = turing(alfabeto,[q0,q1,q2,q3,q4],"q0",alfabeto_aux,'#',' ')
turing.aceita("ab")
turing.aceita("aabb")
turing.aceita("aaab")
turing.aceita("aaaabbbb")