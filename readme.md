# Rolljak - Correctness Evaluation Microservice

## Setup venv
1. Create venv
```bash
python3 -m venv es-bert-env
```

2. Activate venv
https://docs.python.org/3/tutorial/venv.html
```bash
source es-bert-env/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Getting Started
1. Start Server
```bash
uvicorn main:app --reload
```