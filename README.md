# Automação de Cadastro de Produtos

## 📋 Descrição

Este projeto é uma automação desenvolvida em Python para realizar o cadastro automático de produtos em um sistema web. A automação lê os dados de uma tabela CSV e os insere automaticamente no sistema, eliminando a necessidade de digitação manual.

## 🚀 Funcionalidades

O script realiza as seguintes etapas automaticamente:

1. **Abertura do navegador**: Abre o Google Chrome através do menu iniciar do Windows
2. **Acesso ao site**: Navega até o sistema de cadastro (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
3. **Login no sistema**: Preenche automaticamente as credenciais de e-mail e senha para autenticação
4. **Leitura dos dados**: Importa os produtos a serem cadastrados a partir do arquivo `produtos.csv`
5. **Cadastro dos produtos**: Para cada produto na tabela, preenche os campos:
   - Código
   - Marca
   - Tipo
   - Categoria
   - Preço Unitário
   - Custo
   - Observações (quando houver)

## 📁 Estrutura dos Dados (produtos.csv)

O arquivo CSV contém as seguintes colunas:

| Coluna | Descrição |
|--------|-----------|
| codigo | Código identificador do produto |
| marca | Marca do produto (ex: Logitech, Hashtag, Samsung) |
| tipo | Tipo do produto (ex: Mouse, Camisa, Televisão) |
| categoria | Categoria numérica |
| preco_unitario | Preço de venda |
| custo | Custo do produto |
| obs | Observações adicionais (opcional) |

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem de programação
- **PyAutoGUI** - Biblioteca para automação de GUI (controle de mouse e teclado)
- **Pandas** - Biblioteca para manipulação e leitura de dados CSV

## ⚙️ Pré-requisitos

- Python 3.x instalado
- Bibliotecas: `pyautogui` e `pandas`
- Google Chrome instalado
- Resolução de tela configurada (as coordenadas de clique podem precisar de ajuste)

## 📌 Observações

- As coordenadas de clique do mouse estão configuradas para uma resolução específica e podem precisar ser ajustadas conforme seu monitor
- O arquivo `pegar_posicao.py` pode ser utilizado para capturar as coordenadas corretas da sua tela
- Certifique-se de atualizar as credenciais de login no script antes de executar
