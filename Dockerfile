FROM python:3

WORKDIR /usr/src/app

COPY requirement.txt /usr/src/app
RUN pip install --no-cache-dir -r requirement.txt
COPY . /usr/src/app
CMD [ "python", "app.py" ]
EXPOSE 5000

FROM nginx:latest
WORKDIR /usr/src/app
COPY nginx.conf /etc/nginx/nginx.conf
COPY server.crt /etc/nginx/server.crt
COPY server.key /etc/nginx/server.key