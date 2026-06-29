FROM python:3.12-alpine AS builder
RUN apk update && apk upgrade
WORKDIR /app
COPY requirements.txt .
RUN pip install --target=/install -r requirements.txt

FROM python:3.12-alpine
RUN apk update && apk upgrade
WORKDIR /app
COPY --from=builder /install /usr/local/lib/python3.12/site-packages
COPY app.py .
CMD ["python3", "app.py"]
