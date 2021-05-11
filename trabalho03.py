from pilha import Pilha

file = open('teste.txt', 'r')
p = Pilha()


def matches(ope, close):
    opens = ['<html>', '<body>', '<head>', '<title>', '<center>', '<h1>', '<p>', '<ol>', '<li>']
    closes = ['</html>', '</body>', '</head>', '</title>', '</center>', '</h1>', '</p>', '</ol>', '</li>']
    # verifica se o indice da tag que abre corresponde à que fecha
    return opens.index(ope) == closes.index(close)


balanced = True
search = file.read()
# lista com tadas as palavras do texto
searchlist = search.split()

for word in searchlist:
    # print(i)
    # se a palavra não começar com '</' então é tag de entrada
    if word[0] == "<" and word[1] != "/":
        # adiciona a pilha
        p.push(word)
    elif word[0] == "<" and word[1] == "/":
        # se for tag de saida primeiro verifica se a pilha está vazia
        if p.isEmpty():
            # se estiver esta sobrando tag de saida então tem erro
            print(f'Erro! TAG {p.items[-1]} não foi fechada corretamente.')
            balanced = False
            break
        else:
            # se não estiver vazia adiciona a tag de saida no topo da pilha p
            top = p.pop()
            # se a tag do topo não combina com a tag atual verificada então tem erro
            if not matches(top, word):
                print(f'Erro! TAG {p.items[-1]} não foi fechada corretamente.')
                balanced = False
                break

if balanced:
    print('Tags bem formadas.')

