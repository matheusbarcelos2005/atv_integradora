# Atividade Integradora

Projeto desenvolvido para a Atividade Integradora da disciplina de Desenvolvimento de Software.

O sistema consiste em uma página simples onde o usuário digita uma mensagem, envia pelo navegador e recebe uma resposta na tela vinda de um serviço externo.

## Funcionalidades

- Campo para digitar a mensagem.
- Botão para enviar.
- Validação para não enviar texto vazio ou nulo.
- Área para exibir a resposta recebida.
- Exibição de mensagens de erro amigáveis ao usuário.
- Testes unitários e de integração automatizados.

## Tecnologias Usadas

- Python
- Flask
- HTML, CSS e JavaScript (Vanilla)
- Pytest

## Estrutura do Projeto Simplificada

```text
atv_integradora/
|-- src/
|   |-- app.py
|   |-- external_client.py
|   `-- utils.py
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

## Como Executar

Primeiro instale as dependências:

```powershell
pip install -r requirements.txt
```

Depois configure as variáveis de ambiente no arquivo `.env` (use `.env.example` como referência):

```text
API_KEY=sua_chave_de_api
API_URL=http://url-da-api.com
```

Inicie o projeto:

```powershell
python -m src.app
```

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

## Testes

Para rodar os testes automatizados:

```powershell
python -m pytest
```

Os testes cobrem a validação de mensagens e o comportamento das rotas da aplicação Flask.
