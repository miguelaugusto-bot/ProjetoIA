import os
import urllib.request
import sys

#os caminhos das pastas e arquivos (isso é mais para o fasttext)
url_download= 'https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz'
path_data = 'data'
arquivo_fasttext = 'cc.pt.300.vec.gz'
path_fasttext = os.path.join(path_data, arquivo_fasttext)

def estrutura_pasta():
    pastas = ['data', 'models', 'reports', 'src', 'tests', 'notebooks', 'docs', 'scripts']

    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"[+] Pasta criada: {pasta}/")
        else:
            print(f"[OK] Pasta já existe: {pasta}/")

def baixar_fasttext():
    if not os.path.exists(path_fasttext):
        print("O arquivo do FastText não foi encontrado e terá que baixar (1.2GB)")
        print("Não se preocupe, a instalação sera automatica e precisa aguardar, por gentileza não feche a aba")
    
        try:
            urllib.request.urlretrieve(url_download, path_fasttext)
            print("[+] Download concluido")
        except Exception as e:
            print("[x] Erro ao baixar o arquivo")
            print("Efetue a instalação manual: https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz e depois insira na pasta data o arquivo que esta zipado")

def main():
    print("Realizando configuração do sistema helpdesk chatIA...")

    estrutura_pasta()
    baixar_fasttext()

    print("Configuração finalizada com êxito")
    print("Agora é necessario efetuar a intalação das dependências: pip install -r requirements.txt")
    print("Realizar o treinamento da IA no arquivo notebooks -> treinamento-lstm.ipynb")
    print("Para realizar teste manuais: notebooks -> exploracao.ipynb ")
    print("Para realizar teste automaticos: tests -> tests_intencao.py com o comando pytest em seu terminal")

if __name__ == "__main__":
    main()
