import sys
from hfc.fabric import Client as client_fabric
import asyncio
import base64
import hashlib
from ecdsa import SigningKey, NIST256p
from ecdsa.util import sigencode_der, sigdecode_der

domain = ["inmetro.br"]
channel_name = "nmi-channel"
cc_name = "fabpki"
cc_version = "1.0"
callpeer = []
if __name__ == "__main__":

    #test if the meter creation time was informed as argument

    if len(sys.argv) != 2:
        print("Usage:",sys.argv[0],"<\"ID da estação\">")
        exit(1)

    #get city name
    idEstacao = str(sys.argv[1])

    #creates a loop object to manage async transactions
    loop = asyncio.get_event_loop()

    #instantiate the hyperledeger fabric client
    c_hlf = client_fabric(net_profile=(domain[0] + ".json"))

    #get access to Fabric as Admin user
    admin = c_hlf.get_user(domain[0], 'Admin')
    for i in domain:
    	callpeer.append("peer0." + i)
    
    #the Fabric Python SDK do not read the channel configuration, we need to add it mannually
    c_hlf.new_channel(channel_name)

    #invoke the chaincode to register the meter
    response = loop.run_until_complete(c_hlf.chaincode_invoke(
        requestor=admin, 
        channel_name=channel_name, 
        peers=callpeer,
        cc_name=cc_name, 
      # cc_version=cc_version,
        fcn='getStationData', 
        args=[idEstacao], 
        cc_pattern=None))

    #the signature checking returned... (true or false)
    print("Results from city weather info search:\n", response)