FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install flask

ENTRYPOINT [ "python" ]

CMD ["dz7.py"]