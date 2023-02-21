# importando a lib para gerenciar os arquivos e pastar do diretorio
import os

# buscando o caminho geral do diretorio
cwd = os.getcwd()

# criando uma lista com as pastas disponiveis
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

# movendo os arquivos para fora da pasta
for folder in folder_list:
    path = os.path.join(cwd, folder)

    files = os.listdir(path)
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(cwd, file)
        os.replace(from_path, to_path)

    os.rmdir(path)