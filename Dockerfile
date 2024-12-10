FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

COPY entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

