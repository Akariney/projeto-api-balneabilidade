# Projeto de API para Balneabilidade das Praias de Fortaleza

**Disciplina:** Técnicas de Integração de Sistemas (N703)

**Equipe:**
* Amanda Alves Eloi - 2326260
* Esther de Souza Ramalho - 2313582
* Maycon Barroso Andrade - 2323820

---

## 1. Objetivo do Trabalho

Este projeto teve como objetivo o desenvolvimento de uma API RESTful para consulta de dados sobre a balneabilidade das praias de Fortaleza. A solução demonstra a aplicação prática dos conceitos de integração de sistemas, extraindo e processando dados de um boletim oficial da SEMACE em formato PDF para disponibilizá-los de forma programática via JSON.

## 2. Descrição Funcional da Solução

Nossa API, desenvolvida em Python com FastAPI, oferece dois endpoints principais:

* `GET /praias`: Retorna a lista completa de todos os pontos de monitoramento, contendo ID, nome do local e o status de balneabilidade (Própria ou Imprópria).
* `GET /praias/{id}`: Permite a consulta de um ponto de monitoramento específico. O endpoint retorna os dados da praia correspondente ou um erro `404 Not Found` caso o ID não seja encontrado, conforme as boas práticas de tratamento de erros.

## 3. Arquitetura da API

A arquitetura da solução foi baseada na integração entre nossa API REST (sistema principal) e um arquivo de dados externo (boletim em PDF). A documentação detalhada da arquitetura e o diagrama de fluxo podem ser encontrados no arquivo: **[./docs/architecture.md](./docs/architecture.md)**.

## 4. Relação com o ODS 11 (Cidades e Comunidades Sustentáveis)

Este projeto se conecta diretamente ao Objetivo de Desenvolvimento Sustentável 11 da ONU. Ao transformar dados técnicos de um boletim em uma API aberta e acessível, contribuímos para tornar a cidade de Fortaleza mais **segura**, protegendo a saúde pública de banhistas com informações claras sobre a qualidade da água. Além disso, a iniciativa apoia a **sustentabilidade** da cidade ao promover a monitoria e a transparência sobre a condição de seus ecossistemas costeiros.

## 5. Instruções para Execução

Para executar e testar o projeto, siga os passos abaixo.

**Pré-requisitos:**
* Python 3.10 ou superior
* Git

**Passos para Execução:**
1.  Clone o repositório do GitHub:
    ```bash
    git clone [https://github.com/Akariney/projeto-api-balneabilidade.git](https://github.com/Akariney/projeto-api-balneabilidade.git)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd projeto-api-balneabilidade
    ```
3.  Crie e ative um ambiente virtual:
    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
5.  Execute a API com o servidor Uvicorn:
    ```bash
    uvicorn src.main:app --reload
    ```
6.  A API estará rodando em `http://127.0.0.1:8000`. Para testar os endpoints, importe a coleção [`postman/collection.json`](./postman/collection.json) no Postman ou Insomnia.