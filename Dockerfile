FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
WORKDIR /atucasa
# RUN pip install pipenv
# RUN pipenv install --system
COPY requirements.txt .
# RUN apt install wkhtmltopdf -y
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8933
