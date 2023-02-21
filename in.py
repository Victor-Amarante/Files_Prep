# importando a lib para gerenciar os arquivos e pastar do diretorio
import os

# buscando o caminho geral do diretorio
cwd = os.getcwd()

# criando uma lista com todos os arquivos e pastas do diretorio
full_list = os.listdir(cwd)

# criando uma lista sem pastas e sem arquivo .py
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]

# criando uma lista com valores unicos sobre as extensoes dos arquivos
types = list(set([i.split('.')[1] for i in files_list]))

# criando pastas de acordo com os nomes das extensoes
for file_type in types:
    os.mkdir(file_type)

# movendo os arquivos para as pastas com as mesmas extensoes 
for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[1], file)

    os.replace(from_path, to_path)
