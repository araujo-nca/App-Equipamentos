import pandas as pd


def Planilha(equipamento, tabela):

    try:
        # Variável que armazena a planilha em formato Pandas    
        sheet = pd.read_excel(f"Tabelas/{equipamento}.xlsx", sheet_name = tabela)

    except:
        # Sai do programa caso o nome da planilha esteja errado
        exit(f"Não existe planilha com o nome {tabela}")

    return sheet


def main():

    tabela = Planilha("Tabelas", "4.23.uni")
    secao = tabela.set_index("Seção condutor")

    # text = secao.loc[["1.5"]["Duto único"]]


    print(secao.loc[[4]])
    # print(text)


if __name__ == "__main__":
    main()