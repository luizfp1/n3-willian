import json
ARQUIVO = "dados.json"

try:
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        cadastros = json.load(f)
except FileNotFoundError:
    cadastros = []


def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=4)

def listar(lista):
    for i, pessoa in enumerate(lista):
        print(f"{i} - Nome: {pessoa['nome']} | Cidade: {pessoa['cidade']} | Idade: {pessoa['idade']}")

while True:
    print("\n1-Incluir | 2-Alterar | 3-Excluir | 4-Pesquisar | 5-Listar Ordenado | 0-Sair")
    op = input("Opcao: ")
    
    if op == "1":  
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        idade = int(input("Idade: "))
        cadastros.append({"nome": nome, "cidade": cidade, "idade": idade})
        salvar()
        print("Cadastrado") 

    elif op == "2":  
        listar(cadastros)
        idx = int(input("Numero do cadastro para alterar: "))
        cadastros[idx]["nome"] = input("Novo nome: ")
        cadastros[idx]["cidade"] = input("Nova cidade: ")
        cadastros[idx]["idade"] = int(input("Nova idade: "))
        salvar()
        print("Alterado")

    elif op == "3":  
        listar(cadastros)
        idx = int(input("Numero do cadastro para excluir: "))
        cadastros.pop(idx)
        salvar()
        print("Excluido")

    elif op == "4":  
        campo = input("Pesquisar por (nome ou cidade): ").lower()
        busca = input("Digite o texto: ").lower()
        for pessoa in cadastros:
            if busca in pessoa[campo].lower():
                print(pessoa)

    elif op == "5": 
        escolha = input("Ordenar por (1-Nome / 2-Idade): ")
        if escolha == "1":
            ordenados = sorted(cadastros, key=lambda x: x["nome"].lower())
        else:
            ordenados = sorted(cadastros, key=lambda x: x["idade"])
        listar(ordenados)

    elif op == "0":
        break



