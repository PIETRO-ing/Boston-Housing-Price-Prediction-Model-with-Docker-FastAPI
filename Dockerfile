FROM ubuntu:latest

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python3 python3-pip 

RUN pip install --no-cache-dir -r /app/requirements.txt 

COPY ./app /app/

EXPOSE 8888

CMD [ "/bin/bash", "-c", "jupyter lab --ip='0.0.0.0' port=8888 --no-browser --allow-root"]