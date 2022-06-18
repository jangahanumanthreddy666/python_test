FROM python 
# WORKDIR /usr/src/app
# RUN pip install opencv-python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/
CMD [ "python", "/usr/src/app/main.py" ]