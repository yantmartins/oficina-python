
def salvar_clientes():
    f = open("clientes.txt", "w")
    for c in clientes:
        cpf, nome, tel = c.split(";")
        linha = f"CPF: {cpf}; Nome: {nome}; Tel: {tel}\n"
        f.write(linha)
    f.close()

def salvar_veiculos():
    f = open("veiculos.txt", "w")
    for v in veiculos:
        placa, modelo, ano, cpf = v.split(";")
        linha = f"Placa: {placa}; Modelo: {modelo}; Ano: {ano}; CPF: {cpf}\n"
        f.write(linha)
    f.close()

def salvar_os():
    f = open("os.txt", "w")
    for o in ordens:
        num, desc, valor, cpf, placa = o.split(";")
        linha = f"OS: {num}; Descrição: {desc}; Valor: {valor}; CPF: {cpf}; Placa: {placa}\n"
        f.write(linha)
    f.close()

# === Função para carregar dados do arquivo ===
def carregar(arquivo):
    try:
        f = open(arquivo, "r")
        linhas = [linha.strip() for linha in f.readlines()]
        f.close()
        return linhas
    except:
        return []

# === FUNÇÕES DE CLIENTE ===

def cadastrar_cliente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    tel = input("Telefone: ")
    # Verifica se o CPF já existe na lista clientes
    for c in clientes:
        if c.split(";")[0] == cpf:
            print("CPF já existe.")
            return  
    # Adiciona novo cliente na lista clientes no formato "cpf;nome;tel"
    clientes.append(f"{cpf};{nome};{tel}")
    # Salva a lista atualizada no arquivo clientes.txt
    salvar_clientes()
    print("Cliente cadastrado.")

def listar_clientes():
    # Percorre e imprime cada cliente na lista clientes
    for c in clientes:
        print(c)

def editar_cliente():
    # Solicita CPF do cliente que deseja editar
    cpf = input("CPF do cliente: ")
    # Percorre os clientes para encontrar o CPF informado
    for i in range(len(clientes)):
        if clientes[i].split(";")[0] == cpf:
            # Solicita novo nome e telefone para atualizar
            nome = input("Novo nome: ")
            tel = input("Novo telefone: ")
            # Atualiza os dados do cliente na lista
            clientes[i] = f"{cpf};{nome};{tel}"
            # Salva os dados atualizados no arquivo
            salvar_clientes()
            print("Cliente atualizado.")
            return
    # Caso CPF não seja encontrado
    print("Cliente não encontrado.")

def excluir_cliente():
    # Solicita CPF do cliente para exclusão
    cpf = input("CPF do cliente: ")
    # Cria uma nova lista filtrando o CPF removido
    nova = [c for c in clientes if c.split(";")[0] != cpf]
    # Verifica se houve remoção
    if len(nova) < len(clientes):
        # Atualiza a lista clientes com a nova lista
        clientes[:] = nova
        # Também remove veículos e OS vinculados a esse CPF
        veiculos[:] = [v for v in veiculos if v.split(";")[3] != cpf]
        ordens[:] = [o for o in ordens if o.split(";")[3] != cpf]
        # Salva as listas atualizadas nos arquivos
        salvar_clientes()
        salvar_veiculos()
        salvar_os()
        print("Cliente e dados vinculados removidos.")
    else:
        print("CPF não encontrado.")

# === FUNÇÕES DE VEÍCULO ===

def cadastrar_veiculo():
    # Solicita placa do veículo
    placa = input("Placa: ")
    # Solicita modelo do veículo
    modelo = input("Modelo: ")
    # Solicita ano do veículo
    ano = input("Ano: ")
    # Solicita CPF do dono do veículo
    cpf = input("CPF do dono: ")
    # Verifica se o CPF informado existe nos clientes
    if not any(c.split(";")[0] == cpf for c in clientes):
        print("CPF não cadastrado.")
        return
    # Verifica se a placa já está cadastrada
    if any(v.split(";")[0] == placa for v in veiculos):
        print("Placa já cadastrada.")
        return
    # Adiciona novo veículo na lista veiculos
    veiculos.append(f"{placa};{modelo};{ano};{cpf}")
    # Salva a lista atualizada no arquivo
    salvar_veiculos()
    print("Veículo cadastrado.")

def listar_veiculos():
    # Percorre e imprime cada veículo na lista veiculos
    for v in veiculos:
        print(v)

def editar_veiculo():
    # Solicita placa do veículo a ser editado
    placa = input("Placa: ")
    # Procura o veículo na lista
    for i in range(len(veiculos)):
        if veiculos[i].split(";")[0] == placa:
            # Solicita novo modelo e ano para atualizar
            modelo = input("Novo modelo: ")
            ano = input("Novo ano: ")
            # CPF permanece o mesmo
            cpf = veiculos[i].split(";")[3]
            # Atualiza o veículo
            veiculos[i] = f"{placa};{modelo};{ano};{cpf}"
            # Salva a lista atualizada
            salvar_veiculos()
            print("Veículo atualizado.")
            return
    # Caso placa não encontrada
    print("Veículo não encontrado.")

def excluir_veiculo():
    # Solicita placa do veículo para exclusão
    placa = input("Placa: ")
    # Filtra a lista removendo o veículo da placa informada
    nova = [v for v in veiculos if v.split(";")[0] != placa]
    if len(nova) < len(veiculos):
        # Atualiza lista veiculos
        veiculos[:] = nova
        # Remove ordens de serviço vinculadas à placa removida
        ordens[:] = [o for o in ordens if o.split(";")[4] != placa]
        # Salva as listas atualizadas
        salvar_veiculos()
        salvar_os()
        print("Veículo e OS removidas.")
    else:
        print("Placa não encontrada.")

# === FUNÇÕES DE ORDEM DE SERVIÇO (OS) ===

def cadastrar_os():
    # Solicita número da OS
    num = input("Número da OS: ")
    # Solicita descrição do serviço
    desc = input("Descrição: ")
    # Solicita valor do serviço
    valor = input("Valor: ")
    # Solicita CPF do cliente
    cpf = input("CPF: ")
    # Solicita placa do veículo
    placa = input("Placa: ")
    # Verifica se CPF existe
    if not any(c.split(";")[0] == cpf for c in clientes):
        print("CPF inválido.")
        return
    # Verifica se placa existe
    if not any(v.split(";")[0] == placa for v in veiculos):
        print("Placa inválida.")
        return
    # Verifica se número da OS já existe
    if any(o.split(";")[0] == num for o in ordens):
        print("Número de OS já existe.")
        return
    # Adiciona nova OS na lista ordens
    ordens.append(f"{num};{desc};{valor};{cpf};{placa}")
    # Salva a lista atualizada no arquivo
    salvar_os()
    print("OS cadastrada.")

def listar_os():
    # Percorre e imprime todas as ordens na lista ordens
    for o in ordens:
        print(o)

def editar_os():
    # Solicita número da OS a ser editada
    num = input("Número da OS: ")
    # Procura pela OS na lista
    for i in range(len(ordens)):
        if ordens[i].split(";")[0] == num:
            # Solicita nova descrição e valor para atualizar
            desc = input("Nova descrição: ")
            valor = input("Novo valor: ")
            # CPF e placa permanecem iguais
            cpf = ordens[i].split(";")[3]
            placa = ordens[i].split(";")[4]
            # Atualiza a OS na lista
            ordens[i] = f"{num};{desc};{valor};{cpf};{placa}"
            # Salva as ordens atualizadas
            salvar_os()
            print("OS atualizada.")
            return
    # Caso OS não encontrada
    print("OS não encontrada.")

def excluir_os():
    # Solicita número da OS para exclusão
    num = input("Número da OS: ")
    # Filtra lista removendo a OS especificada
    nova = [o for o in ordens if o.split(";")[0] != num]
    if len(nova) < len(ordens):
        # Atualiza lista ordens
        ordens[:] = nova
        # Salva as ordens atualizadas
        salvar_os()
        print("OS removida.")
    else:
        print("OS não encontrada.")

# === MENU PRINCIPAL ===
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Editar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Cadastrar Veículo")
        print("6 - Listar Veículos")
        print("7 - Editar Veículo")
        print("8 - Excluir Veículo")
        print("9 - Cadastrar OS")
        print("10 - Listar OS")
        print("11 - Editar OS")
        print("12 - Excluir OS")
        print("0 - Sair")
        op = input("Opção: ")

        match op:
            case "1": cadastrar_cliente()
            case "2": listar_clientes()
            case "3": editar_cliente()
            case "4": excluir_cliente()
            case "5": cadastrar_veiculo()
            case "6": listar_veiculos()
            case "7": editar_veiculo()
            case "8": excluir_veiculo()
            case "9": cadastrar_os()
            case "10": listar_os()
            case "11": editar_os()
            case "12": excluir_os()
            case "0":
                print("Saindo.")
                break
            case _:
                print("Opção inválida.")

        # Depois de executar a ação, espera o usuário apertar Enter para continuar
        input("\nPressione Enter para voltar ao menu...")

# === INÍCIO DO PROGRAMA ===
# Carrega os dados dos arquivos para as listas
clientes = carregar("clientes.txt")
veiculos = carregar("veiculos.txt")
ordens = carregar("os.txt")

# Inicia o menu interativo
menu()
