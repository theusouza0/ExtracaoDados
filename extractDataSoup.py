import requests
from bs4 import BeautifulSoup
import telebot

# Definir o alvo
url = "https://www.uol.com.br/"

# Enviar request com timeout de 10s
try: 
    response = requests.get(url, timeout = 10)

    # Tratamento dos dados HTML através da request feita
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trazer todos os títulos dos artigos publicados na página
    mainArticles = soup.find_all('h3', class_="title__element headlineMain__title") 
    subArticles = soup.find_all('h3', class_="title__element headlineSub__content__title") 
       
    # Imprimir os títulos
    for mainArticle in mainArticles:
        print(mainArticle.text)

    for subArticles in subArticles:
        print(subArticles.text)
        
# Tratamento de possíveis erros na requisição:
except requests.exceptions.HTTPError as http_err:
    print(f"Erro HTTP: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Erro de conexão: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Erro de timeout: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Erro ao fazer a requisição: {req_err}")
except Exception as e:
    print(f"Erro inesperado: {e}")