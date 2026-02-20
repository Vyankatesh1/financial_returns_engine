FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pandas numpy numpy-financial

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
