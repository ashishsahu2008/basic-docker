FROM python:3.6.4
COPY . /usr/src/app
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
CMD ["python", "/usr/src/app/api.py"]
EXPOSE 80
