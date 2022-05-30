from bitcoinlib.services.services import Service
from funs import get_key_from_phrase

k = get_key_from_phrase('Shinichi Mochizuki', 1)
print(k['address'])
srv = Service()
print(srv.getbalance(k['address']))
print(srv.gettransactions(k['address'], limit=1))
