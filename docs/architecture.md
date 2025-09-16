graph TD
    A[Cliente] -->|1. Requisição HTTP (GET /praias)| B(API REST em Python);
    B -->|2. Busca dados| C{Fonte de Dados Simulada};
    C -->|3. Retorna dados| B;
    B -->|4. Resposta JSON| A;