#perguntar em que turno estuda
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# M-matutino para V-Vespertino ou N-Noturno



turno = input('Em qual turno você estuda?DIGITTE M-matutino para V-Vaspertino ou N-Noturno: ')

match turno:
    case "M":
            print ("Bom dia")
    case "V":
            print ('Boa tarde!')
    case"N":
            print ('Boa noite!')
    case _: print ("Opção inválida.")
