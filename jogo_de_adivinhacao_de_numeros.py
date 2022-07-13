from PySimpleGUI import PySimpleGUI as sg
from random import randint

#Função do resultado
def iniciar_jogo():
  if adivinhe == numero:
      resposta = (f'PARABÉNS - VOCÊ ACERTOU!\nNÚMERO CORRETO: {adivinhe}\nGASTOU: {tentativa} tentativas!')   
  elif adivinhe > numero:
      resposta = (f'Você errou, o número é MENOR que {adivinhe}')
  elif adivinhe < numero:
      resposta = (f'Você errou, o número é MAIOR que {adivinhe}')
  return resposta

def esconder_campos():
  janela['resultado'].update('')
  janela['texto_adivinhe'].update(visible=False)
  janela['aleatorio'].update(visible=False)
  janela['botao_jogar'].update(visible=False)
  janela['jogar_novamente'].update(visible=False)
  

#layout
layout_esquerda=[[sg.Image(filename='jogo.png')]]

layout_direita=[
    [sg.Push(), sg.Text('JOGO DE ADIVINHAÇÃO DE NÚMEROS',font=('helvetica', 25)), sg.Push()],
    [sg.Text('')],
    [sg.Push(),sg.Text('Escolha o intervalo de números:',font=('helvetica',20)), 
    sg.Input(key= 'primeiro', size = (6,3),font=('helvetica',20)), 
    sg.Text('até',font=('helvetica',20)), 
    sg.Input(key='segundo', size=(6,3),font=('helvetica',20)),sg.Push()],
    [sg.Push(), sg.Button('Iniciar o jogo',font=('helvetica',20)), sg.Push()],
    [sg.Text('')],
    [sg.Text('Adivinhe um número: ', font=('helvetica',20), visible=False, key='texto_adivinhe'), 
    sg.Input(key='aleatorio', size=(5,2),font=('helvetica',20),visible=False), 
    sg.Button('Jogar',font=('helvetica',20),visible=False,key='botao_jogar')],
    [sg.Text('')],
    [sg.Push(), sg.Text('', key='resultado',font=('helvetica',25)),sg.Push()],
    [sg.Button('JOGAR NOVAMENTE', font=('helvetica',20),visible=False, key='jogar_novamente')]
]

sg.theme('darkpurple')
layout = [[sg.Column(layout_esquerda),sg.VSeparator(),sg.Column(layout_direita, element_justification="center")]]

#janela
janela = sg.Window('Jogo de adivinhação de números', layout, size = (1250,500))

#Eventos
adivinhe = 0
while True:
    evento, valores = janela.read()
    
    try:  
      if evento == sg.WIN_CLOSED:
        break

      if evento == 'Iniciar o jogo':
        primeiro = int(valores['primeiro'])
        segundo = int(valores['segundo'])
        janela['texto_adivinhe'].update(visible=True)
        janela['aleatorio'].update(visible=True)
        janela['botao_jogar'].update(visible=True)
        numero = randint(primeiro,segundo)
        tentativa = 1

      if evento == 'botao_jogar':
        adivinhe = int(valores['aleatorio'])
        resposta = iniciar_jogo()
        tentativa += 1
        janela['resultado'].update(resposta)

      if adivinhe == numero:
        janela['jogar_novamente'].update(visible=True)
      
      if evento == 'jogar_novamente':
        esconder_campos()
        adivinhe = 0
        numero = ''
    except:
      if valores['primeiro'] == '' and valores['segundo'] == '':
        sg.Popup('VOCÊ NÃO DIGITOU NENHUM NÚMERO NO CAMPO', font=('helvetica', 15))
        esconder_campos()
      if valores['primeiro'] == '':
        sg.Popup('VOCÊ DIGITOU APENAS UM NÚMERO', font=('helvetica', 15))
        esconder_campos()
      if valores['segundo'] == '':
        sg.Popup('VOCÊ DIGITOU APENAS UM NÚMERO', font=('helvetica', 15))
        esconder_campos()
      if primeiro > segundo:
        sg.Popup('O PRIMEIRO NÚMERO NÃO PODE SER MAIOR QUE O SEGUNDO', font=('helvetica', 15))
        esconder_campos()

#fechamento da janela
janela.close()