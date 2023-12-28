
#Define a qualidade do item, nesse caso é a produção total (peças boas + refugos) e por fim fazendo a divisão
def qualidade(x, y):
    qualidade_total = ((x - y) / x)
    print("Sua qualidade foi de:", round(qualidade_total * 100, 2), "%")
    return qualidade_total

#Coloque as horas da produção real nesse caso considera apenas 1 turno (8 horas)
def disponibilidade():
    tempo_total_planejado = 8
    tempo_producao_real = float(input("Tempo de produção: "))
    disponibilidade_total = tempo_producao_real / tempo_total_planejado
    print("Sua disponibilidade foi de:", disponibilidade_total * 100, "%")
    return disponibilidade_total


#Adicione o ciclo em que é trabalhado a peça, ideal é que seja automatico e seja já tenha um pre-set
def desempenho():
    ciclo_teorico = 100
    try:
     while True:
        ciclo_produzido = int(input("Ciclo produzido? "))
        if ciclo_produzido == 0:
            break
        else:
            desempenho_total = float(ciclo_produzido / ciclo_teorico)
            print("Seu desempenho foi de:", desempenho_total * 100, "%")
            return desempenho_total
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

def main():

#Inicia o programa a partir das escolhas do usuário (S / N)
    while True:
        producao = input("Teve produção? (S/N) ").upper()
        if producao == "S":
            maquina = input("Digite a IJ: ")
            break
        elif producao == "N":
            quit()

#Define o quantidade de peças e refugos produzidos após o usuario dar inicio ao programa
#Não será aceito no programa se o valor do refugo for maior do que a produção total
    while True:
        try:
            prod = int(input("Prod: "))
            scrap = int(input("Scrap: "))
            if prod == 0 or prod < scrap:
                continue
            else:
                break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")

    qualidade_total = qualidade(prod, scrap)
    disponibilidade_total = disponibilidade()
    desempenho_total = desempenho()
    oee_resultado = (qualidade_total * disponibilidade_total * desempenho_total) * 100
    print("IJ:",maquina)
    print("Eficiência Global do Equipamento (OEE):", round(oee_resultado, 2), "%")

if __name__ == "__main__":
    main()
