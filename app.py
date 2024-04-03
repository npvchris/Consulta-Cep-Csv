import pandas as pd
import tkinter as tk

# Função para verificar a disponibilidade do CEP no arquivo CSV correspondente ao tipo selecionado
def verificar_disponibilidade_cep(cep, tipo_consulta):
    try:
        # Carregar o arquivo CSV correspondente ao tipo de consulta
        df = pd.read_csv(f"{tipo_consulta}.csv")
        # Verificar se o CEP está na lista
        if cep in df['CEP'].astype(str).values:
            return "Cabeamento disponível para este CEP.", "green"
        else:
            return "Cabeamento não disponível para este CEP.", "red"
    except FileNotFoundError:
        return f"Arquivo {tipo_consulta}.csv não encontrado.", "red"


# Função para lidar com o evento de clique no botão de consulta
def consultar():
    cep = entry_cep.get()
    tipo_consulta = var_tipo.get()
    
    mensagem_retorno, cor = verificar_disponibilidade_cep(cep, tipo_consulta)
    
    # Criar janela de mensagem personalizada
    popup = tk.Toplevel()
    popup.title("Resultado da Consulta")
    label = tk.Label(popup, text=mensagem_retorno, bg=cor)
    label.pack(padx=20, pady=10)

# Criar a interface gráfica
root = tk.Tk()
root.title("Consulta de CEP")
root.geometry("300x200")

# Entrada para o CEP
label_cep = tk.Label(root, text="CEP:")
label_cep.pack()
entry_cep = tk.Entry(root)
entry_cep.pack()

# Opção para selecionar o tipo de consulta
label_tipo = tk.Label(root, text="Selecione o tipo de consulta:")
label_tipo.pack()
var_tipo = tk.StringVar()
var_tipo.set("CLARO")  # Opção padrão
radio_claro = tk.Radiobutton(root, text="CLARO", variable=var_tipo, value="CLARO")
radio_claro.pack(anchor=tk.W)
radio_tim = tk.Radiobutton(root, text="TIM", variable=var_tipo, value="TIM")
radio_tim.pack(anchor=tk.W)
radio_vivo = tk.Radiobutton(root, text="VIVO", variable=var_tipo, value="VIVO")
radio_vivo.pack(anchor=tk.W)

# Botão de consulta
button_consultar = tk.Button(root, text="Consultar", command=consultar)
button_consultar.pack()

root.mainloop()
