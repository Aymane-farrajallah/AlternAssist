FROM python:3.14.4-slim

WORKDIR /main

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app" , "--host" ,"0.0.0.0" ,"--port" ,"8000"]