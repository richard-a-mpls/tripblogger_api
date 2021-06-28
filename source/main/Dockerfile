FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY generated/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install pyjwt
RUN pip3 install flask-cors

RUN pip3 install Unicode
RUN pip3 install Unidecode
RUN pip3 install pymongo

COPY ./generated /usr/src/app

RUN mkdir /usr/src/app/swagger_server/extensions
COPY ./python/* /usr/src/app/swagger_server/extensions/

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]