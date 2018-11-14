FROM python:3.6

EXPOSE 5000

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /code

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]