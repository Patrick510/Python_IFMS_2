# 1 - Programa para copiar, mover, ou excluir um arquivo:
# Solicitar ao usuário um caminho de arquivo. Caso o arquivo não exista, ou seja um diretório, informar o usuário e encerrar o programa.
# Solicitar ao usuário se quer excluir, copiar, ou mover o arquivo. Caso o usuário escolha copiar ou mover o arquivo, solicitar ao usuário para onde copiar ou mover o arquivo.

from pathlib import Path
import shutil

def ex1():
    # Solicita o caminho do arquivo ao usuário
    path = Path(input("Digite o caminho de um arquivo: ").strip())

    # Solicita a ação desejada ao usuário
    action = input("Deseja excluir, copiar, ou mover o arquivo? (excluir(e)/copiar(c)/mover(m)) ").strip().lower()

    if action == "e":
        path.unlink()
        print(f"Arquivo '{path}' excluído com sucesso.")
    elif action == "c":
        new_path = Path(input("Digite o caminho completo para onde deseja copiar o arquivo (inclua o nome do arquivo): ").strip())
        shutil.copy(path, new_path)
        print(f"Arquivo '{path}' copiado para '{new_path}'.")
    elif action == "m":
        new_path = Path(input("Digite o caminho completo para onde deseja mover o arquivo (inclua o nome do arquivo): ").strip())
        shutil.move(path, new_path)
        print(f"Arquivo '{path}' movido para '{new_path}'.")
    else:
        print("Ação inválida. Por favor, escolha 'excluir', 'copiar' ou 'mover'.")

ex1()
