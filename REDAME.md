# Docker - Python - PostgreSQL
CONTAINER PYTHON COM POSTGRESQL E ADMINER



Não sei programar em python, mas algumas vezes fui obrigado a criar ambientes de “dev” nas empresas em que trabalhei.

Mas, vamos criar um ambiente dockerizado para utilização do python com postgresql.

Também vamos usar o adminer como SGBD para o postgresql.



Vamos criar um Dockerfile para build da aplicação e um docker-compose para iniciarmos os conatiners:



- FROM python:3.6

- ENV PYTHONUNBUFFRERED 1

- RUN mkdir /code

- WORKDIR /code

- ADD requirements.txt /code/

- RUN pip install -r requirements.txt

- ADD . /code/



Com estas configurações já temos as configurações básicas do pyhton, mas pode-se adicionar mais detalhes a imagem. Vide https://hub.docker.com/_/python

Vamos ao docker-compose.yml:



- version: '3.1'

- services:

- db:

- image: postgres

- restart: always

- environment:

- POSTGRES_PASSWORD: Postgres2021!

- web:

- build: .

- command: python manage.py runserver 0.0.0.0:8000

- volumes:

- "- .:/code"

- ports:

- "- 8000:8000"

- "links:"

- "- db"

- adminer:

- image: adminer

- restart: always

- ports:

- "- 8081:8080"



Criamos os serviços “db” e “web” onde: “db” será o banco de dados “postgresql” e “web” o python.

Teremos também o “adminer” para gerenciar o postgresql. Nada impede de trocar por outro SGBD de sua preferência.



Crie um arquivo com nome de “requirements.txt” e coloque as seguintes configurações no mesmo:

- Django

- psycopg2



Feito isto vamos rodar os comandos necessários para “build” e “up” dos containers.

→ docker-compose run web django-admin startproject <nome-projeto> .

→ docker-compose up



Vá até localhost:8000 e veja o python rodando e respectivamente vá até localhost:8081 e veja o adminer rodando.



Neste ponto temos python, postgresql e adminer em um ambiente docker.

