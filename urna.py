print ("Atividade Urna Eletronica")

Pass = 2825
php = 10
css= 20
html= 30
Branco = 0
Vt = 0
Nulo = 0
Vtphp = 0
Vtcss = 0
Vthtml = 0
VtBranco = 0

S = int (input ("Digite sua senha para iniciar a sessão: "))

while S != Pass:
    S = int (input ("Senha errada!, por favor digite sua senha novamente: "))
while(1):
    print("Para votar no candidato php, digite", php, "\nPara votar no candidato css, digite", css, "\nPara votar no candidato html, digite", html, "\nPara votar em BRANCO, digite",Branco,"\n")
    Vt = int (input ("Vote no seu candidato: "))

    if Vt == php:
        print ("Você deseja votar no canditado php?")
    elif Vt == css:
        print ("Você deseja votar no canditado css?")
    elif Vt == html:
        print ("Você deseja votar no canditado html?")
    elif Vt == Branco:
        print ("Você deseja votar em Branco?")
    else:
        print ("Você deseja votar Nulo?")

    Cv = int (input ("1: Confirmar \n0: Corrigir\n"))

    if Cv != 1:
        print("\nCorrija seu voto!\n")
    else:
        S = int (input ("Digite sua senha para confirmar: "))
        while S != Pass:
            S = int (input ("Senha errada! Digite sua senha novamente: "))
        if Vt == 10:
            Vtphp+=1
        elif Vt == 20:
            Vtcss+=1
        elif Vt == 30:
            Vthtml+=1
        elif Vt == 0:
            VtBranco+=1
        else:
            Nulo+=1
        print("Voto computado com sucesso!\n")

        Vn = int (input ("Deseja votar novamente?\n1: Para votar novamente \n0: Para encerrar\n"))
        
        if Vn != 1:
            S = int (input ("Digite sua senha para encerrar a sessão de votos: "))
            while S != Pass:
                S = int (input ("Senha errada! Digite sua senha novamente: "))
            VtV = Vtphp + Vtcss + Vthtml
            Pvphp = Vtphp / VtV * 100
            Pvcss = Vtcss / VtV * 100
            Pvhtml = Vthtml / VtV * 100

            print("O candidato php teve",Pvphp,"%")
            print("O candidato css teve",Pvcss,"%")
            print("O candidato html teve",Pvhtml,"%")

            if Pvphp > 50:
                print("O canditato php foi eleito!",)
            elif Pvcss > 50:
                print("O canditato css foi eleito!")
            elif Pvhtml > 50:
                print("O canditato html foi eleito!")
            else:
                print ("A eleição irá para o segundo turno!")
            break
