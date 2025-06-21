import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Interativa")
        master.geometry("300x450")
        master.configure(bg="lightgray")

        self.historico = []
        self.entrada = tk.Entry(master, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
        self.entrada.pack(pady=10)

        self.criar_botoes()

    def criar_botoes(self):
        botoes = [
            ('7', self.adicionar), ('8', self.adicionar), ('9', self.adicionar), ('/', self.adicionar),
            ('4', self.adicionar), ('5', self.adicionar), ('6', self.adicionar), ('*', self.adicionar),
            ('1', self.adicionar), ('2', self.adicionar), ('3', self.adicionar), ('-', self.adicionar),
            ('0', self.adicionar), ('.', self.adicionar), ('+', self.adicionar), ('=', self.calcular),
            ('C', self.limpar), ('√', self.raiz_quadrada), ('^', self.adicionar)
        ]

        frame = tk.Frame(self.master, bg="lightgray")
        frame.pack()

        linha = 0
        coluna = 0

        for (texto, comando) in botoes:
            if texto == '=':
                btn = tk.Button(frame, text=texto, width=6, height=2, font=("Arial", 12), command=self.calcular)
            elif texto == 'C':
                btn = tk.Button(frame, text=texto, width=6, height=2, font=("Arial", 12), command=self.limpar)
            elif texto == '√':
                btn = tk.Button(frame, text=texto, width=6, height=2, font=("Arial", 12), command=self.raiz_quadrada)
            else:
                btn = tk.Button(frame, text=texto, width=6, height=2, font=("Arial", 12), command=lambda t=texto: comando(t))
            btn.grid(row=linha, column=coluna, padx=5, pady=5)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        # Botão separado para o Histórico (sem argumento)
        btn_hist = tk.Button(self.master, text="Histórico", width=20, height=2, font=("Arial", 12),
                             command=self.mostrar_historico)
        btn_hist.pack(pady=5)
        # Botão para limpar histórico
        btn_limpar_hist = tk.Button(self.master, text="Limpar Histórico", width=20, height=2, font=("Arial", 12),
                                    command=self.limpar_historico)
        btn_limpar_hist.pack(pady=5)

    def adicionar(self, valor):
        self.entrada.insert(tk.END, valor)

    def limpar(self, _=None):
        self.entrada.delete(0, tk.END)

    def calcular(self, _=None):
        expressao = self.entrada.get()
        try:
            # Substitui ^ por ** para potência
            expressao = expressao.replace('^', '**')
            resultado = eval(expressao)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
            self.historico.append(f"{expressao} = {resultado}")
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida")

    def raiz_quadrada(self, _=None):
        try:
            valor = self.entrada.get()
            if not valor:
                raise ValueError
            numero = float(valor)
            if numero < 0:
                raise ValueError("Número negativo")
            resultado = math.sqrt(numero)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
            self.historico.append(f"√{numero} = {resultado}")
        except Exception:
            messagebox.showerror("Erro", "Digite um número válido para a raiz quadrada")

    def mostrar_historico(self):
        if self.historico:
            historico_texto = "\n".join(self.historico[-10:])
            messagebox.showinfo("Histórico de Operações", historico_texto)
        else:
            messagebox.showinfo("Histórico de Operações", "Nenhuma operação realizada ainda.")

    def limpar_historico(self):
        self.historico.clear()
        messagebox.showinfo("Histórico", "Histórico limpo com sucesso!")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
