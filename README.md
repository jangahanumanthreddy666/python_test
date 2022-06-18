# python_test
Python Program for writing new videos from one directory to another directory with some Modifications: 
Like convert video an angle of 90 degrees, and change Gray Color..
Steps:-
1) Create Python file like main.py file
    a) Install Plug in Opencv
    CMD:- pip install opencv-python


2) After open Path(input Directory Path), The Path Containing all Video Files.
    path = "workspace"


3) read the above Directory to get all video files
        dir_list = os.listdir(path)
        x=len(dir_list)

   Here os is a module so, we want to import os module like
        import os

4) After iterating the Files to Write the new Videos into new Directory.
        out.write(frame)

5) write the Video Converting Line : 
       out = cv.VideoWriter(p4, fourcc, 20.0, (300,  180))


6) We can also play the videos what you have to read.
    ret, img=cap.read()
    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    cv.imshow("GrayColor", gray)
-------------------------------------------------------------------------------------------------
Dockerfile for this Program
Steps:
1) Write a Dockerfile with command 'vi Dockerfile'
2)Inside Dockerfile Follow the Layers to run Python file
    a)take a base python base image from Dockerhub
        CMD:- FROM python
    b)copy the requirements.txt 
        CMD:- COPY requirements.txt ./
    c) Install the requirements.
        CMD:- RUN pip install --no-cache-dir -r requirements.txt
    d) copy the files to docker image using COPY command
        CMD:- COPY . /usr/src/app/
    e) Run the main.py file contineously using CMD command
        CMD:- CMD [ "python", "/usr/src/app/main.py" ]
3) Finally build the image below command
        CMD:- docker build -t py_test:1 .
4) Run the Docker Container
        CMD:- docker run -d py_test:1
5) Check the containers 
        CMD:- docker ps -a
