leituras = []

    #Função para solicitar ao usuario cinco informações.
def solicitar_velocidade():
        leituras.clear
        for i in range(1,6):
            while True:   
                try:
                    leituras.append(int(input(f'Insira a {i}º velocidade do motor: ')))
                    break
                except ValueError:
                    print('Insira apenas números inteiros.')

    #função para calcular a média.
def calcular_media():
        media = sum(leituras) / len(leituras)
        return media

    #função para exibir o maior valor na lista.
def maior_valor():
        maior = leituras[0]
        for numero in leituras:
            if numero > maior:
                maior = numero
        return maior      

    #Função para exibir o menor valor na lista.
def menor_valor():
        menor = leituras[0]
        for numero in leituras:
            if numero <= menor:
                menor = numero
        return menor
            
    #Função para calcular toda a lista.
def calcular_total():
        total = sum(leituras)
        return total

    #Função que exibe o relatorio.
def relatorio():
        print('-----RELATÓRIO-----')
        print(f'A lista com todos os valores é a seguinte\n{leituras}')
        print(f'A média dos valores inseridos é a seguinte.\nMedia: {media}')
        print(f'A maior leitura lida foi: {maior}')
        print(f'A menor leitura lida foi:{menor}')
        print(f'A soma de todas as leituras foi:{total}')

    #Função para o usuario escolher se quer continuar.
def continuar_programa():
    while True:
        try:
            continuar = str(input('Você deseja continuar o progarama?(S/N)'))
        except:
                print('Insira apenas(S/N)')
        if continuar == 'S':
                print('Recomeçando o programa.')
                return continuar
        elif continuar == 'N':
            print('Obrigado por usar o programa.\nENCERRANDO...')
            continuar = 'N'
            return continuar

        else:
            print('Insir apenas S ou N')


continuar = 'S'

while continuar == 'S':

    solicitar_velocidade()
    media = calcular_media()
    maior = maior_valor()
    menor = menor_valor()
    total = calcular_total()
    relatorio()
    continuar = continuar_programa()






















   


            
