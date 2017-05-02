from fareoffice/python3



RUN rm -rf /usr/bin/python
RUN ln -s /opt/rh/python33/root/usr/bin/python3 /usr/bin/python
RUN ln -s /opt/rh/python33/root/usr/bin/pip /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install python-redmine flask
