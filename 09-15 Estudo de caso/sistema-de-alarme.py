#   sistema de alarme


fumaca = input("Há fumaça? (s/n): ").lower()
botao_emergenca = input("Botão de emergência acionado? (s/n): ").lower()
chave_seguranca = input("Chave de segurança ativada? (s/n): ").lower()
movimento = input("Há movimento suspeito? (s/n): ").lower()

alarme = False



if movimento == 's' and chave_seguranca == 's' and fumaca == 'n' and botao_emergenca == 'n':
    alarme = False
    print("Tudo normal.")

elif fumaca == 's' or botao_emergenca == 's' and chave_seguranca == 's' or movimento == 's':
    alarme = True
    print("Alarme disparado!")

else:
    alarme = False
    print("Tudo normal.")


print("Alarme:", alarme)
