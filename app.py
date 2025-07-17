# 1. IMPORTAÇÕES
# Importa as classes e funções necessárias:
# - Flask: A classe principal para criar a aplicação.
# - render_template: Para carregar e exibir arquivos HTML.
# - SQLAlchemy: A classe principal para interagir com o banco de dados.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# 2. CONFIGURAÇÃO DA APLICAÇÃO E DO BANCO DE DADOS
# Cria a instância principal da aplicação Flask.
app = Flask(__name__)
# Configura o caminho para o arquivo do banco de dados SQLite.
# 'sqlite:///website.db' significa que o arquivo 'website.db' será criado na pasta raiz do projeto.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///website.db"
# Cria a instância do SQLAlchemy, conectando-a com a aplicação Flask.
db = SQLAlchemy(app)


# 3. DEFINIÇÃO DO MODELO (TABELA DO BANCO DE DADOS)
# Define a estrutura da tabela 'task' no banco de dados.
# Cada classe que herda de db.Model se torna uma tabela.
class Task(db.Model):
    # Define a coluna 'id' como um inteiro e chave primária (identificador único).
    id = db.Column(db.Integer, primary_key=True)
    # Define a coluna 'description' como texto de até 100 caracteres.
    # unique=True garante que não haverá duas tarefas com a mesma descrição.
    # nullable=False significa que esta coluna não pode ser deixada em branco.
    description = db.Column(db.String(100), unique=True, nullable=False)


# 4. DEFINIÇÃO DA ROTA PRINCIPAL (VIEW)
# O decorador @app.route define qual URL ativará a função abaixo.
# '/' é a rota raiz do site (página inicial).
@app.route("/")
def index():
    # OBS: Esta é uma lista estática. O próximo passo seria buscar do banco de dados.
    # Exemplo de como seria: tasks = Task.query.all()
    tasks = [
        "Tarefa A",
        "Tarefa B",
        "Tarefa C",
    ]
    # Carrega o arquivo 'index.html' da pasta 'templates' e passa a variável 'tasks' para ele.
    return render_template("index.html", tasks=tasks)


# 5. EXECUÇÃO DA APLICAÇÃO
# Este bloco de código só é executado quando o script 'app.py' é rodado diretamente.
if __name__ == "__main__":
    # O contexto da aplicação é necessário para que o SQLAlchemy saiba qual aplicação
    # está usando o banco de dados.
    with app.app_context():
        # Este comando cria todas as tabelas definidas nos modelos (como a classe Task).
        # Ele só cria as tabelas que ainda não existem.
        db.create_all()
    # Inicia o servidor de desenvolvimento do Flask.
    # debug=True ativa o modo de depuração, que reinicia o servidor a cada alteração
    # e mostra erros detalhados no navegador.
    app.run(debug=True, port=5153)