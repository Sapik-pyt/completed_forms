FROM python:3

WORKDIR /src/server/forma
COPY . /
COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/src/server/forma/entrypoint.sh"]