from PySimpleGUI import PySimpleGUI as sg
from random import randint

#Função do resultado
def iniciar_jogo():
    if adivinhe == numero:
        resposta = (f'PARABÉNS - VOCÊ ACERTOU O NÚMERO {adivinhe} com {tentativa} tentativas!')
        
    elif adivinhe > numero:
        resposta = (f'Você errou, o número é MENOR que {adivinhe}')
        
    elif adivinhe < numero:
        resposta = (f'Você errou, o número é MAIOR que {adivinhe}')
        
    return resposta


tentativa = 1

#layout
sg.theme('dark')
layout = [
    [sg.Text('ADIVINHE O NÚMERO')],
    [sg.Text('Escolha o intervalo de números'), sg.Input(key= 'primeiro'), sg.Text('até'), sg.Input(key='segundo')],
    [sg.Button('Iniciar o jogo')],
    [sg.Text('Adivinhe um número'), sg.Input(key='aleatorio')],
    [sg.Button('Jogar')],
    [sg.Text('', key='resultado')]
]

#janela
janela = sg.Window('Jogo de adivinhação de números', layout)

#Eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Iniciar o jogo':
        primeiro = int(valores['primeiro'])
        segundo = int(valores['segundo'])
        numero = randint(primeiro,segundo)
        
    if evento == 'Jogar':
        adivinhe = int(valores['aleatorio'])
        resposta = iniciar_jogo()
        tentativa += 1
        janela['resultado'].update(resposta)

#fechamento da janela
janela.close()