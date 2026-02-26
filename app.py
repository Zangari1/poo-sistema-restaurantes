from modelos.restaurante import Restaurante

restaurante_mc = Restaurante('McDonalds', 'Fast Food')
restaurante_mc.receber_avaliacao('Pedro', 4.8)
restaurante_mc.receber_avaliacao('Eduardo', 5)
restaurante_mc.receber_avaliacao('Victor', 3.8)
restaurante_mc.alternar_status()

restaurante_bk = Restaurante('Burguer King', 'Fast Food')
restaurante_bk.receber_avaliacao('Helena', 3)
restaurante_bk.receber_avaliacao('Luana', 4)
restaurante_bk.receber_avaliacao('Giovanna', 4.9)
restaurante_bk.alternar_status()

restaurante_ph = Restaurante('Pizza Hut', 'Fast Food')
restaurante_ph.receber_avaliacao('Matheus', 3.5)
restaurante_ph.receber_avaliacao('Guilherme',5)
restaurante_ph.receber_avaliacao('Alvaro', 4.8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()