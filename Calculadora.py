from tkinter import *


# Definindo cores
cor1 = "#3b3b3b"  # cinza
cor2 = "#feffff"  # branco
cor3 = "#38576b"  # azul escuro
cor4 = "#ECEFF1"  # azul
cor5 = "#FFAB40"  # laranja




# Função para atualizar o display
def atualizar_display(valor):
    atual = valor_texto.get()


    # Tratamento para diferentes tipos de valores
    if valor == "=":
        try:
            # Cálculo do resultado usando eval
            resultado = str(eval(atual))
            valor_texto.set(resultado)
        except Exception:
            valor_texto.set("Erro")
    elif valor == "C":
        valor_texto.set("")
    else:
        # Verifica se o último valor foi um erro
        if atual == "Erro":
            valor_texto.set(valor)
        else:
            valor_texto.set(atual + valor)




# Configuração da janela principal
janela = Tk()
janela.title("CALCULADORA")
janela.geometry("235x318")
janela.config(bg=cor1)


# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)


frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)


# Variável para display
valor_texto = StringVar()


# Criando Label para mostrar o valor
app_label = Label(
    frame_tela,
    textvariable=valor_texto,
    width=16,
    height=2,
    padx=7,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=("Ivy 18"),
    bg=cor3,
    fg=cor2,
)
app_label.place(x=0, y=0)


# Criando botões com função lambda para chamar a função de atualização
botao_dados = [
    ("C", 11, 0, 0, cor2),
    ("%", 5, 118, 0, cor5),
    ("/", 5, 177, 0, cor5),
    ("7", 5, 0, 52, cor2),
    ("8", 5, 59, 52, cor2),
    ("9", 5, 118, 52, cor2),
    ("*", 5, 177, 52, cor5),
    ("4", 5, 0, 104, cor2),
    ("5", 5, 59, 104, cor2),
    ("6", 5, 118, 104, cor2),
    ("-", 5, 177, 104, cor5),
    ("1", 5, 0, 156, cor2),
    ("2", 5, 59, 156, cor2),
    ("3", 5, 118, 156, cor2),
    ("+", 5, 177, 156, cor5),
    ("0", 11, 0, 208, cor2),
    (".", 5, 118, 208, cor2),
    ("=", 5, 177, 208, cor5),
]


# Iterando sobre a lista de botões para criá-los
for texto, largura, x, y, cor in botao_dados:
    botao = Button(
        frame_corpo,
        text=texto,
        width=largura,
        height=2,
        bg=cor,
        font=("Ivy 13 bold"),
        relief=RAISED,
        overrelief=RIDGE,
        command=lambda valor=texto: atualizar_display(valor),
    )
    botao.place(x=x, y=y)


# Inicia o loop da interface gráfica
janela.mainloop()



