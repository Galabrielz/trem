class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_totais = 0
        self.movimentos_consecutivos = 0
        self.direcao_anterior = None

    def mover(self, comandos):
        for comando in comandos:
            if self.movimentos_totais >= 50:
                break
            
            if comando not in ["ESQUERDA", "DIREITA"]:
                raise ValueError(f"Comando inválido: {comando}")
            
            if comando == self.direcao_anterior:
                self.movimentos_consecutivos += 1
            else:
                self.movimentos_consecutivos = 1
                self.direcao_anterior = comando

            if self.movimentos_consecutivos > 20:
                raise ValueError("Limite de 20 movimentos consecutivos na mesma direção excedido.")
            
            if comando == "ESQUERDA":
                self.posicao -= 1
            elif comando == "DIREITA":
                self.posicao += 1
            
            self.movimentos_totais += 1

        return self.posicao


trem = TremAutonomo()
posicao_final = trem.mover(["DIREITA", "DIREITA"])
print("Posição final:", posicao_final)
