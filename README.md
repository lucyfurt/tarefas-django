\# Task Management System

\## Descrição

Este é um sistema de gestão de tarefas desenvolvido em Django, utilizando PostgreSQL como banco de dados e templates do Django para renderização de páginas HTML. O objetivo deste projeto é permitir aos usuários criar, visualizar, atualizar e excluir tarefas de forma simples e eficiente.

\## Tecnologias Utilizadas

- \*\*Django\*\*: Framework web utilizado para o desenvolvimento do backend.
- \*\*PostgreSQL\*\*: Sistema de gerenciamento de banco de dados utilizado para armazenar os dados.
- \*\*TEMPLATE DJANGO\*\*: Utilizado através dos templates do Django para renderizar as páginas do sistema.

\## Funcionalidades

- \*\*Cadastro de Usuários\*\*: Possibilidade de criar novos usuários.
- \*\*Login/Logout\*\*: Sistema de autenticação para acesso seguro às funcionalidades.
- \*\*CRUD de Tarefas\*\*: Permite criar, visualizar, atualizar e excluir tarefas.


\## Como Executar o Projeto

\### Pré-requisitos

- \*\*Python 3.x\*\*: Linguagem de programação utilizada.
- \*\*Django 3.x\*\*: Framework web utilizado.
- \*\*PostgreSQL\*\*: Banco de dados utilizado.
- \*\*pip\*\*: Gerenciador de pacotes do Python.

\### Passos para Execução

1. \*\*Clone o Repositório\*\*

\```bash

git clone https://github.com/lucyfurt/tarefas-django.git



\```

1. \*\*Crie e Ative um Ambiente Virtual\*\*

\```bash

python -m venv venv

source venv/bin/activate  # No Windows: venv\Scripts\activate

\```

1. \*\*Instale as Dependências\*\*

\```bash

pip install -r requirements.txt

\```

1. \*\*Configure o Banco de Dados\*\*

Edite o arquivo `settings.py` e configure as informações do banco de dados PostgreSQL:

\```python

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.postgresql',

'NAME': 'nome\_do\_banco',

'USER': 'seu\_usuario',

'PASSWORD': 'sua\_senha',

'HOST': 'localhost',

'PORT': '5432',

}

}

\```

1. \*\*Aplique as Migrações\*\*

\```bash

python manage.py migrate

\```

1. \*\*Crie um Superusuário\*\*

\```bash

python manage.py createsuperuser

\```

1. \*\*Execute o Servidor de Desenvolvimento\*\*

\```bash

python manage.py runserver

\```

1. \*\*Acesse a Aplicação\*\*

Abra o navegador e acesse `http://127.0.0.1:8000` para utilizar a aplicação.

\## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

\## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.

\---

\### Notas Adicionais

- Certifique-se de ter o PostgreSQL instalado e em execução.
- Você pode criar um arquivo `.env` para armazenar as configurações sensíveis, como informações do banco de dados.
- Considere adicionar testes automatizados para garantir a qualidade do código.

