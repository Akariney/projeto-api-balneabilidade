# Projeto de API para Balneabilidade das Praias de Fortaleza

**Disciplina:** Técnicas de Integração de Sistemas (N703)
**Professor:** [Nome do Professor]
**Equipe:**
* [Nome Completo do Integrante 1] - [Matrícula]
* [Nome Completo do Integrante 2] - [Matrícula]
* [Nome Completo do Integrante 3] - [Matrícula]
* [E assim por diante...]

---

## 1. Objetivo do Trabalho

[Descreva aqui, com suas palavras, o objetivo principal do projeto. Por exemplo: "Desenvolver uma API RESTful para fornecer dados sobre a balneabilidade das praias de Fortaleza, integrando uma fonte de dados simulada para demonstrar os conceitos de integração de sistemas..."]

## 2. Descrição Funcional da Solução

[Explique aqui o que a sua API faz. Quais são as funcionalidades? Por exemplo: "A API permite que sistemas clientes consultem a lista de todas as praias monitoradas e também busquem o status de balneabilidade (própria ou imprópria) de uma praia específica através de seu identificador único..."]

## 3. Arquitetura da API

[Nesta seção, você vai colocar o link para o arquivo `architecture.md` e, se quiser, uma breve descrição da arquitetura. Por exemplo: "A arquitetura detalhada, incluindo o diagrama do sistema, pode ser encontrada em nosso documento de arquitetura: [./docs/architecture.md](./docs/architecture.md). A solução utiliza uma API em Python com o framework FastAPI..."]

## 4. Instruções para Execução via Postman/Insomnia

[Aqui você vai detalhar o passo a passo para que o professor possa testar sua API. Inclua como configurar o ambiente, como rodar o projeto e como usar a coleção do Postman/Insomnia que vocês vão fornecer.]

**Pré-requisitos:**
* Python 3.x
* Postman ou Insomnia

**Passos para Execução:**
1.  Clone o repositório: `git clone [URL_DO_SEU_REPOSITORIO]`
2.  Navegue até a pasta do projeto: `cd [NOME_DA_PASTA]`
3.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
4.  Instale as dependências: `pip install -r requirements.txt`
5.  Execute a API: `uvicorn src.main:app --reload`
6.  Importe a coleção [`postman/collection.json`](./postman/collection.json) no Postman/Insomnia e execute as requisições para os endpoints disponíveis.