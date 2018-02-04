FROM frolvlad/alpine-python3
WORKDIR /srv/app

# Install Python's Natural Language Toolkit and its dependencies
RUN apk update
RUN apk add build-base gcc abuild binutils binutils-doc gcc-doc python3-dev lapack lapack-dev gfortran
RUN pip3 install numpy && pip3 install scipy && pip3 install scikit-learn \
    && pip3 install wikipedia && pip3 install nltk

# Download required Natural Language Toolkit data packages
COPY scripts/nltk_downloads.py scripts/nltk_downloads.py
RUN python3 scripts/nltk_downloads.py

# The unwiki package doesn't appear to be available via pip, so get it from GitHub
RUN mkdir -p /usr/lib/python3.6/site-packages/unwiki
RUN curl -L https://raw.githubusercontent.com/fitnr/unwiki/master/unwiki/__init__.py > /usr/lib/python3.6/site-packages/unwiki/__init__.py

# Copy the demo Python scripts
COPY nlpdemo nlpdemo
COPY nlp.py nlp.py