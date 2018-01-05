FROM django

ADD . /library

WORKDIR /library

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 127.0.0.1:8001" ]