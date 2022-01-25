FROM python:3.8-alpine
ADD . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirement.txt

CMD python app.py