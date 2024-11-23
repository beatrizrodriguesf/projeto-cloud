FROM python:3.11

WORKDIR ./api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "8000"]