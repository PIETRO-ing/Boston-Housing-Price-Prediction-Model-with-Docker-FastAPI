FROM python:3.9-slim

COPY ./app /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]