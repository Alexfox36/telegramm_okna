FROM python:3.11-slim

COPY requirements.txt requirementstxt
RUN pip install -r requirements.txt
COPY . .
RUN npm build

CMD ["python", "main2.py"]