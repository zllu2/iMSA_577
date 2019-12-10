# Dockerfile to set autograder environment.
FROM jupyter/scipy-notebook:latest

MAINTAINER Linden Lu <zllu2@illinois.edu>

USER root

# Install nose
RUN pip install nose

# Install nbgrader
RUN pip install --upgrade pip
RUN pip install nbgrader --ignore-installed
RUN pip install pytest

# Install and enable extensions
#RUN jupyter nbextension install --sys-prefix --py nbgrader
#RUN jupyter nbextension enable --sys-prefix --py nbgrader
#RUN jupyter serverextension enable --sys-prefix --py nbgrader

# set environment
USER $NB_USER

# Setup work directory for backward-compatibility
#RUN mkdir /home/$NB_USER/work

USER root

# Setup directories where files will be stored
RUN mkdir /grader
COPY source /grader/source/
COPY nbgrader_config.py /grader/

#Submissions directory, is this needed?
#RUN mkdir -p /shared/submission/

#Copy Grader Files
COPY execute_grader.sh /grader/
COPY exporter.py /grader/

# read permission: we may need to read from datasets 
# write permission: store .pyc files and perhaps other things
# excute permissions: Run entrypoint
#
RUN chmod a+rwx -R /grader/

# Setup EntryPoint
WORKDIR /grader
ENTRYPOINT ["./execute_grader.sh"]
