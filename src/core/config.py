from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    exchange: str = os.getenv("EXCHANGE", "bybit")
    api_key: str | None = os.getenv("API_KEY")
    api_secret: str | None = os.getenv("API_SECRET")
    password: str | None = os.getenv("PASSWORD")
    network: str = os.getenv("NETWORK", "testnet")
    symbols: list[str] = [s.strip() for s in os.getenv("SYMBOLS", "BTC/USDT").split(',')]
    timeframe: str = os.getenv("TIMEFRAME", "1h")


settings = Settings()