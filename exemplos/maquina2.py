from turing import *
'''
Maquina de Turing 1
L = Complemento de entrada binaria
'''

DIR = True
ESQ = False

alfabeto = ['0','1']
alfabeto_aux = ['0','1']

trans_q0 = [['#','#',DIR,"q0"],['0','1',DIR,"q0"],['1','0',DIR,"q0"],[' ',' ',ESQ,"q1"]]
trans_q1 = [['1','1',ESQ,"q1"],['0','0',ESQ,"q1"],['#','#',DIR,"qf"]]
trans_qf = [['0','0',DIR,"qf"],['1','1',DIR,"qf"],[' ',' ',DIR,"qf"],['#','#',DIR,"qf"]]

q0 = estado("q0",trans_q0)
q1 = estado("q1",trans_q1)
qf = estado("qf",trans_qf,is_final=True)

turing = turing(alfabeto,[q0,q1,qf],"q0",alfabeto_aux,'#',' ')
a = turing.aceita("10",passos=False)
b = turing.aceita("1010",passos=False)
c = turing.aceita("1001",passos=False)
d = turing.aceita("00001",passos=False)

print(a)
print(b)
print(c)
print(d)