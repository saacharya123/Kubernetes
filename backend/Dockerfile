FROM python:3.10
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 9000
CMD ["python", "app.py"]
