FROM ubuntu:latest

COPY ./app /app/

WORKDIR /app

#COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 

#RUN pip install -r /app/requirements.txt 



#EXPOSE 8888

#CMD [ "/bin/bash", "-c", "jupyter lab --ip='0.0.0.0' port=8888 --no-browser --allow-root"]