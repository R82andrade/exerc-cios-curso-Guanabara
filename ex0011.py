#  calculando descontos
preço = float (input('Digite o valor do produto:'))
novo = preço - (preço * 5 /100) 
print ('o produto no valor normal  é R${} com o desconto 5% vai custar R${}'.format (preço, novo))