from estado import *

'''
Created on 12/09/2013

@author: Ronaldo
'''

class turing():
    def __init__(self,alfabeto,estados,est_inicial,alfabeto_aux,simb_inicio,simb_branco):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estados.append(estado('?'))
        self.estado_inicial = est_inicial
        self.alfabeto_aux = alfabeto_aux
        self.simb_inicio = simb_inicio
        self.simb_branco = simb_branco
        self.fita = []
        self.cabeca = 0
        self.estado_atual = self.estado_inicial
        
    def aceita(self,cadeia,passos=True):
        self.cabeca = 0
        self.fita = self.simb_inicio + cadeia + self.simb_branco
        self.estado_atual = self.estado_inicial
        
        if passos:
            print("---- Cadeia "+cadeia+" ----")
        
        while 0 <= self.cabeca < len(self.fita):
            saida = self.programa()
            if passos:
                print(saida)
            
        if passos:
            if self.get_estado(self.estado_atual).is_final:
                print("Cadeia '"+cadeia+"' aceita!")
            else:
                print("Cadeia '"+cadeia+"' rejeitada!")
                
            print("-----------------"+("-"*len(cadeia)))
        
        return self.fita[1:-1]
    
    def programa(self):
        saida = "programa("+self.estado_atual+","+self.fita[self.cabeca]+") = "
        transicao = self.get_estado(self.estado_atual).get_transicao(self.fita[self.cabeca])
        
        # Ve se simbolo esta em alfabeto
        if not self.checar_simbolo(self.alfabeto,self.fita[self.cabeca]):
            print(self.fita[self.cabeca]+" nao pertence ao alfabeto!")
            self.cabeca = len(self.fita)
        #
        
        if transicao is not None:
            # Se houver algo para escrever, escreve.
            if transicao[1] is not None:
                
                if not self.checar_simbolo(self.alfabeto_aux,transicao[1]):
                    print(self.fita[self.cabeca]+" nao pertence ao alfabeto!")
                    self.cabeca = len(self.fita)
                
                aux = list(self.fita)
                aux.pop(self.cabeca)
                aux.insert(self.cabeca,transicao[1])
                self.fita = ''.join(aux)
            #
            
            # Ve para qual lado mover a cabeca.
            if transicao[2]:
                self.cabeca += 1
            else:
                self.cabeca -= 1
            #
            
            # Procura e faz a transicao
            if transicao[3] is not None:
                self.estado_atual = transicao[3]
            else:
                self.estado_atual = '?'
            #
        else:
            self.cabeca = len(self.fita)
            self.estado_atual = '?'
            
        saida += self.estado_atual
        
        return saida
        
    def get_estado(self,nome):
        for estado in self.estados:
            if estado.get_nome() is nome:
                return estado
                break
                
        return None
        
    def checar_simbolo(self,alfabeto,simbolo):
        if simbolo is self.simb_inicio or self.simb_branco:
            return True
        
        for i in alfabeto:
            if i is simbolo:
                return True
            
        return False