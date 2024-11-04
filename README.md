# Auth MS Serverless Lambda Python

Este projeto é um serviço de autenticação serverless utilizando AWS Lambda e Chalice. Ele fornece endpoints para login, cadastro e atualização de tokens utilizando Firebase Authentication.

## Endpoints

### Login

- **URL:** `/login`
- **Método:** `POST`
- **Descrição:** Autentica um usuário com email e senha.
- **Exemplo de Corpo da Requisição:**
  ```json
  {
    "email": "usuario@example.com",
    "password": "senha123"
  }

###<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'> Cadastro</vscode_annotation>

### Signup

- **URL:** `/signup`
- **Método:** `POST`
- **Descrição:** Cria um novo usuário com email e senha.
- **Exemplo de Corpo da Requisição:**
  ```json
  {
    "email": "novo_usuario@example.com",
    "password": "senha123"
  }

### Refresh token

- **URL:** `/signup`
- **Método:** `POST`
- **Descrição:** Cria um novo usuário com email e senha.
- **Exemplo de Corpo da Requisição:**
  ```json
  {
    "refresh_token": "token_de_atualizacao"
  }

## Pré-requisitos

- Python 3.8+
- AWS CLI configurado
- Chalice instalado (pip install chalice)
