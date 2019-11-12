FROM python:3.7.3-stretch

WORKDIR /flask

COPY server/server.py /flask/
COPY server/requirements.txt /flask/
COPY server/db /flask/

RUN pip3 install --upgrade pip &&\
    pip3 install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "server.py" ] 