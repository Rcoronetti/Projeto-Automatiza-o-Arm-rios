
import time

vet=['livre','livre','livre','livre','livre','livre','livre','livre','livre','livre']
opcao=1
while opcao !=0:
    print()
    print ('MENU')
    print('1 - Situação dos armários\n2 - Armários livres\n3 - Utilizar Armário\n4 - Remover armário\n5 - Resumo dos armários\n0 - Sair')
    opcao = int(input('Informe a opção desejada: '))
    print()
   

    if opcao == 0:
        print('\033[1;30;47mPrograma sendo finalizado...\033[m')
        time.sleep(3)
        print('\033[1;30;47maguarde...\033[m')
        time.sleep(1)
        print('\033[1;30;47mObrigado por utilizar nossos serviços, volte sempre!!\033[m')

    if opcao == 1:
        time.sleep(1)
        for i in range(10):
            if vet[i] == 'livre':
                print(f'\033[0;32;40mArmário livre: {i}\033[m')
            if vet[i]=='ocupado':
                print(f'\033[7;30;41mArmário ocupado: {i}\033[m',end=' ')         
                time.sleep(1)
                print()

    if opcao == 2: 
        time.sleep(1)
        for i in range(10):
            if vet[i] == 'livre':
                print(f'\033[0;32;40mArmário livre: {i}\033[m', end=' ')
                print()                
                

    if opcao == 3:   
        time.sleep(1)
        armario=(int(input(f'Informe o armário que deseja utilizar:  ')))
        print(f'Você escolheu o armário Nº: {armario}')
        print('Aguarde um instante para concluirmos a reserva...' )
        time.sleep(3)        
        if vet[armario] == 'ocupado':
            print('\033[7;30;41mARMÁRIO SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            print()   
            time.sleep(1)
        else:
            print('Reserva efetuada.Obrigado!')
            time.sleep(1)
            vet[armario]='ocupado'
            time.sleep(1)
        print()

    if opcao == 4:        
        armario=(int(input(f'Informe o armário que deseja liberar:  ')))        
        if vet[armario] == 'livre':
            print('\033[7;30;41mARMÁRIO NÃO ESTÁ SENDO UTILIZADO! POR FAVOR REPITA OPERAÇÃO.\033[m')
            time.sleep(1)
            print()      
        else:
            print(f'Você liberou o armário Nº: {armario}')
            print('Aguarde um instante para concluirmos a liberação...' )
            time.sleep(2)
            print('Seu armário está aberto e disponível para uso novamente.Obrigado!')
            time.sleep(1)
            vet[armario]='livre'
            time.sleep(1)

    if opcao ==5:
        livres = vet.count('livre')
        ocupados = vet.count('ocupado')
        time.sleep(1)
        print(f'\033[7;30;41mArmários Ocupados : {ocupados}\033[m') 
        print(f'\033[0;32;40mArmários Livres : {livres}\033[m')  
        time.sleep(1)
        print()      

    if opcao < 0 or opcao >5:
        time.sleep(1)
        print('\033[1;31;40mPor favor digite um cód válido!\033[m')  
        time.sleep(1)
        print()  
        





    


