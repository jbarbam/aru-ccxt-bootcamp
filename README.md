# CCXT Bootcamp

Learn **CCXT** step by step in 2 weeks with practical coding exercises.

## 📦 Project Structure
```
ccxt-bootcamp/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ .env.example
├─ data/
├─ src/
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ utils.py
│  │  └─ io.py
│  ├─ day01_listado_exchanges.py
│  ├─ day02_tickers_basicos.py
│  ├─ day03_ohlcv_y_graficos.py
│  └─ ... up to day14_papertrading.py
└─ tests/
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/jbarbam/aru-ccxt-bootcamp.git
cd aru-ccxt-bootcamp
```

### 2. Create and activate a virtual environment
**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Copy `.env.example` to `.env` and fill in your exchange credentials (preferably testnet/sandbox):
```env
EXCHANGE=bybit
API_KEY=YOUR_KEY
API_SECRET=YOUR_SECRET
NETWORK=testnet
SYMBOLS=BTC/USDT,ETH/USDT,SOL/USDT
TIMEFRAME=1h
```
⚠️ **Never commit `.env`**. It's already excluded via `.gitignore`.

### 5. Run your first script
```bash
python src/day01_listado_exchanges.py
```
This will create a `data/exchanges.csv` file listing supported exchanges.

---

## 📚 Exercises Roadmap
- **Week 1**: Fundamentals (exchanges, tickers, OHLCV, balances, spot orders, robustness, mini dashboard).
- **Week 2**: Strategies & automation (PnL analysis, SMA signals, risk management, futures/margin, logging, alerts, bot automation, paper trading).

Each day corresponds to one file (`src/dayXX_*.py`).

---

## 🛠️ Tools & Libraries
- [CCXT](https://github.com/ccxt/ccxt) — unified crypto exchange API.
- Pandas — data manipulation.
- Matplotlib — charting.
- python-dotenv — environment variables.

---

## 🤝 Contributing
1. Fork the repo.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

---

## ⚠️ Disclaimer
This repository is **for educational purposes only**. Do not trade with real funds until you fully understand the risks. Always start in sandbox/testnet mode.

---

## 📄 License
MIT License.

