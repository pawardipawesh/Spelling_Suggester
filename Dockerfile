# Update the sources list
FROM ubuntu:18.04
LABEL maintainer="Sanjeev Kumar Rai / Dipawesh Pawar"

# install useful system tools and libraries
RUN apt-get update && apt-get install -y libfreetype6-dev && \
    apt-get install -y libglib2.0-0 \
                       libxext6 \
                       libsm6 \
                       libxrender1 \
                       libblas-dev \
                       liblapack-dev \
                       gfortran \
                       libfontconfig1 --fix-missing

# install Python and pip package manager
RUN apt-get install -y python3.6 \
                       python3.6-dev \
                       python3-pip

COPY ./requirements.txt /
COPY . /app
WORKDIR /app
RUN pip3 install -r ./requirements.txt
