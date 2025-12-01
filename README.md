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
    type nul > .env
    ```
    Linux e macOS:
    ```
    touch .env
    ```
2. Adicionar as variáveis de ambiente:
    ```
    MODEL_NAME=llama3.2:3b
    SERVER_URL=http://localhost:11434
    ```
3. Instalar e preparar o Ollama na sua máquina:<br>
    ```
    https://ollama.com/download
    ```
    Siga as instruções do site de acordo com o seu sistema operacional.
    <br><br>
    Após a instalação do Ollama, instale o modelo:
    ```
    ollama pull llama3.2:3b
    ```
    Inicie o servidor Ollama:
    ```
    ollama serve
    ```
## Execução da aplicação

1. Inicie o servidor do Ollama:
    ```
    ollama serve
    ```

2. Ative o ambiente virtual:
   ```
    source venv/bin/activate
   ```

3. Inicie o servidor FastAPI:
   ```
    uvicorn main:app --reload
   ```

4. Acesse a documentação interativa em: http://localhost:8000/docs


5. Envie uma requisição ao endpoint /chat com o seguinte JSON:
   ```
   "message": "Quanto é 12 * 7?"
   ```

