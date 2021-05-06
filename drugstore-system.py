import sys

linha = '-' * 40
opcao_desejada = 0
opcao_clientes = 0


def menu():
    global opcao_desejada
    try:
        print(linha)
        print("Bem vindo a central da farmácia!".center(40))
        print(linha)
        print("\n 1 - Clientes \n 2 - Funcionários \n 3 - Medicamentos \n-1 - para encerrar o programa \n")
        opcao_desejada = int(input("Digite o número correspondente a opção desejada: "))

        if opcao_desejada == 1:
            try:
                print("Tem certeza que deseja entrar na central dos clientes?")
                op = int(input("1 - Sim\n2 - Não\n"))
                if op == 1:
                    clientes()
                elif op == 2:
                    menu()
                else:
                    print("AVISO: Digite uma opção válida")
                    menu()
            except ValueError:
                print("\nAVISO: A opção deve ser numérica\n")
                menu()

        elif opcao_desejada == 2:
            try:
                print("Tem certeza que deseja entrar na central dos funcionários?")
                op = int(input("1 - Sim\n2 - Não\n"))
                if op == 1:
                    funcionarios()
                elif op == 2:
                    menu()
                else:
                    print("AVISO: Digite uma opção válida")
                    menu()
            except ValueError:
                print("\nAVISO: A opção deve ser numérica\n")
                menu()

        elif opcao_desejada == 3:
            try:
                print("Tem certeza que deseja entrar na central dos medicamentos?")
                op = int(input("1 - Sim\n2 - Não\n"))
                if op == 1:
                    medicamentos()
                elif op == 2:
                    menu()
                else:
                    print("AVISO: Digite uma opção válida")
                    menu()

            except ValueError:
                print("\nAVISO: A opção deve ser numérica\n")
                menu()

        elif opcao_desejada == -1:
            sys.exit()
        else:
            print("AVISO: Digite uma opção válida")
            menu()

    except ValueError:
        print("\nAVISO: A opção deve ser numérica\n")
        menu()


def clientes():
    # =-= Menu Clientes =-= #
    print('-' * 40)
    print("Você está na central dos clientes".center(40))
    print('-' * 40)
    print("\n1 - Cadastrar\n2 - Editar\n3 - Remover\n4 - Buscar\n5 - Listar\n6 - Voltar pra o menu\n")
    print('-' * 40)
    opcao_clientes = input("Digite a opção desejada para a central dos clientes: ")

    # =-= Cadastrar Cliente =-= #
    if opcao_clientes == "1":
        print('-' * 40)
        print("Opção escolhida: 1 - CADASTRAR CLIENTE")
        print('-' * 40)
        cont = ""
        while cont != "SAIR":
            nome = str(input("Digite o nome do cliente: ")).capitalize()
            cpf = input(f"Digite o CPF de {nome}: ")
            data_nascimento = str(input("Digite a data de nascimento, exemplo: dd-mm-yyyy: "))
            idade = 0
            try:
                # Cálculo da idade
                data = data_nascimento.split('-')
                ano_atual = 2020
                idade = ano_atual - int(data[2])  # data[2] = ano de nascimento
            except IndexError:
                print("A data {} está no formato errado!".format(data_nascimento))
                print("Digite a data de nascimento no formato dd-mm-yyyy")
                data_nascimento = str(input("Digite novamente sua data de nascimento: "))
                data = data_nascimento.split('-')
                ano_atual = 2020
                idade = ano_atual - int(data[2])  # data[2] = ano de nascimento

            # Escrevendo no arquivo
            arquivo_clientes = open('clientes.txt', 'a', encoding='utf8')
            arquivo_clientes.write(f'{nome.replace(" ", "_")} {cpf} {data_nascimento} {str(idade)}\n')
            arquivo_clientes.close()

            print(f'Cliente adicionado com sucesso!! \n'
                  f'Nome: {nome} \n'
                  f'CPF: {cpf} \n'
                  f'Data de nascimento: {data_nascimento} \n'
                  f'Idade: {idade}')

            cont = input("Pressione ENTER para cadastrar mais um cliente, ou digite 'sair' "
                         "para voltar para a central: ").upper()
            if cont == "SAIR":
                clientes()
            elif cont == "":
                continue
            else:
                print("AVISO: Digite uma opção válida")
                clientes()

    # =-= Editar Cliente =-= #
    elif opcao_clientes == "2":
        try:
            print('-' * 40)
            print("\n Opcão escolhida: 2 - EDITAR CLIENTE")
            print('-' * 40)
            procurar_cliente = input("Digite o CPF do cliente que você quer editar: ")
            arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')
            arquivo_novo = open('novo.txt', 'w', encoding='utf8')

            for linha in arquivo_clientes:
                if procurar_cliente in linha:
                    procurar_cliente = linha
                    continue
                else:
                    arquivo_novo.write(linha)
            arquivo_clientes.close()

            cliente_editado = procurar_cliente.split(" ")
            print(f'Você está editando o seguinte cliente: \n'
                  f'Nome: {cliente_editado[0].replace(" ", "_")} \n'
                  f'CPF: {cliente_editado[1]} \n'
                  f'Data de nascimento: {cliente_editado[2]} \n'
                  f'Idade: {str(cliente_editado[3])}')

            try:
                print("1 - Editar nome \n2 - Editar CPF\n3 - Editar data de nascimento")
                opcao = int(input("Digite a opção: "))

                if opcao == 1:
                    cliente_editado[0] = input("Digite o novo nome: ").replace(" ", "_").capitalize()
                if opcao == 2:
                    cliente_editado[1] = input("Digite o novo CPF: ")
                if opcao == 3:
                    cliente_editado[2] = input("Digite a nova data de nascimento no formato dd-mm-yyyy: ")
                    try:
                        # Cálculo da idade
                        data = cliente_editado[2].split('-')
                        ano_atual = 2020
                        cliente_editado[3] = ano_atual - int(data[2])  # cliente_editado[2] = ano de nascimento
                    except IndexError:
                        print("A data {} está no formato errado!".format(cliente_editado[2]))
                        print("Digite a data de nascimento no formato dd-mm-yyyy")
                        cliente_editado[2] = str(input("Digite novamente sua data de nascimento: "))
                        data = cliente_editado[2].split('-')
                        ano_atual = 2020
                        cliente_editado[3] = ano_atual - int(data[2])  # cliente_editado[2] = ano de nascimento
                else:
                    print("Opção invalida!")
                    input("Aperte enter pra voltar pra a central de clientes.\n")
                    clientes()

                cliente_editado = f'{cliente_editado[0].replace(" ", "_")} {cliente_editado[1]} {cliente_editado[2]} {str(cliente_editado[3])}'
                arquivo_novo.write(cliente_editado)
                arquivo_novo.close()

                arquivo_clientes = open('clientes.txt', 'w', encoding='utf8')
                arquivo_novo = open('novo.txt', 'r', encoding='utf8')
                for linha in arquivo_novo:
                    arquivo_clientes.write(linha)
                arquivo_clientes.close()
                arquivo_novo.close()
                print(f"Cliente editado com sucesso!")
                print(f"Novo cliente: {cliente_editado}")
            except IndexError:
                print("AVISO: Digite um cliente válido para editar!")
            input("Digite ENTER pra voltar pra central de clientes.\n")
            clientes()
        except IndexError:
            print("AVISO: Digite um cliente válido para editar!")
        input("Digite ENTER pra voltar pra central de clientes.\n")
        clientes()

    # =-= Remover Cliente =-= #
    elif opcao_clientes == "3":
        print('-' * 40)
        print("\n Opcão escolhida: 3 - REMOVER CLIENTE")
        print('-' * 40)
        cliente_removido = input("Digite o CPF do cliente que você quer remover: ")
        arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')
        arquivo_novo = open('novo.txt', 'w', encoding='utf8')

        for linha in arquivo_clientes:
            if cliente_removido in linha:
                removeu = linha
                continue
            else:
                arquivo_novo.write(linha)
        arquivo_clientes.close()
        arquivo_novo.close()

        arquivo_clientes = open('clientes.txt', 'w', encoding='utf8')
        arquivo_novo = open('novo.txt', 'r', encoding='utf8')
        for linha in arquivo_novo:
            arquivo_clientes.write(linha)
        arquivo_clientes.close()
        arquivo_novo.close()
        print(f"Cliente removido: {removeu}")
        print(f"Removido com sucesso!")
        input("Pressione ENTER pra voltar pra central.\n")
        clientes()

    # =-= Buscar Cliente =-= #
    elif opcao_clientes == "4":
        print("\n Opcão escolhida: 4 - BUSCAR CLIENTE")
        print("\n1 - Procurar por CPF \n2 - Procurar por nome\n")
        opcao = int(input("Digite a opção:"))
        arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')

        if opcao == 1:
            procurar_cliente = input("Digite o CPF do cliente que você quer buscar: ")
            for linha in arquivo_clientes:
                if procurar_cliente in linha:
                    cliente_editado = linha

        if opcao == 2:
            procurar_cliente = input("Digite o nome do cliente que você quer buscar: ").capitalize()
            arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')
            for linha in arquivo_clientes:
                if procurar_cliente in linha:
                    cliente_editado = linha

        arquivo_clientes.close()
        try:
            print('-' * 40)
            print("CLIENTE ENCONTRADO".center(40))
            print('-' * 40)
            cliente = cliente_editado.split(" ")
            print(
                f'Nome: {cliente[0].replace("_", " ")}\n'
                f'CPF: {cliente[1]} \n'
                f'Data de Nascimento: {cliente[2]} \n'
                f'Idade: {cliente[3].strip()}')
            print('-' * 40)
        except NameError:
            print("CPF ou nome não encontrados!")
        input("Pressione ENTER pra voltar pra central.\n")
        clientes()

    # =-= Listar Clientes =-= #
    elif opcao_clientes == "5":
        print("\n Opcão escolhida: 5 - LISTAR CLIENTE")
        arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')

        i = 0
        lista_clientes = []
        for linha in arquivo_clientes:
            if linha == "" or linha == "\n":
                continue
            else:
                cliente = linha.split(" ")
                lista_clientes.append(cliente)
                i += 1

        i = 0
        print("-" * 80)
        print(f"{'NOME'.center(20):20}{'CPF'.center(20):20}{'DATA NASCIMENTO'.center(20):20}{'IDADE'.center(20):20}")
        print("-" * 80)
        for i in range(len(lista_clientes)):
            print(
                f"{lista_clientes[i][0][:20].center(20).capitalize()} "  # Nome
                f"{lista_clientes[i][1].center(20):20} "  # CPF
                f"{lista_clientes[i][2].center(20):20} "  # Data de nascimento
                f"{lista_clientes[i][3].strip().center(20):20}")  # Idade
        print("-" * 80)
        input("Aperte ENTER pra retornar à central de Clientes!\n")
        clientes()

    # =-= Voltar pra o menu =-= #
    elif opcao_clientes == "6":
        menu()
    else:
        print("AVISO: Digite uma opção válida")
        clientes()


def funcionarios():
    # =-= Menu Funcionários =-= #
    print("\n\n")
    print('-' * 40)
    print("Você está na central dos funcionários".center(40))
    print('-' * 40)
    print("\n1 - Cadastrar\n2 - Editar\n3 - Remover\n4 - Buscar\n5 - Listar\n6 - Voltar pra o menu")
    opcao = input("\nDigite a opção desejada para a central dos funcionários: ")

    # =-= Cadastrar Funcionário =-= #
    if opcao == "1":
        print('-' * 40)
        print("Opção escolhida: 1 - CADASTRAR FUNCIONÁRIO")
        print('-' * 40)
        cont = ""
        while cont != "Sair":
            matricula = input("Digite a matrícula do funcionário: ")
            nome = input("Digite o nome do funcionário: ").capitalize()
            data_nascimento = input("Digite sua data de nascimento, exemplo: dd-mm-yyyy: ")
            idade = 0
            try:
                # Cálculo da idade
                data = data_nascimento.split('-')
                ano_atual = 2020
                idade = ano_atual - int(data[2])  # data[2] = ano de nascimento
            except IndexError:
                print("A data {} está no formato errado!".format(data_nascimento))
                print("Digite a data de nascimento no formato dd-mm-yyyy")
                data_nascimento = input("Digite novamente a data de nascimento: ")
            data_admissao = input("Digite a data de admissão: ")

            # Escrevendo no arquivo
            arquivo_funcionarios = open('funcionarios.txt', 'a', encoding='utf8')
            arquivo_funcionarios.write(f'\n{matricula} {nome.replace(" ", "_")} '
                                       f'{data_nascimento} {str(idade)} {data_admissao}\n')
            arquivo_funcionarios.close()

            cont = input("Pressione ENTER para cadastrar mais um funcionário, "
                         "ou digite 'sair' para voltar para a central de funcionários: ").lower()
            if cont == "sair":
                print("\nOpção escolhida: VOLTAR A CENTRAL DOS FUNCIONÁRIOS")
                funcionarios()

    # =-=-= Editar Funcionário =-=-= #
    elif opcao == "2":
        print('-' * 40)
        print("\n Opcão escolhida: 2 - EDITAR FUNCIONÁRIO")
        print('-' * 40)
        procurar_funcionario = input("Digite a matrícula do funcionário que você quer editar: ")
        arquivo_funcionarios = open('funcionarios.txt', 'r', encoding='utf8')
        arquivo_novo = open('novo.txt', 'w', encoding='utf8')

        for linha in arquivo_funcionarios:
            if procurar_funcionario in linha:
                procurar_funcionario = linha
                continue
            else:
                arquivo_novo.write(linha)
        arquivo_funcionarios.close()
        try:

            funcionario_editado = procurar_funcionario.split(" ")

            print('-' * 40)
            print("Você está editando o seguinte funcionário:")
            print(f'Matrícula: {funcionario_editado[0]} \n'
                  f'Nome: {funcionario_editado[1]} \n'
                  f'Data de nascimento: {funcionario_editado[2]} \n'
                  f'Idade {funcionario_editado[3]} \n'
                  f'Data de admissão: {funcionario_editado[4]}\n')
            print('-' * 40)

            print("1 - Editar Matrícula \n2 - Editar Nome\n3 - Editar data de nascimento \n4 - Editar data de admissão")
            opcao = int(input("Digite a opção: "))

            if opcao == 1:
                funcionario_editado[0] = input("Digite a nova matrícula: ")
            if opcao == 2:
                funcionario_editado[1] = input("Digite o novo nome: ").capitalize()
            if opcao == 3:
                funcionario_editado[2] = input("Digite a nova data de nascimento no formato dd-mm-yyyy: ")
                try:
                    # Cálculo da idade
                    data = funcionario_editado[2].split('-')
                    ano_atual = 2020
                    funcionario_editado[3] = ano_atual - int(data[2])  # cliente_editado[2] = ano de nascimento
                except IndexError:
                    print("A data {} está no formato errado!".format(funcionario_editado[2]))
                    print("Digite a data de nascimento no formato dd-mm-yyyy")
                    funcionario_editado[2] = str(input("Digite novamente sua data de nascimento: "))
            if opcao == 4:
                funcionario_editado[4] = input("Digite a nova data de admissão: ")

            funcionario_editado = f'\n{funcionario_editado[0]} {funcionario_editado[1].replace(" ", "_")} ' \
                                  f'{funcionario_editado[2]} {str(funcionario_editado[3])} {funcionario_editado[4]}'
            arquivo_novo.write(funcionario_editado)
            arquivo_novo.close()

            arquivo_funcionarios = open('funcionarios.txt', 'w', encoding='utf8')
            arquivo_novo = open('novo.txt', 'r', encoding='utf8')
            for linha in arquivo_novo:
                arquivo_funcionarios.write(linha)
            arquivo_funcionarios.close()
            arquivo_novo.close()
            print(f"Funcionário editado com sucesso!")
            print(f"Funcionário editado: {funcionario_editado}")
            print('-' * 40)
        except IndexError:
            print("AVISO: Digite um funcionário válido para editar!")
        input("Aperte ENTER pra voltar pra a central de funcionários: \n")
        funcionarios()

    # =-=-= Remover Funcionário =-=-= #
    elif opcao == "3":
        print('-' * 40)
        print("\n Opcão escolhida: 3 - REMOVER FUNCIONÁRIO")
        print('-' * 40)
        funcionario_removido = input("Digite a matrícula do funcionário que você quer remover: ")
        arquivo_funcionarios = open('funcionarios.txt', 'r', encoding='utf8')
        arquivo_novo = open('novo.txt', 'w', encoding='utf8')

        for linha in arquivo_funcionarios:
            if funcionario_removido in linha:
                funcionario_removido = linha
                continue
            else:
                arquivo_novo.write(linha)
        arquivo_funcionarios.close()
        arquivo_novo.close()

        arquivo_funcionarios = open('funcionarios.txt', 'w', encoding='utf8')
        arquivo_novo = open('novo.txt', 'r', encoding='utf8')
        for linha in arquivo_novo:
            arquivo_funcionarios.write(linha)
        arquivo_funcionarios.close()
        arquivo_novo.close()
        print(f"Funcionário removido: {funcionario_removido}")
        print(f"Removido com sucesso!")
        input("Digite ENTER pra voltar pra central de funcionários.\n")
        funcionarios()

    # Buscar
    elif opcao == "4":
        print('-' * 40)
        print("\n Opcão escolhida: 4 - BUSCAR FUNCIONÁRIO")
        print('-' * 40)
        print("\n1 - Procurar por matrícula \n2 - Procurar por nome\n")
        opcao = input("Digite a opção: ")
        arquivo_funcionarios = open('funcionarios.txt', 'r', encoding='utf8')

        if opcao == "1":
            procurar_funcionario = input("Digite a matrícula do funcionário que você quer buscar: ")
            for linha in arquivo_funcionarios:
                if procurar_funcionario in linha:
                    funcionario_procurado = linha

        if opcao == "2":
            procurar_funcionario = input("Digite o nome do cliente que você quer buscar: ").capitalize()
            arquivo_funcionarios = open('clientes.txt', 'r', encoding='utf8')
            for linha in arquivo_funcionarios:
                if procurar_funcionario in linha:
                    funcionario_procurado = linha

        arquivo_funcionarios.close()
        try:
            funcionario = funcionario_procurado.split(" ")
            print(
                f'Matrícula: {funcionario[0]} \nNome: {funcionario[1].replace("_", " ")} \n'
                f'Data de Nascimento: {funcionario[2]} \nIdade: {funcionario[3]} \n'
                f'Data de admissão: {funcionario[4]}')
        except NameError:
            print("Matrícula ou nome não encontrados!")
        input("Digite ENTER pra voltar pra a central de funcionários.\n")
        funcionarios()

    # Listar
    elif opcao == "5":
        print("\n Opcão escolhida: 5 - LISTAR FUNCIONÁRIOS")
        arquivo_funcionarios = open('funcionarios.txt', 'r', encoding='utf8')

        lista_funcionarios = []
        for linha in arquivo_funcionarios:
            if linha == "\n":
                continue
            else:
                funcionario = linha.split(" ")
                lista_funcionarios.append(funcionario)

        i = 0
        print("-" * 110)
        print(f"{'MATRÍCULA'.center(20)}{'NOME'.center(30)}{'DATA NASCIMENTO'.center(20)}"
              f"{'IDADE'.center(20)} {'DATA DE ADMISSÃO'.center(20)}")
        print("-" * 110)
        for i in range(len(lista_funcionarios)):
            print(
                f"{lista_funcionarios[i][0]:^20} {lista_funcionarios[i][1].center(30):^30} "
                f"{lista_funcionarios[i][2].center(20):^20} {lista_funcionarios[i][3].center(20):^20} "
                f"{lista_funcionarios[i][4].strip().center(20):^20}")
        print("-" * 110)
        input("Digite ENTER pra voltar pra central de funcionários.\n")
        funcionarios()

    # =-= Voltar pra o menu =-= #
    elif opcao == "6":
        menu()

    else:
        print("Digite uma opção válida!!")
        funcionarios()


def medicamentos():
    linhamed = 0
    global medicamento_editado, opcaomed, arquivo_novo
    print('-' * 40)
    print("Você está na central dos medicamentos".center(40))
    print('-' * 40)
    print("\n1 - Cadastrar\n2 - Editar\n3 - Remover\n4 - Buscar\n5 - Listar\n6 - Voltar pra o menu\n")
    try:
        opcao_medicamentos = str(input("Digite a opção desejada para a central dos medicamentos: "))

        # =-= Cadastrar Medicamento =-= #
        if opcao_medicamentos == "1":
            print("Opção escolhida: 1 - CADASTRAR MEDICAMENTO")
            contmed = ""
            while contmed != "Sair":
                nomemed = str(input("Digite o nome do medicamento: ")).capitalize()
                laboratorio = str(input("Digite o laboratório em que foi feito: "))
                valor_med = input("Digite o valor do medicamento: ")
                if "," in valor_med:
                    valor_med.replace(",", ".")
                valor_med = float(valor_med)
                generico = str(input("Digite o  tipo do medicamento:\n 1 - Genérico\n 2 - Não genérico\n"))
                if generico == "1":
                    generico = "True"
                elif generico == "2":
                    generico = "False"
                else:
                    print("Valor invalido!")
                    input("Digite ENTER pra voltar pra central!")
                    medicamentos()
                try:
                    quantidade = int(input("Digite a quantidade que possui do mesmo: "))
                except NameError:
                    print("Valor invalido! Você deve digitar um número inteiro!")
                    input("Digite ENTER pra voltar pra central!")
                    medicamentos()

                # Escrevendo no arquivo
                arquivo_medicamentos = open('medicamentos.txt', 'a', encoding='utf8')
                arquivo_medicamentos.write(
                    f'\n{nomemed.replace(" ", "_")} {laboratorio} {valor_med} {generico} {quantidade}')
                arquivo_medicamentos.close()

                print("Medicamento adicionado com sucesso!")
                print(f"Nome: {nomemed} \n"
                      f"Laboratório: {laboratorio} \n"
                      f"Valor: R${valor_med} \n"
                      f"Genérico: {generico} \n"
                      f"Quantidade disponível: {quantidade}\n")

                contmed = input(
                    "Pressione ENTER para cadastrar mais um medicamento, ou digite 'sair' para voltar para a central: ").lower()
                if contmed == "sair":
                    medicamentos()

        # =-= Editar Medicamentos =-= #
        elif opcao_medicamentos == "2":
            print('-' * 40)
            print("\n Opcão escolhida: 2 - EDITAR Medicamentos")
            print('-' * 40)
            try:
                procurar_medicamento = input("Digite o nome do medicamento que você quer editar: ").capitalize()
                arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
                arquivo_novo = open('novo.txt', 'w', encoding='utf8')

                for linhamed in arquivo_medicamentos:
                    if procurar_medicamento in linhamed:
                        procurar_medicamento = linhamed
                        continue
                    else:
                        arquivo_novo.write(linhamed)
                arquivo_medicamentos.close()
                print(procurar_medicamento)
                medicamento_editado = procurar_medicamento.split()
            except FileNotFoundError:
                print("Este medicamento não está cadastrado")
                medicamentos()

            print(f"Medicamento editado: \n"
                  f"Nome {medicamento_editado[0]} \n"
                  f"Laboratório:{medicamento_editado[1]} \n"
                  f"Valor: R${medicamento_editado[2]:.2} \n"
                  f"Tipo: {medicamento_editado[3]} \n"
                  f"Quantidade disponível: {medicamento_editado[4]}")

            print("1 - Editar nome \n2 - Editar laboratório\n3 - Editar valor\n"
                  "4 - Editar tipo \n5 - Editar quantidade")
            opcaomed = int(input("Digite a opção: "))
            if opcaomed == 1:
                medicamento_editado[0] = input("Digite o novo nome: ").capitalize()
            if opcaomed == 2:
                medicamento_editado[1] = input("Digite o novo Laboratório ")
            if opcaomed == 3:
                medicamento_editado[2] = input("Digite um novo valor: ")
            if opcaomed == 4:
                medicamento_editado[3] = input("Digite um novo tipo;\n 1 - Genérico\n 2 - Não genérico")
                if medicamento_editado[3] == "1":
                    medicamento_editado[3] = "True"
                elif medicamento_editado[3] == "2":
                    medicamento_editado[3] = "False"
            if opcaomed == 5:
                medicamento_editado[4] = input("Digite uma nova quantidade: ")

            medicamento_editado = f'\n{medicamento_editado[0].replace(" ", "_")} {medicamento_editado[1]} ' \
                                  f'{medicamento_editado[2]} {medicamento_editado[3]} {medicamento_editado[4]}'
            print(medicamento_editado)
            medicamento_editado2 = medicamento_editado
            arquivo_novo.write(medicamento_editado2)
            arquivo_novo.close()

            arquivo_medicamentos = open('medicamentos.txt', 'w', encoding='utf8')
            arquivo_novo = open('novo.txt', 'r', encoding='utf8')
            for linhamed in arquivo_novo:
                arquivo_medicamentos.write(linhamed)
            arquivo_medicamentos.close()
            arquivo_novo.close()
            print(f"Medicamento editado com sucesso!")
            print(f"Novo medicamento: ", medicamento_editado2)
            input("Digite ENTER pra voltar pra central de medicamentos. \n")
            medicamentos()


        # Remover
        elif opcao_medicamentos == "3":
            print('-' * 40)
            print("\n Opcão escolhida: 3 - REMOVER MEDICAMENTO")
            print('-' * 40)
            medicamento_removido = input("Digite o nome do medicamento que você quer remover: ").capitalize()
            arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
            arquivo_novo = open('novo.txt', 'w', encoding='utf8')

            for linhamed in arquivo_medicamentos:
                if medicamento_removido in linhamed:
                    removeu = linhamed
                    continue
                else:
                    arquivo_novo.write(linhamed)
            arquivo_medicamentos.close()
            arquivo_novo.close()

            arquivo_medicamentos = open('medicamentos.txt', 'w', encoding='utf8')
            arquivo_novo = open('novo.txt', 'r', encoding='utf8')
            for linhamed in arquivo_novo:
                arquivo_medicamentos.write(linhamed)
            arquivo_medicamentos.close()
            arquivo_novo.close()
            print(f"Medicamento removido: {removeu}")
            print("Removido com sucesso!")
            input("Digite ENTER pra voltar pra central de medicamentos. \n")
            medicamentos()

        # Buscar
        elif opcao_medicamentos == "4":
            # =-= Buscar Medicamento =-= #
            print('-' * 40)
            print("\n Opcão escolhida: 4 - BUSCAR MEDICAMENTO")
            print('-' * 40)
            procurar_medicamento = input("Digite o nome do medicamento que você quer buscar: ").capitalize()
            arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
            for linhamed in arquivo_medicamentos:
                if procurar_medicamento in linhamed:
                    medicamento_editado = linhamed
            arquivo_medicamentos.close()
            try:
                medicamento = medicamento_editado.split(" ")
                print(
                    f'Nome: {medicamento[0].replace("_", " ")}\n'
                    f'Laboratório: {medicamento[1]} '
                    f'\nValor: {medicamento[2]} '
                    f'\nTipo: {medicamento[3]} \n'
                    f'Quantidade: {medicamento[4]}')
            except NameError:
                print("Medicamento não encontrado")
            input("Digite ENTER pra voltar pra central de medicamentos. \n")
            medicamentos()

        # Listar
        elif opcao_medicamentos == "5":
            print("\n Opcão escolhida: 5 - LISTAR MEDICAMENTOS")
            arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
            i = 0
            lista_medicamentos = []
            for linhamed in arquivo_medicamentos:
                if linhamed == "" or linhamed == "\n":
                    continue
                else:
                    medicamento = linhamed.split(" ")
                    lista_medicamentos.append(medicamento)
                    i += 1

            i = 0
            print("-" * 100)
            print(f"{'NOME'.center(20):20}{'LABORATÓRIO'.center(20):20}{'VALOR'.center(20):20}"
                  f"{'TIPO'.center(20):20}" f"{'QUANTIDADE'.center(20):20}")
            print("-" * 100)
            for i in range(len(lista_medicamentos)):
                if lista_medicamentos[i][3] == "True":
                    lista_medicamentos[i][3] = "Genérico"
                else:
                    lista_medicamentos[i][3] = "Não Genérico"
                print(
                    f"{lista_medicamentos[i][0].center(20):20} {lista_medicamentos[i][1].center(20):20} "
                    f"{lista_medicamentos[i][2].center(20):20} {lista_medicamentos[i][3].strip().center(20):20}"
                    f"{lista_medicamentos[i][4].center(20).strip():20}")
            print("-" * 100)
            input("Digite ENTER pra voltar pra central de medicamentos. \n")
            medicamentos()

        elif opcao_medicamentos == "6":
            menu()

        else:
            print("Digite uma opção válida")
            medicamentos()
    except ValueError:
        print("\nAVISO: A opção deve ser numérica\n")
        menu()


menu()
