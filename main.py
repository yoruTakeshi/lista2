import math

idrev = int(input("Digite o número do exercício: "))

if idrev == 1:
  a = float(input("Digite o valor do coeficiente a: "))
  b = float(input("Digite o valor do coeficiente b: "))
  c = float(input("Digite o valor do coeficiente c: "))
  delta = math.pow(b, 2) - (4 * a * c)
  print(delta)
  if delta < 0: print("Essa equação não possui raízes reais.")
  else:
    x1 = ((b * -1) + math.sqrt(delta)) / 2 * a
    x2 = ((b * -1) - math.sqrt(delta)) / 2 * a
    print(f"X1 = {x1}")
    print(f"X2 = {x2}")

if idrev == 2:
  unPrice = float(input("Preço unitário do produto: "))
  qtd = int(input("Quantidade comprada: "))
  valReceived = int(input("Dinheiro Recebido: "))
  if valReceived * qtd < unPrice * qtd:
    print(f"DINHEIRO INSUFICIENTE. FALTAM R$ {(unPrice*qtd)-valReceived:.2f}")
  elif valReceived * qtd > unPrice * qtd:
    print(f"TROCO: R$ {(valReceived)-(unPrice*qtd):.2f}")

if idrev == 3:
  userVal = float(input("Digite o valor gasto: "))
  option = int(
      input(
          "Digite o método de pagamento (1 - A vista, 10% de desconto; 2 - Dividir em 2x sem juros; 3 - Dividir em 3x até 10x com juros de 3% ao mês, somente para compras acima de R$100,00.): "
      ))
  if option == 1:
    desconto = (userVal / 100) * 10
    print(f"Total a Pagar: R${(userVal - desconto):.2f}")
  elif option == 2:
    numparcelas = 2
    print(
        f"Total a Pagar: R${userVal:.2f}, pagos em {numparcelas} vezes de {(userVal/numparcelas):.2f}"
    )
  elif option == 3:
    if userVal > 100:
      numparcelas = int(input("Informe o número de parcelas: "))
      juros = (userVal / 100) * 3
      print(
          f"Total a Pagar: R${userVal:.2f}, pagos em {numparcelas} vezes de R${((userVal/numparcelas)+juros):.2f}"
      )
    else:
      print("ERRO: Somente aplicável a compras acima de R$100,00.")

if idrev == 4:
  c_or_f = input("Você vai digitar a temperatura em que escala (C/F)?: ")
  if c_or_f.isupper() == False:
    c_or_f = c_or_f.upper()
  if c_or_f == "F":
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    conv = (temp - 32) * (5 / 9)
    print(f"Temperatura equivalente em Celsius: {conv:.2f}")
  if c_or_f == "C":
    temp = float(input("Digite a temperatura em Celsius: "))
    conv = (temp * (9 / 5)) + 32
    print(f"Temperatura equivalente em Fahrenheit: {conv:.2f}")

if idrev == 5:
  p1 = 5
  p2 = 3.5
  p3 = 4.8
  p4 = 8.9
  p5 = 7.32
  cod = int(input("Digite o código do produto: "))
  if cod == 1:
    qtd = int(input("Quantidade comprada: "))
    totalVal = p1 * qtd
    print(f"Valor a pagar: R$ {totalVal:.2f}")
  if cod == 2:
    qtd = int(input("Quantidade comprada: "))
    totalVal = p2 * qtd
    print(f"Valor a pagar: R$ {totalVal:.2f}")
  if cod == 3:
    qtd = int(input("Quantidade comprada: "))
    totalVal = p3 * qtd
    print(f"Valor a pagar: R$ {totalVal:.2f}")
  if cod == 4:
    qtd = int(input("Quantidade comprada: "))
    totalVal = p4 * qtd
    print(f"Valor a pagar: R$ {totalVal:.2f}")
  if cod == 5:
    qtd = int(input("Quantidade comprada: "))
    totalVal = p5 * qtd
    print(f"Valor a pagar: R$ {totalVal:.2f}")

if idrev == 6:
  sal_atual = float(input("Digite o salário da pessoa: R$ "))
  if sal_atual <= 1000:
    por = 20
    aum = (sal_atual / 100) * por
    sal_novo = sal_atual + aum
    print(f"Novo salário = R$ {sal_novo:.2f}")
    print(f"Aumento = R$ {aum:.2f}")
    print(f"Porcentagem = {por}%")
  elif sal_atual > 1000 and sal_atual <= 3000:
    por = 15
    aum = (sal_atual / 100) * por
    sal_novo = sal_atual + aum
    print(f"Novo salário = R$ {sal_novo:.2f}")
    print(f"Aumento = R$ {aum:.2f}")
    print(f"Porcentagem = {por}%")
  elif sal_atual > 3000 and sal_atual <= 8000:
    por = 10
    aum = (sal_atual / 100) * por
    sal_novo = sal_atual + aum
    print(f"Novo salário = R$ {sal_novo:.2f}")
    print(f"Aumento = R$ {aum:.2f}")
    print(f"Porcentagem = {por}%")
  elif sal_atual > 8000:
    por = 5
    aum = (sal_atual / 100) * por
    sal_novo = sal_atual + aum
    print(f"Novo salário = R$ {sal_novo:.2f}")
    print(f"Aumento = R$ {aum:.2f}")
    print(f"Porcentagem = {por}%")

if idrev == 7:
  print("Digite dois números inteiros:")
  num1 = float(input())
  num2 = float(input())
  numpor1 = num1 % num2
  numpor2 = num2 % num1
  if numpor1 == 0 or numpor2 == 0 and num1 != 0:
    print("São múltiplos")
  elif num1 == 0:
    print("Só é múltiplo de zero, o próprio zero.")
  elif num2 == 0:
    print("Achou que ia conseguir dividir por zero?")
  else:
    print("Não são múltiplos.")

if idrev == 8:
  gasType = input("Informe o combustível (G para Gasolina / A para Álcool): ")
  if gasType.isupper() is False:
    gasType = gasType.upper()
  elif gasType == "G":
    qtd = int(input("Informe a quantidade: "))
    if qtd <= 20:
      price = qtd * 2.5
      desconto = price * (2.5 / 100)
      totalprice = price - desconto
      print(f"Valor a pagar:  R$ {totalprice:.2f}")
    if qtd > 20:
      price = qtd * 2.5
      desconto = price * (6.5 / 100)
      totalprice = price - desconto
      print(f"Valor a pagar:  R$ {totalprice:.2f}")
  elif gasType == "A":
    qtd = int(input("Informe a quantidade: "))
    if qtd <= 20:
      price = qtd * 1.9
      desconto = price * (3.5 / 100)
      totalprice = price - desconto
      print(f"Valor a pagar:  R$ {totalprice:.2f}")
    elif qtd > 20:
      price = qtd * 1.9
      desconto = price * (5 / 100)
      totalprice = price - desconto
      print(f"Valor a pagar:  R$ {totalprice:.2f}")
