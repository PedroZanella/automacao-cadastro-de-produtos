import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.8 # tempo de espera entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1599, y=649)

# entrar no link
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa para a página carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.press("tab")
pyautogui.write("seu_email@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua_senha")
pyautogui.press("enter")
# fazer uma pausa para a página carregar
time.sleep(4)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv("produtos.csv")     
#pandas.read_excel(sheet_name="gastosano")   
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=2124, y=390)


    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":  #tratamento para campo vazio
        pyautogui.write(obs)
    pyautogui.press("enter")
    time.sleep(2)


pyautogui.scroll(5000)



