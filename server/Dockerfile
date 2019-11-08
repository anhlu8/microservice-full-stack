ARG PYTHON_IMAGE_VERSION

FROM python:$PYTHON_IMAGE_VERSION

WORKDIR /flask

COPY server.py /flask/
COPY requirements.txt /flask/
COPY db /flask/

RUN pip3 install --upgrade pip &&\
    pip3 install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "server.py" ] 