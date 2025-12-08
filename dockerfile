FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium

EXPOSE 9000

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "2"]