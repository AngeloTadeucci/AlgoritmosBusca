# -*- coding: utf-8 -*-

class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        caminho = caminho[::-1]
        return caminho
    
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

class busca(object):

    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            #if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    def profundidade(self, inicio, fim):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da pilha
            atual = l1.deletaUltimo()
            if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])-1,-1,-1):

                novo = grafo[ind][i]
                #print("\tFilho de atual: ",novo)
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                    
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    def profundidade_limitada(self, inicio, fim, limite):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da pilha
            atual = l1.deletaUltimo()
            if atual is None: break

            if atual.valor2 < limite:
                ind = nos.index(atual.valor1)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])-1,-1,-1):
    
                    novo = grafo[ind][i]
                    #print("\tFilho de atual: ",novo)
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                        
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            #print("Árvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"

    def aprofundamento_iterativo(self, inicio, fim):
        
        for limite in range(len(nos)):
            caminho = []

            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
    
            while l1.vazio() == False:
                # remove o primeiro da pilha
                atual = l1.deletaUltimo()
                if atual is None: break
    
                if atual.valor2 < limite:
                    ind = nos.index(atual.valor1)
    
                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])-1,-1,-1):
        
                        novo = grafo[ind][i]
                        #print("\tFilho de atual: ",novo)
                        flag = True  # pressuponho que não foi visitado
        
                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                            
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                #print("Árvore de busca:\n",l2.exibeLista())
                                return caminho

        return "caminho não encontrado"

    def bidirecional(self, inicio, fim):

        # listas para a busca a partir da origem - busca 1
        l1 = lista()      # busca na FILA
        l2 = lista()      # cópia da árvore completa

        # listas para a busca a partir da destino -  busca 2
        l3 = lista()      # busca na FILA
        l4 = lista()      # cópia da árvore completa

        # cria estrutura para controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
        linha = []
        linha.append(fim)
        linha.append(2)
        visitado.append(linha)
        
        while True:
            
            # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
            flag1 = True
            while flag1:
                atual = l1.deletaPrimeiro()
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 1:
                                # visitado na mesma árvore
                                flag2 = False
                            else:
                                # visitado na outra árvore
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l2.exibeCaminho()
                            #caminho = caminho[::-1]
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                        # if flag3
                    # if flag2
                # for i
                
                
                if(l1.vazio()!=True):
                    aux = l1.primeiro()
                    if aux.valor2 == atual.valor2:
                        flag1 = True
                    else:
                        flag1 = False                

            # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                if atual==None:
                    break
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break

                    if flag2:
                        l3.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l4.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l4.exibeCaminho()
                            caminho = caminho[::-1]
                            caminho += l2.exibeCaminho1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)
                        
                if(l3.vazio() != True):
                    aux = l3.primeiro()
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False

nos = [
    "ABANDONED STATE BUILDING",  # 1
    "ARCANA PLATEAU",  # 2
    "AURORA LAKE",  # 3
    "BIOME RESEARCH LAB",  # 4
    "BIOME TEST SITE",  # 5
    "BONNEVILLE",  # 6
    "DUMPING GROUND",  # 7
    "FIELDS OF PERKAU",  # 8
    "FORAIN FOREST",  # 9
    "JUPIA ROAD",  # 10
    "KIDEL AETHERINE PLANT",  # 11
    "KIDEL CROSSING",  # 12
    "KIDEL TAIREN BASE",  # 13
    "LESHY FOREST",  # 14
    "MANNSTAND FORTRESS",  # 15
    "RANMELLE",  # 16
    "RICHMONDE",  # 17
    "SAFEHOLD DEFENSE LINE",  # 18
    "SAFEHOLD",  # 19
    "TAIREN ROBOT FACTORY",  # 20
    "TIAMAN",  # 21
    "WRAITH'S FOOTHOLD",  # 22
    "ZEKEBEN ROAD"  # 23
]

grafo = [
    ["ARCANA PLATEAU", "MANNSTAND FORTRESS"],   # 1
    ["ZEKEBEN ROAD", "ABANDONED STATE BUILDING"],   # 2
    ["BONNEVILLE"],   # 3
    ["BIOME TEST SITE", "FIELDS OF PERKAU"],   # 4
    ["BIOME RESEARCH LAB", "LESHY FOREST"],   # 5
    ["AURORA LAKE", "SAFEHOLD"],   # 6
    ["SAFEHOLD DEFENSE LINE", "ZEKEBEN ROAD", "FIELDS OF PERKAU"],   # 7
    ["BIOME RESEARCH LAB", "LESHY FOREST", "DUMPING GROUND"],   # 8
    ["RICHMONDE"],   # 9
    ["TAIREN ROBOT FACTORY"],   # 10
    ["KIDEL TAIREN BASE"],   # 11
    ["SAFEHOLD", "RANMELLE"],   # 12
    ["KIDEL AETHERINE PLANT", "SAFEHOLD DEFENSE LINE"],   # 13
    ["TIAMAN", "FIELDS OF PERKAU", "BIOME TEST SITE", "TAIREN ROBOT FACTORY"],   # 14
    ["TIAMAN", "ABANDONED STATE BUILDING"],   # 15
    ["KIDEL CROSSING", "RICHMONDE"],   # 16
    ["RANMELLE", "FORAIN FOREST"],   # 17
    ["SAFEHOLD", "DUMPING GROUND", "KIDEL TAIREN BASE"],   # 18
    ["BONNEVILLE", "KIDEL CROSSING", "ZEKEBEN ROAD", "SAFEHOLD DEFENSE LINE"],   # 19
    ["LESHY FOREST", "JUPIA ROAD", "WRAITH'S FOOTHOLD"],   # 20
    ["LESHY FOREST", "MANNSTAND FORTRESS"],   # 21
    ["TAIREN ROBOT FACTORY"],   # 22
    ["ARCANA PLATEAU", "SAFEHOLD", "DUMPING GROUND"],   # 23
]

# PROGRAMA PRINCIPAL

sol = busca()
caminho = []

def runAmplitude(origem, destino):
    return sol.amplitude(origem, destino)

def runProfundidade(origem, destino):
    return sol.profundidade(origem, destino)

def runProfundidadeLimitada(origem, destino, limite):
    return sol.profundidade_limitada(origem, destino, limite)

def runAprofundamentoIterativo(origem, destino):
    return sol.aprofundamento_iterativo(origem, destino)

def runBidirecional(origem, destino):
    return sol.bidirecional(origem, destino)