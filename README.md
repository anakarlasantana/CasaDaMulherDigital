# Casa da Mulher Digital - Backend Django

O projeto Casa da Mulher Digital inclui um backend desenvolvido com Django, que serve como a base para a plataforma digital da Secretaria das Mulheres do Estado do Ceará.

Bibliotecas e Ferramentas do Projeto
O backend Django utiliza as seguintes bibliotecas e ferramentas:

- **Django**: O framework web que facilita o desenvolvimento rápido e limpo.
- **djangorestframework**: Para criar APIs robustas e flexíveis.
- **drf-spectacular**: Para gerar documentação da API com Swagger.
- **django-cors-headers**: Para gerenciar o CORS e permitir requisições entre diferentes domínios.
- **asgiref**: Utilizado para suporte ao ASGI.
- **jsonschema** e **jsonschema-specifications**: Para validação de dados.
- **PyYAML**: Para trabalhar com arquivos YAML.
- **sqlparse**: Para parsing de SQL.
- **tzdata**: Para suporte a dados de fusos horários.
- **SQLite**: O projeto está configurado para usar o SQLite como banco de dados padrão.

# Como Rodar o Projeto Localmente
Para rodar o backend Django localmente, siga os passos abaixo:

1. Clone o Repositório
Primeiro, clone o repositório do backend para sua máquina local. No terminal, execute:

```bash
git clone https://github.com/anakarlasantana/CasaDaMulherDigital_api.git
```

2. Crie e Ative um Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto. Crie e ative o ambiente virtual:
```bash
Crie:
python -m venv env
Ative:
.\env\Scripts\activate
```
3. Instale as Dependências
Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
4. Configure o Banco de Dados
Aplique as migrações para configurar o banco de dados:
```bash
python manage.py migrate
```
5. Inicie o Servidor de Desenvolvimento
Agora você pode iniciar o servidor de desenvolvimento do Django:
Aplique as migrações para configurar o banco de dados:
```bash
python manage.py runserver
```

O servidor estará disponível em http://localhost:5173/.

6. Acessando o Django Admin você poderá testar o CRUD do banco.
```bash
Login: admin
Senha: admin
```
7. Acesse a Documentação da API
http://127.0.0.1:8000/api/docs/swagger-ui/
ou
http://127.0.0.1:8000/api/docs/redoc/

# Pronto para Começar!
Com o backend Django em funcionamento, você está pronto para desenvolver a plataforma. Se precisar de ajuda ou tiver dúvidas, consulte a documentação adicional ou entre em contato com a equipe
