class AcertosErrosBrancos:
    def __init__(self) -> None:
        self.acerto = self.erro = self.branco = 0

    def atribuir_valor(self, i:int) -> None:
        if (i == 1):
            self.acerto += 1
        if (i == 2):
            self.erro += 1
        if (i == 3):
            self.branco += 1

    def validar_i(self, i: str) -> int:
        if (i.isnumeric() and int(i) in [1, 2, 3, 0]):
            return int(i)
        print('\nAdicione um número válido\n')
        return -1

    def perguntar(self):
        i = 1
        while int(i) != 0:
            msg = '1 - para adicionar valor a acertos, 2 - para erros, 3 - para brancos, 0 - para sair: '
            i = self.validar_i(input(msg))
            if (i != -1):
                self.atribuir_valor(i)
    
    def __str__(self) -> str:
        total_acerto = self.acerto - self.erro
        denominador = self.acerto + self.erro + self.branco
        percent = total_acerto*100/denominador
        return f'\nAcertos: {self.acerto}\tErros: {self.erro}\tBrancos: {self.branco}\nTotal: {total_acerto}\t%: {percent}'


if __name__ == '__main__':
    x = AcertosErrosBrancos()
    x.perguntar()
    print(x)
