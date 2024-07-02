FROM python:3.10
WORKDIR /code/frontend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]