FROM python:3.5

COPY . /prod
WORKDIR /prod

RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD ["python3", "service.py"]