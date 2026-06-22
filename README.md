# Atividade Integradora

Aplicacao web desenvolvida para a Atividade Integradora. O sistema permite digitar uma pergunta em uma pagina web, enviar o prompt para o ChatGPT e exibir a resposta retornada na tela.

## Objetivo

Demonstrar a integracao entre uma interface web, uma aplicacao Flask e um servico externo de inteligencia artificial, mantendo separacao entre validacao, regra de negocio e comunicacao com o cliente da OpenAI.

## Funcionalidades

- Envio de prompts pela interface web.
- Validacao de prompts vazios ou muito longos.
- Exibicao da resposta gerada pelo modelo.
- Exibicao do modelo utilizado e da quantidade de tokens.
- Tratamento de erros de validacao e falhas de comunicacao.
- Testes automatizados para envio, validacao e recebimento de respostas.

## Tecnologias usadas

- Python
- Flask
- HTML, CSS e JavaScript
- OpenAI
- Pytest

## Estrutura do projeto

```text
atv_integradora/
|-- src/
|   |-- app.py
|   |-- chat_client.py
|   |-- openai_client.py
|   |-- chat_service.py
|   `-- prompt_validator.py
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

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

Inicie o projeto:

```powershell
python -m src.app
```

Depois acesse no navegador:

```text
http://127.0.0.1:5000
```

## Como usar

1. Abra a pagina no navegador.
2. Digite uma pergunta no campo de texto.
3. Clique em "Enviar".
4. A resposta sera exibida na tela.

## Testes

Para rodar os testes:

```powershell
python -m pytest
```

Os testes verificam se o envio do prompt e o recebimento da resposta estao funcionando corretamente.

## Organizacao do codigo

- `src/app.py`: cria a aplicacao Flask e define as rotas.
- `src/chat_service.py`: concentra a regra de negocio do envio do prompt.
- `src/openai_client.py`: faz a comunicacao com a OpenAI.
- `src/prompt_validator.py`: valida o texto digitado pelo usuario.
- `templates/index.html`: estrutura da pagina.
- `static/app.js`: controla o envio do prompt e a exibicao da resposta.
- `static/style.css`: define o visual da aplicacao.
