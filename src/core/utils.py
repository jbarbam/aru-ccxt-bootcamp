import ccxt
from .config import settings


SUPPORTS_TESTNET = {"bybit", "okx", "binance"}


def get_client():
name = settings.exchange.lower()
if not hasattr(ccxt, name):
raise ValueError(f"Exchange no soportado: {name}")
klass = getattr(ccxt, name)


params = {}
if name in SUPPORTS_TESTNET and settings.network == "testnet":
params["options"] = {"defaultType": "spot"}


client = klass({
"apiKey": settings.api_key,
"secret": settings.api_secret,
**params,
})


if name in SUPPORTS_TESTNET and settings.network == "testnet":
client.set_sandbox_mode(True)


return client