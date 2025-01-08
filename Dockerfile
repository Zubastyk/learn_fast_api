FROM python:3.12-slim
WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip install --no-cache-dir poetry==1.8.3

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . ./

CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "83"]