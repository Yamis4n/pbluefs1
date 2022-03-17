#INICIAR AS VARIAVEIS:
Tacucar = 0
Tarroz = 0
Tcafe = 0
Textrato_tomate = 0
Tmacarrao = 0
Tbolacha = 0
Toleo = 0
Tfarinha_de_trigo = 0
Tfeijao = 0
Tsal = 0
Toutros = 0

#fisica:
Facucar = 0
Farroz = 0
Fcafe = 0
Fextrato_tomate = 0
Fmacarrao = 0
Fbolacha = 0
Foleo = 0
Ffarinha_de_trigo = 0
Ffeijao = 0
Fsal = 0
Foutros = 0
#juridica:
Jacucar = 0
Jarroz = 0
Jcafe = 0
Jextrato_tomate = 0
Jmacarrao = 0
Jbolacha = 0
Joleo = 0
Jfarinha_de_trigo = 0
Jfeijao = 0
Jsal = 0
Joutros = 0

sair = False
while sair == False:
    '''menu com nova doação relatrio e encerrar o dia'''
    menu = int(input("0. NOVA DOAÇÃO\n1. RELATORIO\n2. FINALIZAR O DIA\n"))
    if menu == 2:
        '''relatorio'''
        sair = True
    elif menu == 1:
        '''relatorio'''
        cestas = 0
        
        Tacucar = Facucar + Jacucar
        Tarroz = Farroz + Jarroz
        Tcafe = Fcafe + Jcafe
        Textrato_tomate = Fextrato_tomate + Jextrato_tomate
        Tmacarrao = Fmacarrao + Jmacarrao
        Tbolacha = Fbolacha + Jbolacha
        Toleo = Foleo + Joleo
        Tfarinha_de_trigo = Ffarinha_de_trigo + Jfarinha_de_trigo
        Tfeijao = Ffeijao + Jfeijao
        Tsal = Fsal + Jsal
        Toutros = Foutros + Joutros

        print(f"{Tacucar} kgs de açucar\n{Tarroz} kgs de arroz\n{Tcafe} kgs de café\n{Textrato_tomate}\
             un de extrato de tomate\n{Tmacarrao} un macarrao\n{Tbolacha} pct de bolacha\n{Toleo} L de oleo\
                 \n{Tfarinha_de_trigo} kgs de farinha de trigo\n{Tfeijao} kgs de feijao\n{Tsal} kgs de sal")

        print('pessoas juridicas:\n', (Jacucar // 1)+(Jarroz // 4) + (Jcafe // 2) + \
            (Jextrato_tomate // 2) + (Jmacarrao // 3) + (Jbolacha // 1) + (Joleo // 1) + \
                (Jfarinha_de_trigo // 1) + (Jfeijao // 4) + (Jsal // 1) + (Joutros // 1))
        print('pessoas físicas:\n', (Facucar // 1)+(Farroz // 4) + (Fcafe // 2) + \
            (Fextrato_tomate // 2) + (Fmacarrao // 3) + (Fbolacha // 1) + (Foleo // 1) + \
                (Ffarinha_de_trigo // 1) + (Ffeijao // 4) + (Fsal // 1) + (Foutros // 1))

        while Tacucar >= 1 and Tarroz >= 4 and Tcafe >= 2 and Textrato_tomate >= 2 and \
            Tmacarrao >= 3 and Tbolacha >= 1 and Toleo >= 1 and Tfarinha_de_trigo >= 1 and \
                Tfeijao >= 4 and Tsal >= 1 and Toutros >= 1:
            cestas -= 1
            Tacucar -= 1
            Tarroz -= 4
            Tcafe -= 2
            Textrato_tomate -= 2
            Tmacarrao -= 3
            Tbolacha -= 1
            Toleo -= 1
            Tfarinha_de_trigo -= 1
            Tfeijao -= 4
            Tsal -= 1
            Toutros -= 1
        print("total de cestas:", cestas)

        if Toutros >= cestas:
            print(cestas, "cestas receberão um item extra")
        else:
            print((Toutros - cestas) * -1, "receberão um item extra")
        
        if Toutros <= cestas:
            print((Toutros - cestas) , "não receberão um item extra")
        else:
            print(" 0 cestas receberão um item extra")
        
        print(f"{Tacucar} kgs de açucar\n{Tarroz} kgs de arroz\n{Tcafe} kgs de café\n{Textrato_tomate}\
             un de extrato de tomate\n{Tmacarrao} un macarrao\n{Tbolacha} pct de bolacha\n{Toleo} L de oleo\
                 \n{Tfarinha_de_trigo} kgs de farinha de trigo\n{Tfeijao} kgs de feijao\n{Tsal} kgs de sal")
    elif menu == 0:
        input("nome do doador:\n")
        tipo_do_doador = int(input("0. PESSOA FÍSICA.\n1. PESSOA JURÍDICA.\n"))
        if tipo_do_doador == 0:
            tipo_do_item = int(input("0. Açucar\n1. arroz\n2. café\n3. extrato de tomate\
                \n4. macarrão\n5. bolacha\n6. oleo\n7. farinha de trigo\n8. feijão\n9. sal\n10. outros.\n"))
            if tipo_do_item == 0:
                Facucar += float(input("quantos quilos?\n"))
            elif tipo_do_item == 1:
                Farroz += float(input("quantos quilos?\n"))
            elif tipo_do_item == 2:
                Fcafe += float(input("quantos quilos?\n"))
            elif tipo_do_item == 3:
                Fextrato_tomate += float(input("quantas unidades?\n"))
            elif tipo_do_item == 4:
                Fmacarrao += float(input("quantas unidades?\n"))
            elif tipo_do_item == 5:
                Fbolacha += float(input("quantos pacotes?\n"))
            elif tipo_do_item == 6:
                Foleo += float(input("quantos litros?\n"))
            elif tipo_do_item == 7:
                Ffarinha_de_trigo += float(input("Quantos quilos?\n"))
            elif tipo_do_item == 8:
                Ffeijao += float(input("quantos quilos?\n"))
            elif tipo_do_item == 9:
                Fsal += float(input("quantos quilos?\n"))
            elif tipo_do_item == 10:
                Foutros += float(input("quantas unidades?\n"))
        elif tipo_do_doador == 1:
            tipo_do_item = int(input("0. Açucar\n1. arroz\n2. café\n3. extrato de tomate\
                \n4. macarrão\n5. bolacha\n6. oleo\n7. farinha de trigo\n8. feijão\n9. sal\n10. outros.\n"))
            if tipo_do_item == 0:
                Jacucar += float(input("quantos quilos?\n"))
            elif tipo_do_item == 1:
                Jarroz += float(input("quantos quilos?\n"))
            elif tipo_do_item == 2:
                Jcafe += float(input("quantos quilos?\n"))
            elif tipo_do_item == 3:
                Jextrato_tomate += float(input("quantas unidades?\n"))
            elif tipo_do_item == 4:
                Jmacarrao += float(input("quantas unidades?\n"))
            elif tipo_do_item == 5:
                Jbolacha += float(input("quantos pacotes?\n"))
            elif tipo_do_item == 6:
                Joleo += float(input("quantos litros?\n"))
            elif tipo_do_item == 7:
                Jfarinha_de_trigo += float(input("Quantos quilos?\n"))
            elif tipo_do_item == 8:
                Jfeijao += float(input("quantos quilos?\n"))
            elif tipo_do_item == 9:
                Jsal += float(input("quantos quilos?\n"))
            elif tipo_do_item == 10:
                Joutros += float(input("quantas unidades?\n"))
            
