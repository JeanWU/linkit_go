from ubuntu:14.04

maintainer Teng-Yi Huang

RUN apt-get update && apt-get install -y curl build-essential python-dev

# Install miniconda to /miniconda

RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh
RUN bash Miniconda3-4.0.5-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-4.0.5-Linux-x86_64.sh
RUN echo "export PATH=/miniconda/bin:$PATH" >> /etc/bash.bashrc
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda


# install nginx
run apt-get install -y nginx supervisor

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

run apt-get autoremove
add ./app/requirements.txt /home/docker/code/
#add ./app/conda-requirements.txt /home/docker/code/
#RUN conda install --yes --file /home/docker/code/conda-requirements.txt
RUN pip install -r /home/docker/code/requirements.txt
#RUN pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
#RUN conda install --yes -c travis uwsgi=2.0.2
#RUN conda install -y -c simpleitk simpleitk=0.9.1

add . /home/docker/code/

run python /home/docker/code/app/manage.py collectstatic --noinput
RUN apt-get remove -y curl build-essential python-dev


expose 80
#expose 443
#expose 1688
cmd ["supervisord", "-n"]
