# -*- coding: utf-8 -*-

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1        # valor do nó na árvore
        self.valor2    = valor2        # custo do caminho até o nó atual
        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):

        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break

            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


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

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            str.append(aux.estado)
            aux = aux.proximo

        return str

    def exibeArvore(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def exibeArvore1(self,s):


        atual = self.head
        while atual.estado != s:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def exibeArvore2(self, s, v1):

        atual = self.tail

        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior

        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail

class busca(object):

    def custo_uniforme(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                #print(l1.exibeArvore())
                #print(l2.exibeArvore())
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            visitado[j][1]=v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v1, atual)
                    l2.inserePos_X(novo, v1, v1, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"


    def greedy(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                ind1 = nos.index(grafo[ind][i][0])

                # HEURÍSTICA DO NÓ ATUAL ATÉ O OBJETIVO
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = h[ind1]

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1

                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"


    def a_estrela(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]
                ind1 = nos.index(grafo[ind][i][0])

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = v2 + h[ind1]

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"


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

h = [366,0,160,242,161,178,77,151,226,244,241,234,380,98,193,253,329,80,199,374,57,27,38]

grafo = [
    [["ARCANA PLATEAU", 189], ["MANNSTAND FORTRESS", 13]],   # 1
    [["ZEKEBEN ROAD", 58], ["ABANDONED STATE BUILDING", 232]],   # 2
    [["BONNEVILLE", 140]],   # 3
    [["BIOME TEST SITE", 17], ["FIELDS OF PERKAU", 78]],   # 4
    [["BIOME RESEARCH LAB", 51], ["LESHY FOREST", 53]],   # 5
    [["AURORA LAKE", 71], ["SAFEHOLD", 199]],   # 6
    [["SAFEHOLD DEFENSE LINE", 184], ["ZEKEBEN ROAD", 185], ["FIELDS OF PERKAU", 88]],   # 7
    [["BIOME RESEARCH LAB", 61], ["LESHY FOREST", 71], ["DUMPING GROUND", 352]],   # 8
    [["RICHMONDE", 366]],   # 9
    [["TAIREN ROBOT FACTORY", 161]],   # 1272
    [["KIDEL TAIREN BASE", 310]],   # 11
    [["SAFEHOLD", 151], ["RANMELLE", 216]],   # 12
    [["KIDEL AETHERINE PLANT", 237], ["SAFEHOLD DEFENSE LINE", 300]],   # 13
    [["TIAMAN", 281], ["FIELDS OF PERKAU", 999], ["BIOME TEST SITE", 19], ["TAIREN ROBOT FACTORY", 110]],   # 14
    [["TIAMAN", 39], ["ABANDONED STATE BUILDING", 325]],   # 15
    [["KIDEL CROSSING", 122], ["RICHMONDE", 269]],   # 16
    [["RANMELLE", 80], ["FORAIN FOREST", 323]],   # 17
    [["SAFEHOLD", 347], ["DUMPING GROUND", 113], ["KIDEL TAIREN BASE", 318]],   # 18
    [["BONNEVILLE", 304], ["KIDEL CROSSING", 188], ["ZEKEBEN ROAD", 30], ["SAFEHOLD DEFENSE LINE", 222]],   # 19
    [["LESHY FOREST", 332], ["JUPIA ROAD", 15], ["WRAITH'S FOOTHOLD", 40]],   # 20
    [["LESHY FOREST", 274], ["MANNSTAND FORTRESS", 186]],   # 21
    [["TAIREN ROBOT FACTORY", 67]],   # 22
    [["ARCANA PLATEAU", 17], ["SAFEHOLD", 1], ["DUMPING GROUND", 33]],   # 23
]


sol = busca()
caminho = []

def runCustoUniforme(inicio, fim):
    return sol.custo_uniforme(inicio, fim)

def runGreedy(inicio, fim):
    return sol.greedy(inicio, fim)

def runAEstrela(inicio, fim):
    return sol.a_estrela(inicio, fim)