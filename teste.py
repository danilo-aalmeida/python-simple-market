import unittest
from models.produto import Produto


class ProdutoTestes(unittest.TestCase):

    def setUp(self) -> None:
        self.produto: Produto = Produto('Play Station 4', 1789.44)

    def test_codigo(self: object) -> None:
        self.assertEqual(self.produto.codigo, 1)

    def test_nome(self: object) -> None:
        self.assertEqual(self.produto.nome, 'Play Station 4')

    def test_preco(self: object) -> None:
        self.assertEqual(self.produto.preco, 1789.44)


if __name__ == '__main__':
    unittest.main()
