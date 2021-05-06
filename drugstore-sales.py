def vendas():

    print("-" * 40)
    print("Central de Vendas".center(40))
    print("-" * 40)

    # =-= Data da compra =-= #
    data_compra = input("Digite a data da compra no formato"
                        "\ndd-mm-yyyy: ").replace("/", "-")
    if len(data_compra) != 10:
        print("O formato deve ser dia-mes-ano!")
        dia = input("Digite o dia: ")
        mes = input("Digite o mês: ")
        ano = input("Digite o ano:")
        data_compra = f"{dia}-{mes}-{ano}"

    # =-= Matrícula dos funcionários =-= #
    arquivo_funcionarios = open('funcionarios.txt', 'r', encoding='utf8')

    lista_funcionarios = []
    for linha in arquivo_funcionarios:
        if linha == "\n":
            continue
        else:
            funcionario = linha.split(" ")
            lista_funcionarios.append(funcionario)

    i = 0
    print("-" * 42)
    print("MATRÍCULA DOS FUNCIONÁRIOS".center(42))
    print("-" * 42)
    for i in range(len(lista_funcionarios)):
        print(f"{lista_funcionarios[i][1]:<20}........... {lista_funcionarios[i][0].zfill(10):<10}")
    print("-" * 42)

    matricula_funcionario = input("\nDigite a matrícula do funcionário: ")

    # =-= CPF do cliente =-= #
    n = 0
    while n == 0:
        try:
            lista_clientes = []
            procurar_cliente = input("Digite o CPF do cliente comprador: ")
            arquivo_clientes = open('clientes.txt', 'r', encoding='utf8')
            for linha in arquivo_clientes:
                if procurar_cliente in linha:
                    cliente = linha.split(" ")
                    lista_clientes.append(cliente)
                    nomecliente = cliente[0]
                    cpfcliente = cliente[1]
                    n += 1
            arquivo_clientes.close()

        # =-= Nome do cliente =-=#
            print("Cliente comprador:", cliente[0])
        except UnboundLocalError:
            print("Digite um CPF válido.")

    # =-= Compra =-= #
    i = 0
    valores_produtos = []
    valor_total = 0
    while i != -1:
        # Nome do medicamento
        nao_existe = True
        while nao_existe:

            procurar_medicamento = input("Digite o nome do medicamento: ").capitalize()

            arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
            for linha in arquivo_medicamentos:
                if procurar_medicamento in linha:
                    medicamento = linha.split(" ")
                    nomemedicamento = medicamento[0]
                    i = -1

                    if int(medicamento[4]) > 0:
                        nao_existe = False
                    else:
                        print("Não tem mais no estoque!")
            arquivo_medicamentos.close()

        # Quantidade
        qtd_invalida = True
        try:
            while qtd_invalida:
                quantidade = int(input("Agora digita a quantidade de medicamento que quer comprar: "))
                if quantidade > int(medicamento[4]):
                    print("Não possuímos esta quantia, possuímos apenas:", medicamento[4].strip(), "unidades")
                else:
                    qtd_invalida = False
                    print("Quantidade valida!")

                    nova_quantidade = int(medicamento[4].strip()) - quantidade

                    arquivo_medicamentos = open('medicamentos.txt', 'r', encoding='utf8')
                    arquivo_novo = open('novo.txt', 'w', encoding='utf8')

                    for linhamed in arquivo_medicamentos:
                        if procurar_medicamento in linhamed:
                            procurar_medicamento = linhamed
                            continue
                        else:
                            arquivo_novo.write(linhamed)
                    arquivo_medicamentos.close()
                    print(f"Medicamento comprado: {procurar_medicamento}")

                    arquivo_medicamentos.close()
                    arquivo_novo.close()

                    medicamento_editado = procurar_medicamento.split()
                    medicamento_editado[4] = nova_quantidade

                    novo_medicamento = f'{medicamento_editado[0].replace(" ", "_")} {medicamento_editado[1]} ' \
                                       f'{medicamento_editado[2]} {medicamento_editado[3]} {medicamento_editado[4]}'

                    arquivo_medicamentos = open('medicamentos.txt', 'w', encoding='utf8')
                    arquivo_novo = open('novo.txt', 'r', encoding='utf8')
                    for linhamed in arquivo_novo:
                        arquivo_medicamentos.write(linhamed)
                    arquivo_medicamentos.write(f"\n{novo_medicamento}")
                    arquivo_medicamentos.close()
                    arquivo_novo.close()

                    valor_produto = quantidade * float(medicamento_editado[2].strip())
                    valores_produtos.append([medicamento_editado[0], valor_produto])
                    valor_total = valor_total + valor_produto
                i = input("Digite -1 se quiser encerrar! "
                          "Se quiser continuar, aperte ENTER: ")
                try:
                    i = int(i)
                except ValueError:
                    i = 0
        except IndexError:
            print("Ocorreu um erro! Tente novamente!")
            input("Digite ENTER pra recomeçar")
            vendas()

    # =-=  Valor total por produto =-= #
    i = 0
    for produto in valores_produtos:
        print(f"{i+1}. {valores_produtos[i][0]}.........R${valores_produtos[i][1]}")
        i += 1

    # =-= Valor total da compra =-= #
    print(f"Valor total: R${valor_total}")

    # =-= Método de pagamento =-= #
    print("Escolha um método de pagamento:")
    print("\n1 - À vista \n2 - Débito \n3 - Crédito ")
    metodo_pagamento = int(input("Digite a opção: "))

    if metodo_pagamento == 1:
        metodo_pagamento = "À vista"
    elif metodo_pagamento == 2:
        metodo_pagamento = "Débito"
    elif metodo_pagamento == 3:
        metodo_pagamento = "Crédito"

    # =-= Salvar nos arquivos =-= #
    arquivo_nota_fiscal = open(f"{nomecliente}_{data_compra}.txt", "w", encoding="utf8")

    arquivo_nota_fiscal.write(f"Data da compra: {data_compra} \n"
                              f"Matrícula do funcionário: {matricula_funcionario} \n"
                              f"CPF do cliente: {cpfcliente} \n"
                              f"Nome do cliente: {nomecliente} \n")
    i = 0
    arquivo_nota_fiscal.write("-" * 30 + "\n")
    arquivo_nota_fiscal.write("VALOR DA COMPRA\n".center(30))
    for produto in valores_produtos:
        arquivo_nota_fiscal.write(f"{i+1}. {valores_produtos[i][0]}.........R${valores_produtos[i][1]} \n")
        i += 1
    arquivo_nota_fiscal.write(f"Valor total da compra ......... R${valor_total} \n"
                              f"Método de pagamento: {metodo_pagamento}")
    arquivo_nota_fiscal.close()

    arquivo_nota_fiscal = open(f"{nomecliente}_{data_compra}.txt", "r", encoding="utf8")
    arquivo_vendas = open("vendas.txt", "a", encoding="utf8")
    for linha in arquivo_nota_fiscal:
        arquivo_vendas.write(linha)
    arquivo_vendas.write(f"\n\n{'-'*30}\n\n")
    arquivo_vendas.close()
    arquivo_nota_fiscal.close()

    print("-" * 30)
    print("Venda realizada com sucesso!!!".center(30))
    print("-" * 30)
    print(f"Data da compra: {data_compra} \n"
          f"Matrícula do funcionário: {matricula_funcionario} \n"
          f"CPF do cliente: {cpfcliente} \n"
          f"Nome do cliente: {nomecliente} \n")
    i = 0
    print("-" * 30 + "\n")
    print("VALOR DA COMPRA\n".center(30))
    for produto in valores_produtos:
        print(f"{i + 1}. {valores_produtos[i][0]}.........R${valores_produtos[i][1]} \n")
        i += 1
    print(f"Valor total da compra ......... R${valor_total} \n"
          f"Método de pagamento: {metodo_pagamento}")


vendendo = True
while vendendo:
    vendas()
    print("-" * 30)
    continuar = input("Se quiser fazer mais uma venda, aperte ENTER. \n"
                      "Se quiser finalizar, digite -1: ")
    if continuar == "-1":
        vendendo = False
