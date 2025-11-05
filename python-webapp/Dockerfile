FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock* /app/

RUN pip install --no-cache-dir -r pyproject.toml

COPY main.py /app/

EXPOSE 5000

CMD ["python", "main.py"]
