

def palavraPorArquivo(nomeArquivo):
  arquivo = open(f'{nomeArquivo}', 'r', encoding='utf8')
  
  totalPalavras = []
  for e in arquivo:
    e = e.rstrip()
    totalPalavras.append(e.split(" "))  # PALAVRAS POR LINHA
    
  arquivo.close()
  
  # QUANTIDADE DE PALAVRAS NO ARQUIVO

  quantidadePalavras = 0
  for e in totalPalavras:
    quantidadePalavras += len(e)
  
  return str(quantidadePalavras)

  
def maioresPalavras(nomeArquivo):
  # AS 5 MAIORES PALAVRAS (QTD CARACTERES)
  arquivo = open(f'{nomeArquivo}', 'r', encoding='utf8')
  
  totalPalavras = []
  for e in arquivo:
    e = e.rstrip()
    totalPalavras.append(e.split(" "))  # PALAVRAS POR LINHA
    
  arquivo.close()

  totalPalavrasNew = []
  for linha in totalPalavras:
      listaTemp = []
      for palavra in linha:
        for caractere in palavra:
          if '.' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove('.')
            palavra = "".join(listaDeCaracteres)
          elif '...' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove('...')
            palavra = "".join(listaDeCaracteres)
          elif ',' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove(',')
            palavra = "".join(listaDeCaracteres)
          elif '"' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove('"')
            palavra = "".join(listaDeCaracteres)
          elif ';' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove(';')
            palavra = "".join(listaDeCaracteres)
          elif '(' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove('(')
            palavra = "".join(listaDeCaracteres)
          elif ')' in palavra:
            listaDeCaracteres = list(palavra)
            listaDeCaracteres.remove(')')
            palavra = "".join(listaDeCaracteres)
          else:
            listaTemp.append(palavra)
        listaTemp.append(palavra)
      totalPalavrasNew.append(listaTemp)

  
  cincoMaiores = {}
  
  MaioresDeCadaLinha = {}
  
  for linha in totalPalavrasNew:
      palavraQtd = {}
      for palavra in linha:
          qtdCaracteres = len(palavra)
          palavraQtd[f'{palavra}'] = qtdCaracteres
  
      maiorDaLinha = max(palavraQtd.values())
  
      for palavra, qtd in palavraQtd.items():
          if qtd == maiorDaLinha and qtd not in MaioresDeCadaLinha.values():
              MaioresDeCadaLinha[f'{palavra}'] = qtd

  
  maioresDaLinha = list(MaioresDeCadaLinha.values())
  maioresDaLinha.sort(reverse=True)
  maioresDaLinha = maioresDaLinha[:5]
  
  for palavra, qtd in MaioresDeCadaLinha.items():
      if qtd in maioresDaLinha and len(cincoMaiores) < 5:
          cincoMaiores[f'{palavra}'] = qtd

  
  return cincoMaiores

        
def vogalFrequente(nomeArquivo):
  # VOGAL QUE MAIS APARECE
  arquivo = open(f'{nomeArquivo}', 'r', encoding='utf8')
  
  totalPalavras = []
  for e in arquivo:
    e = e.rstrip()
    totalPalavras.append(e.split(" "))  # PALAVRAS POR LINHA
    
  arquivo.close()
  qtdA = 0
  qtdE = 0
  qtdI = 0
  qtdO = 0
  qtdU = 0

  for linha in totalPalavras:
      for palavra in linha:
        for caractere in palavra:
          if 'a' == caractere.lower():
              qtdA+=1
          elif 'e' == caractere.lower():
              qtdE+=1
          elif 'i' == caractere.lower():
              qtdI+=1
          elif 'o' == caractere.lower():
              qtdO+=1
          elif 'u' == caractere.lower():
              qtdU+=1
  
  vogais = {'Vogal A': qtdA, 'Vogal E': qtdE, 'Vogal I': qtdI, 'Vogal O': qtdO, 'Vogal U': qtdU}

  maiorQtd = max(vogais.values())

  for tipo, qtd in vogais.items():
      if qtd == maiorQtd:
          vogalMais = tipo

  
  return vogalMais


    # A LINHA QUE TEM A PALAVRA 'ÇÃO'
def linhaComString(nomeArquivo):
  arquivo = open(f'{nomeArquivo}', 'r', encoding='utf8')
  
  totalPalavras = []
  for e in arquivo:
    e = e.rstrip()
    totalPalavras.append(e.split(" "))  # PALAVRAS POR LINHA
    
  arquivo.close()
  
  linhasAchadas = []

  for linha in totalPalavras:
      for palavra in linha:
          if 'ção' in palavra.lower():
              linhasAchadas.append(" ".join(linha))
  
  
  return linhasAchadas

  

print("Quantidade de palavras no arquivo:", palavraPorArquivo('aparece.txt')+"\n")
print(f"Cinco maiores palavras: {maioresPalavras('aparece.txt')}\n")
print("A vogal que mais aparece é a:", vogalFrequente('aparece.txt')+"\n")
print("Linhas com a string ção:", linhaComString('aparece.txt'))
