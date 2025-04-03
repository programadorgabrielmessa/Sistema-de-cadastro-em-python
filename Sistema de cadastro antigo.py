import tkinter as tk
from tkinter import messagebox

# Funções para manipulação de dados
def cadastrar_colaborador():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    rg = rg_entry.get()
    endereco = endereco_entry.get()
    bairro = bairro_entry.get()
    cidade = cidade_entry.get()
    estado = estado_entry.get()
    pais = pais_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    setor = setor_entry.get()
    try:
        pagamento = float(pagamento_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o pagamento.")
        return

    colaborador = {
        "id": id_global.get(),
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "endereco": endereco,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
        "cep": cep,
        "telefone": telefone,
        "email": email,
        "setor": setor,
        "pagamento": pagamento
    }
    lista_colaboradores.append(colaborador)
    id_global.set(id_global.get() + 1)
    messagebox.showinfo("Sucesso", "Colaborador cadastrado com sucesso!")
    limpar_campos()

def limpar_campos():
    nome_entry.delete(0, tk.END)
    cpf_entry.delete(0, tk.END)
    rg_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)
    bairro_entry.delete(0, tk.END)
    cidade_entry.delete(0, tk.END)
    estado_entry.delete(0, tk.END)
    pais_entry.delete(0, tk.END)
    cep_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    setor_entry.delete(0, tk.END)
    pagamento_entry.delete(0, tk.END)

# Inicializa a aplicação e a janela principal
app = tk.Tk()
app.title("Sistema de Cadastro")
app.geometry("800x600")

# Variáveis globais
id_global = tk.IntVar(value=0)
lista_colaboradores = []

# Criação dos frames
frame_dados_pessoais = tk.LabelFrame(app, text="Dados Pessoais")
frame_dados_pessoais.pack(fill="both", expand="yes", padx=10, pady=10)

# Campos de entrada de dados pessoais
tk.Label(frame_dados_pessoais, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
nome_entry = tk.Entry(frame_dados_pessoais, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="CPF:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
cpf_entry = tk.Entry(frame_dados_pessoais, width=30)
cpf_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="RG:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
rg_entry = tk.Entry(frame_dados_pessoais, width=30)
rg_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Endereço:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
endereco_entry = tk.Entry(frame_dados_pessoais, width=30)
endereco_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Bairro:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
bairro_entry = tk.Entry(frame_dados_pessoais, width=30)
bairro_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Cidade:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
cidade_entry = tk.Entry(frame_dados_pessoais, width=30)
cidade_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Estado:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
estado_entry = tk.Entry(frame_dados_pessoais, width=30)
estado_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="País:").grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
pais_entry = tk.Entry(frame_dados_pessoais, width=30)
pais_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="CEP:").grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
cep_entry = tk.Entry(frame_dados_pessoais, width=30)
cep_entry.grid(row=8, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Telefone:").grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)
telefone_entry = tk.Entry(frame_dados_pessoais, width=30)
telefone_entry.grid(row=9, column=1, padx=5, pady=5)

tk.Label(frame_dados_pessoais, text="Email:").grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)
email_entry = tk.Entry(frame_dados_pessoais, width=30)
email_entry.grid(row=10, column=1, padx=5, pady=5)

# Frame de dados profissionais
frame_dados_profissionais = tk.LabelFrame(app, text="Dados Profissionais")
frame_dados_profissionais.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Label(frame_dados_profissionais, text="Setor:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
setor_entry = tk.Entry(frame_dados_profissionais, width=30)
setor_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_dados_profissionais, text="Pagamento:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
pagamento_entry = tk.Entry(frame_dados_profissionais, width=30)
pagamento_entry.grid(row=1, column=1, padx=5, pady=5)

# Botões de ação
frame_acoes = tk.Frame(app)
frame_acoes.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Button(frame_acoes, text="Cadastrar", command=cadastrar_colaborador).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(frame_acoes, text="Limpar", command=limpar_campos).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(frame_acoes, text="Sair", command=app.quit).pack(side=tk.LEFT, padx=5, pady=5)

# Inicializa o loop da aplicação
app.mainloop()
