# DESAFIO
'''
Crie um programa que vai até onde seu bloco de notas estiver aberto e digite a frase
"Automação é incrível!"
'''
import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("command","v")

# Mover mouse até campo de digitar
pyautogui.moveTo(2296,102, duration=2)
# Clicar no campo de digitar
pyautogui.click()
# Digitar minha mensagem
escrever_frase("Automação é incrível!")
