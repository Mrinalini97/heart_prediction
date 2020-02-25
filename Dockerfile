
FROM python 3.6

LABEL maintainer = "Mrinalini <mrinalini.m97@gmail.com>"

#create a user. (optional while you are learning docker concepts but neccessary while you deploy in kubernetes)

RUN useradd -u 1006 -ms /bin/bash mri

COPY . /app

WORKDIR /app

RUN chown -R 1006:1006 /app

#download all requirements(libraries) in requirements.txt

RUN  pip3 install -r requirements.txt 

#Exposing the port 

EXPOSE 9878

USER 1006

#command that you want your docker to run as soon as it spins up

CMD ["python", "app.py"]