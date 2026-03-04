import tkinter as tk


class CalculadoraApp:
    COR_FUNDO = "#3b3b3b"
    COR_TEXTO = "#feffff"
    COR_TELA = "#38576b"
    COR_OPERADOR = "#FFAB40"

    BOTOES = [
        ("C", 11, 0, 0, COR_TEXTO),
        ("%", 5, 118, 0, COR_OPERADOR),
        ("/", 5, 177, 0, COR_OPERADOR),
        ("7", 5, 0, 52, COR_TEXTO),
        ("8", 5, 59, 52, COR_TEXTO),
        ("9", 5, 118, 52, COR_TEXTO),
        ("*", 5, 177, 52, COR_OPERADOR),
        ("4", 5, 0, 104, COR_TEXTO),
        ("5", 5, 59, 104, COR_TEXTO),
        ("6", 5, 118, 104, COR_TEXTO),
        ("-", 5, 177, 104, COR_OPERADOR),
        ("1", 5, 0, 156, COR_TEXTO),
        ("2", 5, 59, 156, COR_TEXTO),
        ("3", 5, 118, 156, COR_TEXTO),
        ("+", 5, 177, 156, COR_OPERADOR),
        ("0", 11, 0, 208, COR_TEXTO),
        (".", 5, 118, 208, COR_TEXTO),
        ("=", 5, 177, 208, COR_OPERADOR),
    ]

    def __init__(self) -> None:
        self.janela = tk.Tk()
        self.janela.title("CALCULADORA")
        self.janela.geometry("235x318")
        self.janela.config(bg=self.COR_FUNDO)

        self.valor_texto = tk.StringVar()

        self._criar_layout()
        self._criar_botoes()

    def _criar_layout(self) -> None:
        frame_tela = tk.Frame(self.janela, width=235, height=50, bg=self.COR_TELA)
        frame_tela.grid(row=0, column=0)

        self.frame_corpo = tk.Frame(self.janela, width=235, height=268, bg=self.COR_FUNDO)
        self.frame_corpo.grid(row=1, column=0)

        app_label = tk.Label(
            frame_tela,
            textvariable=self.valor_texto,
            width=16,
            height=2,
            padx=7,
            relief=tk.FLAT,
            anchor="e",
            justify=tk.RIGHT,
            font=("Ivy 18"),
            bg=self.COR_TELA,
            fg=self.COR_TEXTO,
        )
        app_label.place(x=0, y=0)

    def _criar_botoes(self) -> None:
        for texto, largura, x, y, cor in self.BOTOES:
            botao = tk.Button(
                self.frame_corpo,
                text=texto,
                width=largura,
                height=2,
                bg=cor,
                font=("Ivy 13 bold"),
                relief=tk.RAISED,
                overrelief=tk.RIDGE,
                command=lambda valor=texto: self.atualizar_display(valor),
            )
            botao.place(x=x, y=y)

    def atualizar_display(self, valor: str) -> None:
        atual = self.valor_texto.get()

        if valor == "=":
            self._calcular_resultado(atual)
            return

        if valor == "C":
            self.valor_texto.set("")
            return

        if atual == "Erro":
            self.valor_texto.set(valor)
            return

        self.valor_texto.set(atual + valor)

    def _calcular_resultado(self, expressao: str) -> None:
        try:
            resultado = eval(expressao, {"__builtins__": {}}, {})
            self.valor_texto.set(str(resultado))
        except Exception:
            self.valor_texto.set("Erro")

    def executar(self) -> None:
        self.janela.mainloop()


def main() -> None:
    app = CalculadoraApp()
    app.executar()


if __name__ == "__main__":
    main()



