def Comissaosalario():
    nome = input("entre com o nome do vendedor")
    salariofixo = float(input("informe o salario"))
    vendas = float(input("informe o total de vendas"))
    comissao = 0.15*vendas
    pagamentoesperado = salariofixo+comissao

    return nome, salariofixo, vendas, pagamentoesperado

if __name__ == "__main__":
    nome, comissao, vendas, pegamentoesperado = Comissaosalario()
    strg = "{0} obteve R$: {1:.2f} de comissao e vai receber: {2:.2f}".format(nome,vendas,comissao)
    print(strg)