FROM  python:3.5
ADD ./mnist /code
WORKDIR /code
RUN pip install --default-timeout=2000 --no-cache-dir -r requirements.txt
CMD ["python","/code/package/init1.py"]