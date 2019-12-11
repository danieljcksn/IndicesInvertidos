def contaPalavra(arquivoIn, palavra):
    
    cont = 0
    global banco
    arquivo = open(arquivoIn,'r')
    banco = arquivo.read().split()
    for linha in banco:
        if linha == palavra:
            cont = cont + 1
    return cont


def geraTabelaIndices(enderecos, desc):
    #Criando um novo arquivo de palavras desconsideradas sem quebras de linha.
    desc = open(desc, 'r')
    desc = desc.readlines()
    desconsideradas = open('desconsideradas.txt', 'w')
    for i in desc:
        i = i.strip('\n')
        desconsideradas.write(i)
        desconsideradas.write(' ')
    desconsideradas.close()

    #Armazenando as palavras desconsideradas em uma lista, facilitando, portanto, a manipulacao.
    desconsideradas = open('desconsideradas.txt', 'r')
    arraydesc = desconsideradas.readline()
    arraydesc = arraydesc.split()
    print('Palavras a serem desconsideradas:', arraydesc)

    #Criando um novo arquivo de enderecos sem quebras de linha.
    enderecos = open(enderecos, 'r')
    enderecos = enderecos.readlines()
    caminhos = open('conjunto.txt', 'w')
    for i in enderecos:
        i = i.strip('\n')
        caminhos.write(i)
        caminhos.write(' ')
    caminhos.close()

    #Armazenando os enderecos em uma lista, facilitando, desse modo, a manipulacao.
    caminhos = open('conjunto.txt', 'r')
    arraycaminhos = caminhos.readline()
    arraycaminhos = arraycaminhos.split()
    print('Caminhos dos arquivos:', arraycaminhos)

    #Lendo todos os arquivos (a.txt, b.txt, c.txt) e eliminando os caracteres especiais (,! ?,)
    for i in arraycaminhos:
        #Abre objeto i (a.txt, b.txt ou c.txt) de arraycaminhos para eliminar os caracteres especiais
        arq = open(i, 'r')
        arq = arq.readlines()
        linhas = open(i, 'w')
        for k in arq:
            #Separa todas as palavras pelo espaco
            k = k.split()
            for j in k:
                #Elimina os caracteres especiais de cada palavra
                j = j.strip('\n,.?! ')
                #Escreve novamente a palavra apos formatacao no arquivo original
                linhas.write(j)
                linhas.write(' ')
        linhas.close()

    #Removendo todas as palavras que devem ser desconsideradas do arquivo.
    for i in arraycaminhos:
        arquivoIn = open(i, 'r')
        listaArquivo = arquivoIn.read()
        listaArquivo = listaArquivo.split()
        arquivoIn.close()
        w = len(listaArquivo)
        for k in range(w):
            for j in range(len(arraydesc)):
                if listaArquivo[k] == arraydesc[j]:
                    listaArquivo[k] = ''
                    #Substitui as palavras desconsideradas por um caractere nulo

        arquivoOut = open(i, 'w')
        for k in range(len(listaArquivo)):
            #Caso exista alguma palavra na posicao k da lista do arquivo, efetua a operacao de escrita.
            if listaArquivo[k] != '':
                arquivoOut.write(listaArquivo[k])
                arquivoOut.write(' ')
        arquivoOut.close()


    indices = open('indice.txt', 'w+')
    palavras = []

    #Gerando uma lista com as palavras que os arquivos possuem.
    for i in arraycaminhos:
        arquivoIn = open(i, 'r')
        listaArquivo = arquivoIn.read()
        listaArquivo = listaArquivo.split()
        arquivoIn.close()
        for k in range(len(listaArquivo)):
            if listaArquivo[k] in palavras:
                continue              
            else: 
                palavras.append(listaArquivo[k])

    indices = open('indice.txt', 'w+')
    for i in arraycaminhos:
        for w in range(len(palavras)):
            a = contaPalavra('a.txt', palavras[w])
            b = contaPalavra('b.txt', palavras[w])
            c = contaPalavra('c.txt', palavras[w])
            if i == 'a.txt' and a != 0:
                indices.write(palavras[w] + ': ' + '1' + ',' + str(a) + ' 2,' + str(b) + ' 3,' + str(c) + '\n')
            elif i == 'b.txt' and a == 0 and b != 0:
                indices.write(palavras[w] + ': ' + '1' + ',' + str(a) + ' 2,' + str(b) + ' 3,' + str(c) + '\n')
            elif i == 'c.txt' and a == 0 and b == 0:
                indices.write(palavras[w] + ': ' + '1' + ',' + str(a) + ' 2,' + str(b) + ' 3,' + str(c) + '\n')

    indices.close()
    ind = open('indice.txt', 'r')
    lerIndices = ind.readlines()
    print(lerIndices)
   
geraTabelaIndices('conjunto.txt', 'desconsideradas.txt')