FROM python:3.8.3
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT python /app/app.py