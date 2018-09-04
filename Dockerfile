FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --verbose --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./test.py" ]
