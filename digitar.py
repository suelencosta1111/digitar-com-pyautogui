# Como digitar com PyAutoGUI
import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("command","v")

# Mover mouse até campo de digitar
pyautogui.moveTo(2659,1054, duration=2)
# Clicar no campo de digitar
pyautogui.click()
# Digitar minha mensagem
escrever_frase("Sou um robô incrível :D")
# Clicar no botão de enviar
pyautogui.click(3172,1053, duration=2)