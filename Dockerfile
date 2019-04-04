FROM python

WORKDIR /app

COPY ./main.py ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python", "-u", "main.py"]
