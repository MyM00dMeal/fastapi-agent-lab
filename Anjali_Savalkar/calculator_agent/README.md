# 🧮 Calculator AI Agent using FastAPI

## Overview

A **rule-based AI Agent** that performs calculator operations via REST APIs.
It receives user input, decides which operation to execute, performs the calculation, stores the result, and returns a structured response.

---

## Tech Stack

* Python 3.9+
* FastAPI, Uvicorn, Pydantic

---

## Project Structure

```
app/
├── main.py       # FastAPI entry
├── agent.py      # Decision logic
├── services.py   # Calculator operations
├── schemas.py    # Pydantic models
├── storage.py    # In-memory memory
└── utils.py      # Helpers/validation
```

---

## API Endpoints

* **POST /calculate** → Perform calculation
* **GET /history** → Get all calculations
* **GET /history/{id}** → Get calculation by ID
* **PUT /history/{id}** → Update calculation
* **DELETE /history/{id}** → Delete calculation

---

## Supported Operations

`add`, `subtract`, `multiply`, `divide`

---

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

