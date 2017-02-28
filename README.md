# python-turing
Biblioteca para criação de Máquinas de Turing Determinísticas.

## Índice
1. <a href="#1">O que é Máquina de Turing</a>
2. <a href="#2">Sobre este programa</a>
3. <a href="#3">Como executar</a>
4. <a href="#4">Como criar uma Máquina de Turing</a>

## <a name="1">1. O que é Máquina de Turing</a>

A m&aacute;quina de
	Turing &eacute; um dispositivo te&oacute;rico conhecido como m&aacute;quina
	mundial, que foi concebido pelo matem&aacute;tico brit&acirc;nico
	Alan Turing , muitos anos antes de existirem os modernos
	computadores digitais (o artigo de refer&ecirc;ncia foi publicado em
	1936). Num sentido preciso, &eacute; um modelo abstrato de um
	computador, que se restringe apenas aos aspectos l&oacute;gicos do
	seu funcionamento (mem&oacute;ria, estados e transi&ccedil;&otilde;es)
	e n&atilde;o &agrave; sua implementa&ccedil;&atilde;o f&iacute;sica.
	Numa m&aacute;quina de Turing pode-se modelar qualquer computador
	digital.
	
## <a name="2">2. Sobre este programa</a>
Este
	programa foi desenvolvido de modo a simular o processamento de uma
	M&aacute;quina de Turing Determin&iacute;stica. Foi desenvolvido na
	linguagem Python 3 e requere a entrada manual de dados sobre a
	simula&ccedil;&atilde;o e um interpretador para a linguagem.

## <a name="3">3. Como executar</a>
### 3.1 Via Eclipse
Para executar o programa via eclipse, deve-se ir ao menu File (Arquivo),
		e em seguida Import (Importar). Uma janela ser&aacute; aberta
		exibindo as op&ccedil;&otilde;es de importa&ccedil;&atilde;o.
		Expanda o diret&oacute;rio General e selecione Existing Projects
		into Workspace. Clique em Next, e ent&atilde;o, escolha a pasta ra&iacute;z do programa em Select root directory. Assim feito, ser&aacute; carregado o projeto, necessitando apenas ao usu&aacute;rio selecionar um dos exemplos de MT j&aacute; inclusos ou desenvolver um novo, e clicar em Run.

### 3.2 Via Terminal/Prompt de Comando
Para executar o programa via terminal ou prompt de comando, navegue at&eacute; a pasta ra&iacute;z do programa, e ent&atilde;o digite:
<p align="center"><code>python3 XXXX.py</code></p>
Sendo XXXX o nome do arquivo em que est&atilde;o os dados sobre a MT.
*(Nota: Em ambos os casos, &eacute; necess&aacute;rio que o usu&aacute;rio tenha instalado o interpretador para Python3)*

<a name="4">3. Como criar uma M&aacute;quina de Turing</a>
Segue um exemplo de MT j&aacute; criada:
```python
	from turing import *
	
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
```
Onde est&atilde;o sendo declarados: <font color="#FF0000">os alfabetos</font>; <font color="#993333">as transi&ccedil;&otilde;es</font>; <font color="#6633CC">os estados</font>; e <font color="#000099">a m&aacute;quina</font>. E s&atilde;o executados <font color="#00CCCC">alguns testes</font> nessa m&aacute;quina.
</div>
