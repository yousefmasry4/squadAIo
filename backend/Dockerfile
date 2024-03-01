FROM python:3.7-alpine

COPY ./app/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]