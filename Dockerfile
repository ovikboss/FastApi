FROM python:3.12

WORKDIR /App

COPY . /App

COPY requirements.txt .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python", "./App/app.py"]