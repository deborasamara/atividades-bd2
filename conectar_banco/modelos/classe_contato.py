class Contato:
    def __init__(self, id, nome, email, telefone, rua, cidade, estado, data_cadastro):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.rua = rua
        self.cidade = cidade 
        self.estado = estado
        self.data_cadastro = data_cadastro

        # recuperador de dados
        def id(self):
                return self.id
                
        def nome(self):
                return self.rua
                
        def email(self):
                return self.cidade
        
        def telefone(self):
                return self.id
                
        def rua(self):
                return self.rua
                
        def cidade(self):
                return self.cidade
                
        def estado(self):
                return self.rua
                
        def data_cadastro(self):
                return self.cidade
                
        # receber dados
        def id(self, id):
                self.id = id
                
        def nome(self, nome):
                self.nome = nome

        def email(self, email):
                self.email = email

        def telefone(self, telefone):
                self.telefone = email
                
        def rua(self, rua):
                self.rua = rua

        def cidade(self, cidade):
                self.cidade = cidade

        def estado(self, estado):
                self.estado = estado

        def data_cadastro(self, data_cadastro):
                self._data_cadastro = data_cadastro
                
        def __str__(self):
                return f'Contato: {self.id}, {self.nome}, {self.email}, {self.telefone}, {self.estado}, {self.cidade}'