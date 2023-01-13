FROM continuumio/miniconda
USER root

RUN conda install python=3.7

COPY . .


RUN pip install -r requirements.txt


EXPOSE  5555
CMD [ "python", "./main.py" ]
