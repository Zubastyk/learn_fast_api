FROM python:3.12-slim

COPY . .

RUN pip install --no-cache-dir poetry==1.8.3

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["python", "src/main.py", "--host", "0.0.0.0", "--port", "80"]