from bitcoinlib.services.services import Service

srv = Service()
address_list = ['1NiNja1bUmhSoTXozBRBEtR8LeF9TGbZBN']
for a in address_list:
    print(srv.getbalance(a) / 10**8)


