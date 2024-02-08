from pymongo import MongoClient

# Conecte ao MongoDB Atlas (substitua 'seu_uri' pelo URI real)
client = MongoClient('seu_uri')

# Crie um banco de dados chamado 'banco_nosql'
db = client['banco_nosql']

# Crie uma coleção chamada 'bank' para armazenar documentos de clientes
collection = db['bank']

# Insira documentos com a estrutura mencionada
document1 = {
    'cliente_id': 1,
    'nome': 'Matheus Silva',
    'cpf': '111.222.333-44',
    'endereco': 'Rua Principal, número 123',
    'contas': [
        {
            'tipo': 'cc',
            'agencia': 1001,
            'numero': 10001,
            'saldo': 7000
        },
        {
            'tipo': 'cp',
            'agencia': 1001,
            'numero': 20001,
            'saldo': 20000
        }
    ]
}

document2 = {
    'cliente_id': 2,
    'nome': 'Sandra Oliveira',
    'cpf': '555.666.777-88',
    'endereco': 'Avenida Central, número 789',
    'contas': [
        {
            'tipo': 'cc',
            'agencia': 1001,
            'numero': 10002,
            'saldo': 2500
        }
    ]
}

document3 = {
    'cliente_id': 3,
    'nome': 'Patrick Oliveira',
    'cpf': '999.888.777-66',
    'endereco': 'Rua da Praça, número 456',
    'contas': [
        {
            'tipo': 'cp',
            'agencia': 1001,
            'numero': 20002,
            'saldo': 12000
        }
    ]
}

# Insira os documentos na coleção
collection.insert_many([document1, document2, document3])

# Recupere informações com base nos pares de chave e valor
# Exemplo: Recupere informações sobre o cliente com CPF '111.222.333-44'
result = collection.find_one({'cpf': '111.222.333-44'})

# Imprima o resultado
print(result)
