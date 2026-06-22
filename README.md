# Atividade Integradora

Projeto feito para a Atividade Integradora da disciplina de Desenvolvimento de Software.

O sistema tem uma pagina simples onde o usuario digita uma mensagem, envia pelo navegador e recebe uma resposta na tela.

## Funcionalidades

- Campo para digitar a mensagem.
- Botao para enviar.
- Validacao para nao enviar texto vazio.
- Area para mostrar a resposta.
- Mensagem de erro quando acontece algum problema.
- Testes para conferir o envio e o recebimento da resposta.

## Tecnologias usadas

- Python
- Flask
- HTML, CSS e JavaScript
- Pytest

## Estrutura do projeto

```text
atv_integradora/
|-- src/
|   |-- app.py
|   |-- chat_client.py
|   |-- external_client.py
|   |-- chat_service.py
|   `-- message_validator.py
|-- templates/
|   `-- index.html
|-- static/
|   |-- style.css
|   `-- app.js
|-- tests/
|   |-- test_send.py
|   `-- test_receive.py
|-- requirements.txt
|-- .env.example
`-- README.md
```

## Como executar

Primeiro instale as dependencias:

```powershell
pip install -r requirements.txt
```

Depois inicie o projeto:

```powershell
python -m src.app
```

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

## Como usar

1. Abra a pagina no navegador.
2. Digite uma mensagem no campo de texto.
3. Clique em "Enviar".
4. A resposta sera exibida na tela.

## Testes

Para rodar os testes:

```powershell
python -m pytest
```

Os testes verificam as partes principais do projeto, como validacao, envio da mensagem e retorno da resposta.

## Organizacao do codigo

- `src/app.py`: cria a aplicacao Flask e define as rotas.
- `src/chat_service.py`: organiza o envio da mensagem.
- `src/external_client.py`: faz a comunicacao externa.
- `src/message_validator.py`: valida o texto digitado pelo usuario.
- `templates/index.html`: estrutura da pagina.
- `static/app.js`: controla o envio da mensagem e a exibicao da resposta.
- `static/style.css`: define o visual da aplicacao.
