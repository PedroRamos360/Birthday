from datetime import date

def verificarAniversario(nome, MesNiver, DiaNiver):
    dataAtual = date.today()
    if dataAtual.month == MesNiver and dataAtual.day == DiaNiver:
        print('Hoje é o Aniversário de {}!'.format(nome))
        input('')

    elif dataAtual.month == MesNiver and (dataAtual.day + 1) == DiaNiver:
        print('Amanhã será o Aniversário de {}!'.format(nome))
        input('')

    elif dataAtual.month == MesNiver and (dataAtual.day + 2) == DiaNiver:
        print('O Aniversário de {} será em 2 dias!'.format(nome))
        input('')

    elif dataAtual.month == MesNiver and (dataAtual.day + 3) == DiaNiver:
        print('O Aniversário de {} será em 3 dias!'.format(nome))
        input('')





