from random import randint

def digitar_numero():
    a = int(input('Digite o primeiro numero do intervalo: '))
    b = int(input('Digite o segundo numero do intervalo: '))
    return a, b

print('-'*80)
print('JOGO DE ADIVINHAÇÃO DE NÚMEROS')
print('-'*80)

while True:
  tentativa = 1
  a,b = digitar_numero()
  
  while a > b or a < 0 or b < 0:
    print('\nValor digitado inválido, digite novamente!')
    a,b = digitar_numero()
    
  else:
    numero = randint(a,b)
    print('-'*80)
    print('BORA PARA O JOGO')
    while True:
      adivinhe = int(input('\nADIVINHE UM NÚMERO: '))
      if adivinhe == numero:
        print(f'\nPARABÉNS - VOCÊ ACERTOU O NÚMERO {adivinhe} com {tentativa} tentativas!')
        break;
      elif adivinhe > numero:
        print(f'Você errou, o número é MENOR que {adivinhe}')
        tentativa += 1
      elif adivinhe < numero:
        print(f'Você errou, o número é MAIOR que {adivinhe}')
        tentativa += 1

  continuar = input('\nDeseja jogar novamente? (s/n): ').lower()

  if continuar == 'n':
    break;

print('-'*80)
print('FIM DO JOGO')
print('-'*80) 