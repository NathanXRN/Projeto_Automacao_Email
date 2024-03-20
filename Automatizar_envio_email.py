import yfinance
import pyautogui
import pyperclip
import time

codigo = input("Digite o código da ação desejada: ")
dados = yfinance.Ticker(codigo).history("6mo")

fechamento = dados.Close

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento.iloc[-1]

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")

pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.click(x = 84, y = 188)

pyperclip.copy("nathanxavier84@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy("Análises Diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

mensagem = f"""
Prezado Gestor,

Seguem as análises dos últimos seis meses da ação {codigo} conforme solicitado:

Cotação máxima: R$ {round(maxima, 2)}
Cotação mínima: R$ {round(minima, 2)}
Cotação atual: R$ {round(atual, 2)}

 Qual dúvida, estou à disposição!

Atte.
"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x = 1308, y = 1002)
