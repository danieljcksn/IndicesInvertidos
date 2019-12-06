def geraTabelaIndices(endereços, desc):
    #Criando um novo arquivo de palavras desconsideradas sem quebras de linha.
    desc = open(desc, 'r')
    desc = desc.readlines()
    desconsideradas = open('desconsideradas.txt', 'w')
    for i in desc:
        i = i.strip('\n')
        desconsideradas.write(i)
        desconsideradas.write(' ')
    desconsideradas.close()

    #Armazenando as palavras desconsideradas em uma lista, facilitando, portanto, a manipulação.
    desconsideradas = open('desconsideradas.txt', 'r')
    arraydesc = desconsideradas.readline()
    arraydesc = arraydesc.split()
    print('Palavras a serem desconsideradas:', arraydesc)

    #Criando um novo arquivo de endereços sem quebras de linha.
    endereços = open(endereços, 'r')
    endereços = endereços.readlines()
    caminhos = open('caminhos.txt', 'w')
    for i in endereços:
        i = i.strip('\n')
        caminhos.write(i)
        caminhos.write(' ')
    caminhos.close()

    #Armazenando os endereços em uma lista, facilitando, desse modo, a manipulação.
    caminhos = open('caminhos.txt', 'r')
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
            #Separa todas as palavras pelo espaço
            k = k.split()
            for j in k:
                #Elimina os caracteres especiais de cada palavra
                j = j.strip('\n,.?! ')
                #Escreve novamente a palavra após formatação no arquivo original
                linhas.write(j)
                linhas.write(' ')
        linhas.close()

    #Removendo todas as palavras que devem ser desconsideradas do arquivo.
    for i in arraycaminhos:
        arquivoIn = open(i, 'r')
        listaArquivo = arquivoIn.read()
        listaArquivo = listaArquivo.split()
        arquivoIn.close()
        print('Arquivo', i, 'antes das remoções:', listaArquivo)
        w = len(listaArquivo)
        for k in range(w):
            for j in range(len(arraydesc)):
                if listaArquivo[k] == arraydesc[j]:
                    listaArquivo[k] = ''
                    #Substitui as palavras desconsideradas por um caractere nulo

        arquivoOut = open(i, 'w')
        for k in range(len(listaArquivo)):
            #Caso exista alguma palavra na posição k da lista do arquivo, efetua a operação de escrita.
            if listaArquivo[k] != '':
                arquivoOut.write(listaArquivo[k])
                arquivoOut.write(' ')
        print('Arquivo', i, 'após as remoções:', listaArquivo)

geraTabelaIndices('conjunto.txt', 'desconsideradas.txt')