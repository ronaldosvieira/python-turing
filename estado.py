'''
Created on 12/09/2013

@author: Ronaldo
'''

class estado():
    def __init__(self,nome,transicoes=[],is_final=False):
        self.nome = nome
        self.transicoes = transicoes
        self.is_final = is_final
        
    def __str__(self):
        return self.nome
    
    def get_transicao(self,simbolo):
        for transicao in self.transicoes:
            if transicao[0] is simbolo:
                    return transicao
                
        return None
        
    def get_nome(self):
        return self.nome
            