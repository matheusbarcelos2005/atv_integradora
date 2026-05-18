# Integrador ChatGPT - Atividade Integradora

Aplicacao web simples em Python/Flask que envia prompts para a API do ChatGPT
(OpenAI) e exibe a resposta. Projeto da disciplina **Desenvolvimento de Software**
(FAQI Brasil), com foco em Clean Code, SOLID, testes automatizados e CI via
GitHub Actions.

## Stack

- **Linguagem:** Python 3.11+
- **Framework web:** Flask
- **Cliente da API:** SDK oficial `openai`
- **Testes:** pytest
- **CI/CD:** GitHub Actions

## Estrutura do projeto

```
atv_integradora/
├── .github/workflows/ci.yml      # Pipeline de Integracao Continua
├── src/
│   ├── ai_client.py              # Abstracao AIClient + DTO ChatResponse
│   ├── openai_client.py          # Implementacao concreta para OpenAI
│   ├── prompt_validator.py       # Regras de validacao de prompt
│   ├── chat_service.py           # Orquestrador (depende da abstracao)
│   └── app.py                    # Aplicacao Flask
├── templates/index.html          # Interface web
├── static/                       # CSS + JS do front
├── tests/
│   ├── test_send.py              # Teste 1: validacao de envio
│   └── test_receive.py           # Teste 2: validacao de recebimento
├── requirements.txt
├── .env.example
└── pytest.ini
```

## Como executar localmente

```powershell
# 1. Criar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar chave da API
Copy-Item .env.example .env
# edite o .env e coloque sua OPENAI_API_KEY

# 4. Rodar a aplicacao
python -m src.app
# abra http://127.0.0.1:5000 no navegador

# 5. Rodar os testes
pytest
```

## Boas praticas aplicadas

### Clean Code
- **Nomes significativos:** `PromptValidator.validate`, `ChatService.ask`,
  `RecordingAIClient.received_prompts`. Cada nome explica o proposito.
- **Funcoes pequenas e com unica responsabilidade.**
- **Sem comentarios redundantes** - o codigo se explica.
- **DTOs imutaveis** (`@dataclass(frozen=True)`) evitam mutacao acidental.

### SOLID
- **S (Single Responsibility):** `PromptValidator` valida; `OpenAIClient`
  chama a API; `ChatService` orquestra; `app.py` cuida de HTTP.
- **O (Open/Closed):** novos provedores (Anthropic, Groq, etc.) podem ser
  adicionados criando outra classe que herda de `AIClient`, sem alterar
  `ChatService` ou rotas.
- **L (Liskov):** `OpenAIClient`, `RecordingAIClient` e `StubAIClient`
  substituem `AIClient` sem quebrar o `ChatService` - exatamente o que
  permite mockar a API nos testes.
- **I (Interface Segregation):** `AIClient` expoe apenas `send_prompt`, sem
  metodos extras que clientes nao usariam.
- **D (Dependency Inversion):** `ChatService` depende da abstracao `AIClient`,
  nao da implementacao concreta `OpenAIClient`. O `create_app()` aceita um
  servico injetado, facilitando teste e troca de implementacao.

### Padroes de projeto
- **Strategy / Adapter:** `AIClient` define a estrategia de comunicacao com
  qualquer provedor de IA; `OpenAIClient` adapta o SDK da OpenAI a essa
  interface.
- **Factory Method:** `create_app()` constroi a aplicacao Flask com suas
  dependencias.
- **Dependency Injection** via construtor (`ChatService(client, validator)`).

## Testes unitarios

Sao dois testes obrigatorios pela rubrica, ambos rodam sem chamar a API real:

### `tests/test_send.py` - validacao de envio
- Valida que `PromptValidator` rejeita prompts vazios, em branco, nulos ou
  maiores que `MAX_LENGTH`.
- Valida que `ChatService.ask` repassa o prompt correto (e ja sanitizado)
  para o cliente.
- Valida que um prompt invalido **nao chega** ao cliente (curto-circuito
  da validacao).

Isolamento: usa `RecordingAIClient`, uma implementacao falsa de `AIClient`
que apenas registra os prompts recebidos.

### `tests/test_receive.py` - validacao de recebimento
- Valida que `ChatResponse` tem os campos `content`, `model`, `tokens_used`
  e que e imutavel.
- Valida que `ChatService` propaga corretamente cada campo do retorno do
  cliente para quem chamou.
- Cobre casos limite: resposta vazia e resposta longa.

Isolamento: usa `StubAIClient`, que sempre devolve uma `ChatResponse`
pre-configurada - permitindo simular qualquer cenario de retorno da API.

## Integracao Continua (GitHub Actions)

O workflow `.github/workflows/ci.yml` dispara em todo push para `main` e
em pull requests. Ele:

1. Faz checkout do codigo
2. Configura Python 3.11
3. Instala as dependencias
4. Executa `test_send.py`
5. Executa `test_receive.py`

Os dois testes rodam como steps separados para deixar evidente na aba
**Actions** do GitHub que ambos foram executados.
