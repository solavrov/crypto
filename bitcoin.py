from bitcoinlib.services.services import Service

srv = Service()
address_list = ['1NiNja1bUmhSoTXozBRBEtR8LeF9TGbZBN']
print(srv.getbalance(address_list) / 10**8)

