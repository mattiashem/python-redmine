from fareoffice/python3



RUN /usr/bin/pip3.6 install --upgrade pip
RUN /usr/bin/pip3.6 install python-redmine flask
RUN mkdir /code
ADD code/run.py /code/run.py
RUN chmod 700 /code/run.py


CMD python3.6 /code/run.py
