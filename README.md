# Atividade Integradora

A aplicacao permite digitar uma pergunta em uma pagina web, enviar essa pergunta para a API da OpenAI e mostrar a resposta na tela.

## Tecnologias usadas

- Python
- Flask
- HTML, CSS e JavaScript
- API da OpenAI
- Pytest

## Estrutura do projeto

```text
atv_integradora/
|-- src/
<<<<<<< HEAD
|   |-- app.py
|   |-- chat_client.py
|   |-- openai_client.py
|   |-- chat_service.py
|   `-- prompt_validator.py
=======
|   -- app.py
|   -- ai_client.py
|   -- openai_client.py
|   -- chat_service.py
|   -- prompt_validator.py
>>>>>>> e8e074a892f176bf3c94483b03d6f175f67e2ec9
|-- templates/
|   -- index.html
|-- static/
|   -- style.css
|   -- app.js
|-- tests/
|   -- test_send.py
|   -- test_receive.py
|-- requirements.txt
|-- .env.example
 -- README.md
```

## Como executar

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

Crie o arquivo `.env` com base no `.env.example`:

```env
OPENAI_API_KEY=sua_chave_aqui
OPENAI_MODEL=gpt-3.5-turbo
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
<<<<<<< HEAD

## Observacao

Para usar a aplicacao, e necessario ter uma chave valida da API da OpenAI no arquivo `.env`.
=======
>>>>>>> e8e074a892f176bf3c94483b03d6f175f67e2ec9
