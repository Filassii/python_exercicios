produtos = {
    1: ['Monitor LED"', 599.99, 1],
    2: ['Teclado Wireless', 49.26, 1],
    3: ['Cartucho Colorido ', 19.90, ],
    4: ['Mouse Wireless', 54.00,2]
}
total= 0

print(50 * '-')
print('Carrinho de compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal= prod[1] * prod[2]
    print(f'{prod} - R$ {prod[1:]:.2f} - {prod[2]} un - R$ {subtotal:.2f}')
    total += subtotal

print(50 * '-')
print(f'Total da compra: R$ {total:.2f}')
print(50 * '-')

