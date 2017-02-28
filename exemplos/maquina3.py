from turing import *
'''
Maquina de Turing 1
L = (a^n)(b^n)(c^n)
'''

DIR = True
ESQ = False

alfabeto = ['a','b','c']
alfabeto_aux = ['x','y','z']

trans_q0 = [['#','#',DIR,"q0"],['a','x',DIR,"q1"],['y','y',DIR,"q4"],[' ',' ',DIR,"q5"]]
trans_q1 = [['a','a',DIR,"q1"],['y','y',DIR,"q1"],['b','y',DIR,"q2"]]
trans_q2 = [['z','z',DIR,"q2"],['b','b',DIR,"q2"],['c','z',ESQ,"q3"]]
trans_q3 = [['z','z',ESQ,"q3"],['a','a',ESQ,"q3"],['b','b',ESQ,"q3"],['y','y',ESQ,"q3"],['x','x',DIR,"q0"]]
trans_q4 = [['z','z',DIR,"q4"],['y','y',DIR,"q4"],[' ',' ',DIR,"q5"]]
trans_q5 = []

q0 = estado("q0",trans_q0)
q1 = estado("q1",trans_q1)
q2 = estado("q2",trans_q2)
q3 = estado("q3",trans_q3)
q4 = estado("q4",trans_q4)
q5 = estado("q5",trans_q5,is_final=True)

turing = turing(alfabeto,[q0,q1,q2,q3,q4,q5],"q0",alfabeto_aux,'#',' ')
turing.aceita("")
turing.aceita("aabbcc")
turing.aceita("aaabbbccc")
turing.aceita("abbc")