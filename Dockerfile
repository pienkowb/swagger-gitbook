FROM python:3.8

WORKDIR /app

COPY *.py /app/

ENTRYPOINT ["./swagger-gitbook.py"]
