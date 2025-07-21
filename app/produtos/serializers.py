

class ProdutoSerializer:
    def __init__(self, data):
        self.data = data
        self.errors = {}
        self.validated_data = {}

    def is_valid(self):
        nome = self.data.get('nome')
        preco = self.data.get('preco')

        if not nome:
            self.errors['nome'] = "O campo nome é obirgatório"
        if not preco:
            self.errors['preco'] = "O campo preco é obrigatório"
        else:
            try:
                preco = float(preco)
            except(ValueError, TypeError):
                self.errors['preco'] = "Preço inválido"

        if not self.errors:
            self.validated_data = {'nome' : nome, 'preco' : preco}
            return True

        return False