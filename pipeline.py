import tkinter as tk
import random

class DiagramaPipeline:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Diagrama de Pipeline")

        self.canvas = tk.Canvas(raiz, width=700, height=400)
        self.canvas.pack()

        # Diferentes configurações de instruções que simulam interrupções
        self.instrucoes1 = [
            ["FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", "", ""],
            ["", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", ""],
            ["", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", ""],
            ["", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", ""],
            ["", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", ""],
            ["", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", ""],
            ["", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", ""],
            ["", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", ""],
            ["", "", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO"]
        ]
        
        self.instrucoes2 = [
            ["FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", "", ""],
            ["", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", ""],
            ["", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", ""],
            ["", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", ""],
            ["", "", "", "", "FI", "DI", "CO", "FO", "", "", "", "", "", ""],
            ["", "", "", "", "", "FI", "DI", "CO", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "FI", "DI", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "FI", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO"]
        ]
        
        self.instrucoes3 = [
            ["FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", "", ""],
            ["", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", ""],
            ["", "", "FI", "DI", "CO", "FO", "", "", "", "", "", "", "", ""],
            ["", "", "", "FI", "DI", "CO", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "FI", "DI", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "FI", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", "", ""],
            ["", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", ""],
            ["", "", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO"]
        ]

        self.instrucoes4 = [
            ["FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", "", ""],
            ["", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", "", ""],
            ["", "", "FI", "DI", "CO", "FO", "EI", "WO", "", "", "", "", "", ""],
            ["", "", "", "FI", "DI", "CO", "FO", "", "", "", "", "", "", ""],
            ["", "", "", "", "FI", "DI", "CO", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "FI", "DI", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "FI", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO", ""],
            ["", "", "", "", "", "", "", "", "FI", "DI", "CO", "FO", "EI", "WO"]
        ]
        # Inicializando com o primeiro conjunto de instruções
        self.instrucoes = self.instrucoes1
        self.largura_celula = 50
        self.altura_celula = 30
        self.passo_atual = 0
        
        # Botão para iniciar a execução
        self.botao_iniciar = tk.Button(raiz, text="Iniciar Pipeline", command=self.iniciar_pipeline)
        self.botao_iniciar.pack(pady=10)
        
        # Botão para iniciar a execução com interrupção aleatória
        self.botao_iniciar_interrupcao = tk.Button(raiz, text="Pipeline com Interrupção", command=self.iniciar_pipeline_com_interrupcao_aleatoria)
        self.botao_iniciar_interrupcao.pack(pady=10)
        
        # Botão para apagar a pipeline
        self.botao_apagar = tk.Button(raiz, text="Apagar Pipeline", command=self.apagar_pipeline)
        self.botao_apagar.pack(pady=10)

        self.desenhar_grelha_vazia()

    def desenhar_grelha_vazia(self):
        
        for i in range(len(self.instrucoes)):
            for j in range(len(self.instrucoes[0])):
                x1 = j * self.largura_celula
                y1 = i * self.altura_celula
                x2 = x1 + self.largura_celula
                y2 = y1 + self.altura_celula
                if i == 0:
                    self.canvas.create_line(x1, y1, x2, y1, fill="black", width=2)  
                if i == len(self.instrucoes) - 1:
                    self.canvas.create_line(x1, y2, x2, y2, fill="black", width=2)  
                if j == 0:
                    self.canvas.create_line(x1, y1, x1, y2, fill="black", width=2)  
                if j == len(self.instrucoes[0]) - 1:
                    self.canvas.create_line(x2, y1, x2, y2, fill="black", width=2)  
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

    def cancelar_pipeline(self):
        # Cancelar qualquer execução anterior
        if hasattr(self, 'after_id'):
            self.raiz.after_cancel(self.after_id)

    def iniciar_pipeline(self):
        self.cancelar_pipeline()
        self.passo_atual = 0
        self.instrucoes = self.instrucoes1  
        self.atualizar_pipeline()
        
    def iniciar_pipeline_com_interrupcao_aleatoria(self):
        self.cancelar_pipeline()
        self.passo_atual = 0
        # Escolher aleatoriamente um conjunto de instruções com interrupção
        self.instrucoes = random.choice([self.instrucoes2, self.instrucoes3, self.instrucoes4])
        self.atualizar_pipeline()
        
    def atualizar_pipeline(self):
        if self.passo_atual < len(self.instrucoes[0]):
            for i, linha in enumerate(self.instrucoes):
                instrucao = linha[self.passo_atual]
                if instrucao:
                    x1 = self.passo_atual * self.largura_celula
                    y1 = i * self.altura_celula
                    x2 = x1 + self.largura_celula
                    y2 = y1 + self.altura_celula
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue", width=2)
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=instrucao, font=("Arial", 14))
            
            self.passo_atual += 1
            self.after_id = self.raiz.after(500, self.atualizar_pipeline)

    def apagar_pipeline(self):
        self.cancelar_pipeline()
        self.canvas.delete("all")
        self.desenhar_grelha_vazia()

if __name__ == "__main__":
    raiz = tk.Tk()
    app = DiagramaPipeline(raiz)
    raiz.mainloop()
