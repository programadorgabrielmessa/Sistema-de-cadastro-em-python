import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro")
        self.geometry("800x600")
        self.lista_colaboradores = []
        self.id_global = tk.IntVar(value=1)

        # Estilização com ttk
        style = ttk.Style()
        style.theme_use('clam')

        # Menu superior
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        ferramentas_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ferramentas", menu=ferramentas_menu)
        ferramentas_menu.add_command(label="Relatórios", command=self.abrir_relatorios)

        # Notebook com abas
        self.notebook = ttk.Notebook(self)
        self.frame_cadastro = ttk.Frame(self.notebook)
        self.frame_consulta = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cadastro, text="Cadastro")
        self.notebook.add(self.frame_consulta, text="Consulta")
        self.notebook.pack(expand=True, fill="both")

        # Criar interfaces
        self.create_cadastro_frame()
        self.create_consulta_frame()

        # Evento para atualizar a consulta ao mudar de aba
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_selected)

    def create_cadastro_frame(self):
        # Frame para dados pessoais
        frame_dados_pessoais = tk.LabelFrame(self.frame_cadastro, text="Dados Pessoais")
        frame_dados_pessoais.pack(fill="both", expand="yes", padx=20, pady=10)

        # Campos de entrada
        tk.Label(frame_dados_pessoais, text="Nome:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.nome_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="CPF:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.cpf_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.cpf_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="RG:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.rg_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.rg_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Endereço:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.endereco_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.endereco_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Bairro:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.bairro_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.bairro_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Cidade:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        self.cidade_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.cidade_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Estado:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        self.estado_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.estado_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="País:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
        self.pais_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.pais_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="CEP:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
        self.cep_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.cep_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Telefone:").grid(row=9, column=0, sticky=tk.W, padx=10, pady=5)
        self.telefone_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.telefone_entry.grid(row=9, column=1, padx=10, pady=5)

        tk.Label(frame_dados_pessoais, text="Email:").grid(row=10, column=0, sticky=tk.W, padx=10, pady=5)
        self.email_entry = tk.Entry(frame_dados_pessoais, width=30)
        self.email_entry.grid(row=10, column=1, padx=10, pady=5)

        # Frame para dados profissionais
        frame_dados_profissionais = tk.LabelFrame(self.frame_cadastro, text="Dados Profissionais")
        frame_dados_profissionais.pack(fill="both", expand="yes", padx=20, pady=10)

        tk.Label(frame_dados_profissionais, text="Setor:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.setor_entry = tk.Entry(frame_dados_profissionais, width=30)
        self.setor_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_dados_profissionais, text="Pagamento:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.pagamento_entry = tk.Entry(frame_dados_profissionais, width=30)
        self.pagamento_entry.grid(row=1, column=1, padx=10, pady=5)

        # Frame para botões
        frame_acoes = tk.Frame(self.frame_cadastro)
        frame_acoes.pack(fill="x", padx=20, pady=10)

        ttk.Button(frame_acoes, text="Cadastrar", command=self.cadastrar_colaborador).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_acoes, text="Limpar", command=self.limpar_campos).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_acoes, text="Sair", command=self.quit).pack(side=tk.LEFT, padx=10)

    def create_consulta_frame(self):
        # Frame para busca
        frame_busca = tk.Frame(self.frame_consulta)
        frame_busca.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_busca, text="Buscar por nome:").pack(side=tk.LEFT, padx=10)
        self.busca_entry = tk.Entry(frame_busca, width=30)
        self.busca_entry.pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_busca, text="Pesquisar", command=self.pesquisar).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_busca, text="Mostrar todos", command=self.mostrar_todos).pack(side=tk.LEFT, padx=10)

        # Tabela para resultados
        self.tree = ttk.Treeview(self.frame_consulta, columns=("ID", "Nome", "CPF", "Setor"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Setor", text="Setor")
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=200)
        self.tree.column("CPF", width=150)
        self.tree.column("Setor", width=150)
        self.tree.pack(side=tk.LEFT, fill="both", expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(self.frame_consulta, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill="y")

    def cadastrar_colaborador(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        rg = self.rg_entry.get()
        endereco = self.endereco_entry.get()
        bairro = self.bairro_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()
        pais = self.pais_entry.get()
        cep = self.cep_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        setor = self.setor_entry.get()
        try:
            pagamento = float(self.pagamento_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para o pagamento.")
            return

        colaborador = {
            "id": self.id_global.get(),
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
        self.lista_colaboradores.append(colaborador)
        self.id_global.set(self.id_global.get() + 1)
        messagebox.showinfo("Sucesso", "Colaborador cadastrado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.rg_entry.delete(0, tk.END)
        self.endereco_entry.delete(0, tk.END)
        self.bairro_entry.delete(0, tk.END)
        self.cidade_entry.delete(0, tk.END)
        self.estado_entry.delete(0, tk.END)
        self.pais_entry.delete(0, tk.END)
        self.cep_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.setor_entry.delete(0, tk.END)
        self.pagamento_entry.delete(0, tk.END)

    def pesquisar(self):
        texto_busca = self.busca_entry.get().lower()
        self.tree.delete(*self.tree.get_children())
        for colaborador in self.lista_colaboradores:
            if texto_busca in colaborador["nome"].lower():
                self.tree.insert("", "end", values=(colaborador["id"], colaborador["nome"], colaborador["cpf"], colaborador["setor"]))

    def mostrar_todos(self):
        self.tree.delete(*self.tree.get_children())
        for colaborador in self.lista_colaboradores:
            self.tree.insert("", "end", values=(colaborador["id"], colaborador["nome"], colaborador["cpf"], colaborador["setor"]))

    def on_tab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Consulta":
            self.mostrar_todos()

    def abrir_relatorios(self):
        rel_win = tk.Toplevel(self)
        rel_win.title("Relatórios")
        rel_win.geometry("400x300")
        tk.Label(rel_win, text="Janela de Relatórios (exemplo)").pack(pady=20)
        # Aqui você pode adicionar mais widgets ou chamar outros scripts

if __name__ == "__main__":
    app = App()
    app.mainloop()