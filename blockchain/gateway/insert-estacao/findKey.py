# https://stackoverflow.com/questions/67906542/search-for-keywords-in-file-directory

import os
import json

keywords = ['sk']

def readPath(path):
    for file in os.listdir(path):
        for keyword in keywords:
            if keyword in file:
                #print(file)
                #print(os.path.abspath(file))
                #filePath = '../../../' + path + file
                filePath = path + file
                #print(filePath)
                #print('')
                return filePath

jsonPath = ''

print("Verificando chaves...")
try:
    with open('../WeatherChain/blockchain/gateway/insert-estacao/connection-org1.json', 'r') as file:
        data = json.load(file)
        jsonPath = '../WeatherChain/blockchain/gateway/insert-estacao/connection-org1.json'
except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        with open('../../../../WeatherChain/blockchain/gateway/insert-estacao/connection-org1.json', 'r') as file:
            data = json.load(file)
        jsonPath = '../../../../WeatherChain/blockchain/gateway/insert-estacao/connection-org1.json'
    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')

# Orderer Admin private key
try:
    filePath = readPath('../WeatherChain/blockchain/organizations/ordererOrganizations/example.com/users/Admin@example.com/msp/keystore/')

except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        filePath = readPath('../../../../WeatherChain/blockchain/organizations/ordererOrganizations/example.com/users/Admin@example.com/msp/keystore/')

    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')

'''
if data['organizations']['orderer.example.com']['users']['Admin']['private_key'] == filePath:
    #print("As chaves já estão atualizadas!")
    raise Exception("As chaves já estão atualizadas")
'''

data['organizations']['orderer.example.com']['users']['Admin']['private_key'] = filePath
with open(jsonPath, 'w') as file:
    json.dump(data, file, indent=2)

# Org1 Admin private key
try:
    filePath = readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/keystore/')

except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        filePath = readPath('../../../../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/keystore/')

    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')


data['organizations']['org1.example.com']['users']['Admin']['private_key'] = filePath
with open(jsonPath, 'w') as file:
    json.dump(data, file, indent=2)

# Org1 User private key
try:
    filePath = readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/')

except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        filePath = readPath('../../../../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/')

    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')


data['organizations']['org1.example.com']['users']['User1']['private_key'] = filePath
with open(jsonPath, 'w') as file:
    json.dump(data, file, indent=2)

# Org2 Admin private key

try:
    readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp/keystore/')

except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        readPath('../../../../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp/keystore/')

    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')


data['organizations']['org2.example.com']['users']['Admin']['private_key'] = filePath
with open(jsonPath, 'w') as file:
    json.dump(data, file, indent=2)

# Org2 User private key
try:
    readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/User1@org2.example.com/msp/keystore/')

except FileNotFoundError:
    print('Caminho não encontrado. Tentando um caminho alternativo...')
    
    try:
        readPath('../../../../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/User1@org2.example.com/msp/keystore/')

    except FileNotFoundError:
        print('Arquivo não encontrado no caminho alternativo.')

else:
    print('Arquivo encontrado')


data['organizations']['org2.example.com']['users']['User1']['private_key'] = filePath
with open(jsonPath, 'w') as file:
    json.dump(data, file, indent=2)