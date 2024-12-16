# Conversor de moedas
real = float(input('Quanto dinheiro você tem na carteira?:R$'))
dolar = real/ 5.15
euro = real/5.51
print ('com R${:.2f} você pode comprar US$ {:.2f}, valor em  € {:.2f} ' .format (real, dolar, euro))