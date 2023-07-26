# https://stackoverflow.com/questions/67906542/search-for-keywords-in-file-directory

import os
import json

keywords = ['sk']

def readPath(path):
    for file in os.listdir(path):
        for keyword in keywords:
            if keyword in file:
                print(file)
                #print(os.path.abspath(file))
                filePath = '../../../' + path + file
                print(filePath)
                print('')
                return filePath

with open('blockchain/gateway/insert-estacao/connection-org1.json', 'r') as file:
    data = json.load(file)



# Orderer Admin private key
filePath = readPath('../WeatherChain/blockchain/organizations/ordererOrganizations/example.com/users/Admin@example.com/msp/keystore/')

data['organizations']['orderer.example.com']['users']['Admin']['private_key'] = filePath
with open('blockchain/gateway/insert-estacao/connection-org1.json', 'w') as file:
    json.dump(data, file, indent=2)

# Org1 Admin private key
filePath = readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp/keystore/')

data['organizations']['org1.example.com']['users']['Admin']['private_key'] = filePath
with open('blockchain/gateway/insert-estacao/connection-org1.json', 'w') as file:
    json.dump(data, file, indent=2)

# Org1 User private key
filePath = readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/')

data['organizations']['org1.example.com']['users']['User1']['private_key'] = filePath
with open('blockchain/gateway/insert-estacao/connection-org1.json', 'w') as file:
    json.dump(data, file, indent=2)

# Org2 Admin private key
readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp/keystore/')

data['organizations']['org2.example.com']['users']['Admin']['private_key'] = filePath
with open('blockchain/gateway/insert-estacao/connection-org1.json', 'w') as file:
    json.dump(data, file, indent=2)

# Org2 User private key
readPath('../WeatherChain/blockchain/organizations/peerOrganizations/org2.example.com/users/User1@org2.example.com/msp/keystore/')

data['organizations']['org2.example.com']['users']['User1']['private_key'] = filePath
with open('blockchain/gateway/insert-estacao/connection-org1.json', 'w') as file:
    json.dump(data, file, indent=2)