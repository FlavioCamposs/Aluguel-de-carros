from time import sleep

print('\033[1;30;107mSEJA MUITO BEM VINDO AO ALUGUEL DE CARROS DO FLÁVIO!!\033[m')
print('-=' * 35)

print('Qual dos serviços abaixo você deseja fazer?')
print('Digite:\n\033[92m1° - Para alugar um novo carro\033[m\n\033[94m2° - Para verificar taxa de aluguel do carro que já foi alugado\033[m')
print('-=' * 35)
servico = int(input('Qual serviço você escolhe? '))

if (servico == 1):
    print('Certo, por favor, espere alguns segundos...')
    sleep(5)
    carrosDisponiveis = ['Kwid', 'Honda Civic', 'HB20', 'Honda City'] #array criado apenas para mostrar os carros
    print('\033[1;92mQue ótimo!\033[m Obrigado pela preferência :)\nAqui está os carros disponiveis:\n\033[;97;47m{}\033[m'.format(', '.join(carrosDisponiveis)))
    print('-=' * 35)
    carros = ['kwid', 'honda civic', 'hb20', 'honda city']
    carroEscolhido = str(input('Qual carro você quer alugar: ')).lower().strip()


    if carroEscolhido == carros[0]:
        print('O valor do Kwid é de \033[1mR$60\033[m por dia, e \033[1mR$0.20\033[m por km rodado!!')
        print('-=' * 35)
        dias = int(input('Por quantos dias você deseja alugar? '))
        valorPorDia = dias * 60 #valor do carro
        print(f'O valor do carro por \033[4m{dias}\033[m dias ficará por \033[1mR${valorPorDia}\033[m, somado com o valor da quilometragem rodada durante esse tempo!')
        print('=' * 35)
        print('Digite:\n\033[92m1° - Para prosseguir\033[m\n\033[91m2° - Para cancelar\033[m')
        escolha = int(input('Digite: ')) #espaço para digitar a resposta do úsuario
        if escolha == 1:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print('\033[1;92mParabéns\033[m, Carro Alugado :), vá até a nossa loja fisica mais próxima para efetuar o pagamento, pegar a documentação e o seu carro!\n\033[4mEsperamos por você!\033[m')
        elif escolha == 2:
            print('\033[91mServiço Cancelado! :(\033[m')
        else:
            print('\033[1;91mNumero Inválido!\033[m')


    elif carroEscolhido == carros[1]:
        print('O valor do Honda Civic é de \033[1mR$120\033[m por dia, e \033[1mR$1.00\033[m por km rodado!!')
        print('-=' * 35)
        dias = int(input('Por quantos dias você deseja alugar? '))
        valorPorDia = dias * 120
        print(f'O valor do carro por \033[4m{dias}\033[m dias ficará por \033[1mR${valorPorDia}\033[m, somado com o valor da quilometragem rodada durante esse tempo!')
        print('-=' * 35)
        print('Digite:\n\033[92m1° - Para prosseguir\033[m\n\033[91m2° - Para cancelar\033[m')
        escolha = int(input('Digite: '))
        if escolha == 1:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print('\033[92mParabéns\033[m, Carro Alugado :), vá até a nossa loja fisica mais próxima para efetuar o pagamento, pegar a documentação e o seu carro!\nEsperamos por você!')
        elif escolha == 2:
            print('\033[91mServiço Cancelado! :(\033[m')
        else:
            print('\033[1;91mNumero Inválido\033[m')


    elif carroEscolhido == carros[2]:
        print('O valor do HB20 é de \033[1mR$90\033[m por dia, e \033[1mR$0.50\033[m por km rodado!!')
        print('-=' * 35)
        dias = int(input('Por quantos dias você deseja alugar? '))
        valorPorDia = dias * 90
        print(f'O valor do carro por \033[4m{dias}\033[m dias ficará por \033[1mR${valorPorDia}\033[m, somado com o valor da quilometragem rodada durante esse tempo!')
        print('-=' * 35)
        print('Digite:\n\033[92m1° - Para prosseguir\033[m\n\033[91m2° - Para cancelar\033[m')
        escolha = int(input('Digite: '))
        if escolha == 1:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print('\033[92mParabéns\033[m, Carro Alugado :), vá até a nossa loja fisica mais próxima para efetuar o pagamento, pegar a documentação e o seu carro!\nEsperamos por você!')
        elif escolha == 2:
            print('\033[91mServiço Cancelado! :(\033[m')
        else:
            print('\033[1;91mNumero Inválido\033[m')


    elif carroEscolhido == carros[3]:
        print('O valor do Honda City é de \033[1mR$100\033[m por dia, e \033[1mR$0.75\033[m por km rodado!!')
        print('-=' * 35)
        dias = int(input('Por quantos dias você deseja alugar? '))
        valorPorDia = dias * 100
        print(f'O valor do carro por \033[4m{dias}\033[m dias ficará por \033[1mR${valorPorDia}\033[m, somado com o valor da quilometragem rodada durante esse tempo!')
        print('-=' * 35)
        print('Digite:\n\033[92m1° - Para prosseguir\033[m\n\033[91m2° - Para cancelar\033[m')
        escolha = int(input('Digite: '))
        if escolha == 1:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print('\033[92mParabéns\033[m, Carro Alugado :), vá até a nossa loja fisica mais próxima para efetuar o pagamento, pegar a documentação e o seu carro!\nEsperamos por você!')
        elif escolha == 2:
            print('\033[91mServiço Cancelado! :(\033[m')
        else:
            print('\033[1;91mNumero inválido!\033[m')


    else:
        print('-=' * 35)
        print('\033[1;91mModelo do carro indisponivel!\033[m')
        print('\033[4mOu, verifique se o nome do carro está escrito corretamente!\033[m')


elif (servico == 2):
    print('Certo, por favor, espere alguns segundos...')
    sleep(5)
    carros = ['kwid', 'honda civic', 'hb20', 'honda city']

    escolha1 = input('Qual foi o carro alugado? ').lower().strip()
    #Valores fixos dos carros e da quilometragem/hora de cada um
    valoresDosCarros = [60, 120, 90, 100]
    valorKmPorHora = [0.20, 1.0, 0.50, 0.75]


    if escolha1 == carros[0]:
        dias = int(input('Por quantos dias o carro foi alugado? '))
        kmRodado = float(input('Quantos km foram rodados? '))
        valorPorDia = valoresDosCarros[0] * dias
        valorPorKm = valorKmPorHora[0] * kmRodado
        taxaFinal = valorPorDia + valorPorKm
        print('-=' * 35)
        if dias > 15: #se o carro for alugado por mais de 15 dias
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            desconto = taxaFinal - (taxaFinal * 15 / 100) #para tirar 15% do valor total da taxa final
            print('Você alugou o carro por mais de \033[4m15 dias\033[m, \033[92mparabéns!!\033[m Você ganhou \033[1m15%\033[m de desconto no valor total :)\nSua taxa final de \033[91mR${}\033[m, ficou por \033[1;92mR${:.2f}\033[m'.format(taxaFinal, desconto))
        else:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print(f'A taxa do carro "Kwid" irá ficar por: \033[1mR${taxaFinal}\033[m')


    elif escolha1 == carros[1]:
        dias = int(input('Por quantos dias o carro foi alugado? '))
        kmRodado = float(input('Quantos km foram rodados? '))
        valorPorDia = valoresDosCarros[1] * dias
        valorPorKm = valorKmPorHora[1] * kmRodado
        taxaFinal = valorPorDia + valorPorKm
        print('-=' * 35)
        if dias > 15:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            desconto = taxaFinal - (taxaFinal * 15 / 100)
            print('Você alugou o carro por mais de \033[4m15 dias\033[m, \033[92mparabéns!!\033[m Você ganhou \033[1m15%\033[m de desconto no valor total :)\nSua taxa final de \033[91mR${}\033[m, ficou por \033[1;92mR${:.2f}\033[m'.format(taxaFinal, desconto))
        else:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print(f'A taxa do carro "Honda Civic" irá ficar por: \033[1mR${taxaFinal}\033[m')


    elif escolha1 == carros[2]:
        dias = int(input('Por quantos dias o carro foi alugado? '))
        kmRodado = float(input('Quantos km foram rodados? '))
        valorPorDia = valoresDosCarros[2] * dias
        valorPorKm = valorKmPorHora[2] * kmRodado
        taxaFinal = valorPorDia + valorPorKm
        print('-=' * 35)
        if dias > 15:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            desconto = taxaFinal - (taxaFinal * 15 / 100)
            print('Você alugou o carro por mais de \033[4m15 dias\033[m, \033[92mparabéns!!\033[m Você ganhou \033[1m15%\033[m de desconto no valor total :)\nSua taxa final de \033[91mR${}\033[m, ficou por \033[1;92mR${:.2f}\033[m'.format(taxaFinal, desconto))
        else:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print(f'A taxa do carro "HB20" irá ficar por: \033[1mR${taxaFinal}\033[m')

    elif escolha1 == carros[3]:
        dias = int(input('Por quantos dias o carro foi alugado? '))
        kmRodado = float(input('Quantos km foram rodados? '))
        valorPorDia = valoresDosCarros[3] * dias
        valorPorKm = valorKmPorHora[3] * kmRodado
        taxaFinal = valorPorDia + valorPorKm
        print('-=' * 35)
        if dias > 7:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            desconto = taxaFinal - (taxaFinal * 15 / 100)
            print('Você alugou o carro por mais de \033[4m15 dias\033[m, \033[92mparabéns!!\033[m Você ganhou \033[1m15%\033[m de desconto no valor total :)\nSua taxa final de \033[91mR${}\033[m, ficou por \033[1;92mR${:.2f}\033[m'.format(taxaFinal, desconto))
        else:
            print('Certo, por favor, espere alguns segundos...')
            sleep(10)
            print(f'A taxa do carro "Honda City" irá ficar por: \033[1mR${taxaFinal}\033[m')


    else:
        print('-=' * 35)
        print('\033[1;91mModelo do carro indisponivel!\033[m')
        print('\033[4mOu, verifique se o nome do carro está escrito corretamente!\033[m')

else:
    print('-=' * 35)
    print('\033[1;91mNumero inválido!\033[m')