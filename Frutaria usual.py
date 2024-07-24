from re import error
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

Nome_Estoque = ['banana', 'laranja', 'maca', 'uva', 'ameixa']

Quantidade_Estoque = {
    'banana': 10,
    'laranja': 20,
    'maçã': 3,
    'uva': 5,
    'ameixa': 50
}
Preco_Estoque = {
    'banana': 1.75,
    'laranja': 2.00,
    'maçã': 3.00,
    'uva': 4.00,
    'ameixa': 5.00
}

Estoque = ",".join(Nome_Estoque)
print("Em nosso estoque temos:", Estoque)

try:
    Quantidade_frutas = int(input("Quantas frutas diferentes você vai comprar ?"))

    if Quantidade_frutas == 0:
        print("Número inválido")

    else:
        i = 1
        fruta_selecionada = []
        Valor_total = 0
        quantidade2 = 0
        for i in range(0, Quantidade_frutas):
            Fruta = input('Que fruta gostaria comprar ?:').lower()

            if Fruta in Nome_Estoque:
                if Fruta in fruta_selecionada:
                    print("Você já adicionou essa fruta.")

                else:
                    fruta_selecionada.append(Fruta)
                    print(
                        f"Nós temos {Quantidade_Estoque[Fruta]} {Fruta}s em nosso estoque, cada uma custando R${Preco_Estoque[Fruta]:.2f}"
                    )
                    quantidade = int(
                        input(f'Quantas {Fruta}s gostaria comprar ?:')
                    )
                    quantidade2 += quantidade

                    if quantidade <= 0:
                        print('Essa quantidade não é válida')

                    elif quantidade <= Quantidade_Estoque[Fruta]:
                        Valor = quantidade * Preco_Estoque[Fruta]
                        if quantidade > 1:
                            print(f'O valor total da compra é R${Valor:.2f}')
                        else:
                            print(f'O valor total da compra é R${Valor:.2f}')
                        Valor_total += Valor
                        Quantidade_Estoque[Fruta] -= quantidade

                    else:
                        print(
                            f'Lamentamos, mas não temos essa quantidade de {Fruta}s no estoque'
                        )

            else:
                print(
                    'Lamentamos o ocorrido, mas não temos essa fruta em nosso estoque'
                )

        if quantidade2 > 0:
            Confirmacao = input(
                'Você deseja continuar para a compra ? (S) ou (N):'
            ).lower()

            if Confirmacao == "s":
                fruta_selecionada_str = ",".join(fruta_selecionada)
                plural = 's' if len(fruta_selecionada) > 1 else ''
                print(
                    f'Você comprou {fruta_selecionada_str}{plural}, e o valor total foi de R${Valor_total:.2f}'
                )

            elif Confirmacao == "n":
                print("Compra cancelada, obrigado pela preferência")
            
            else:
                print("Opção inválida")
except ValueError:
    print("Por favor digite apenas números")
    
