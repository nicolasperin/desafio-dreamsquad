## Instalação das dependências
1. Crie o ambiente virtual:
   ```
   python3 -m venv venv
   ```
2. Ative o ambiente:
   ```
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
## Configuração do ambiente
1. Criar um arquivo .env 
    Windows:
    ```
    md .env
    ```
    Linux e macOS:
    ```
    mkdir .env
    ```
2. Adicionar as variáveis de ambiente
    ```
    MODEL_NAME=llama3
    SERVER_URL=http://localhost:11434
    ```
