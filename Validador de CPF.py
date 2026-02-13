import time
import platform
import os

def limpar_console():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')

    else:
        os.system('clear') 



def novamente():
    print('-=' * 20)
    print('Deseja Usar Novamente?')
    print('[1] Sim   [2] Não')
    resposta_novamente = input('Resposta: ')
    limpar_console()

    if resposta_novamente == '1':
        print('-=' * 20)
        print('Ok! Vamos Voltar Para o Menu!')
        print('-=' * 20)
        time.sleep(1.5)
        limpar_console()
        return menu()

    if resposta_novamente == '2':
        print('-=' * 20)
        print('Obrigada Por Usar Nosso Validador de CPF!')
        print('-=' * 20)
        time.sleep(1.5)
        limpar_console()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def menu():
    print('-=-=-=-=-=- Validador de CPF -=-=-=-=-=-')
    print('ꜱᴏᴍᴇɴᴛᴇ ɴᴜᴍᴇʀᴏꜱ!')
    cpf = input('Digite Seu CPF: ')
    print('-=' * 20)
    time.sleep(1)
    limpar_console()

    def digitos_cpf():
        #Conferir se o CPF Digitado Tem Somente Números e se Se Possui Números Iguais
        if not cpf.isdigit():
            print('-=' * 20)
            print('-> Digite Somente Números!')
            print('-=' * 20)
            time.sleep(1)
            limpar_console()
            return menu()
        
        if len(cpf) != 11 or len(set(cpf)) == 1:
            print('-=' * 20)
            print('-> ERRO! Números Inválidos')
            print('-=' * 20)
            time.sleep(1)
            limpar_console()
            return menu()
        
        return True

    def confirmação_cpf():
        # Confirmar Com o Usuário se o CPF Digitado Está Correto
        print('-=' * 20)
        print('Confirmação de CPF')
        print('-=' * 20)
        print(f'-> {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
        print('Está Correto?')
        print('[1] Sim   [2] Não')
        resposta = input('Resposta: ')

        if resposta == '1':
            print('-=' * 20)
            print('Ok! Vamos Prosseguir!')
            print('-=' * 20)
            time.sleep(1.5)
            limpar_console()

        elif resposta == '2':
            print('-=' * 20)
            print('Ok! Vamos Retornar Para o Menu!')
            print('-=' * 20)
            time.sleep(1.5)
            limpar_console()
            return menu()
        
        else:
            print('-=' * 20)
            print('Digite Somente as Opções Acima!')
            print('-=' * 20)
            time.sleep(1.5)
            limpar_console()
            return confirmação_cpf()
        
    def validação_cpf():
        #Cálculo do Primeiro Dígito
        soma1 = 0
        contador = 10
        for i in range(9):
            soma1 += int(cpf[i]) * (contador)
            contador -= 1

        multiplicado1 = soma1 * 10
        resto1 = multiplicado1 % 11
        digito1 = resto1

        #Cálculo do Segundo Dígito
        soma2 = 0
        contador = 11
        for i in range(10):
            soma2 += int(cpf[i]) * (contador)
            contador -= 1

        multiplicado2 = soma2 * 10
        resto2 = multiplicado2 % 11
        digito2 = resto2

        if digito1 > 9:
            digito1 = 0

        elif digito2 > 9:
            digito2 = 0


        print('-=' * 20)
        print('CPF VÁLIDO!')
        print(f'O Final do Seu CPF é: {digito1} {digito2}')
        print('-=' * 20)
        time.sleep(2)
        limpar_console()
        novamente()


    digitos_cpf()
    confirmação_cpf()
    validação_cpf()

if __name__ == '__main__':
    menu()