FROM python:3

WORKDIR /usr/src/app

COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

COPY . .

CMD [ "python", "./main.py" ]

FROM nginx:latest as production-stage
WORKDIR /usr/src/app
COPY nginx.conf /etc/nginx/nginx.conf
COPY client.csr /etc/nginx/client.csr
COPY client.key /etc/nginx/client.key