FROM python:3.8.16-slim as base
MAINTAINER Sara Veldhoen <sara.veldhoen@kb.nl>

COPY requirements.txt /

RUN pip install --upgrade pip \
    && pip install -r requirements.txt 

ENV HOME=/usr

RUN groupadd -g 999 user && \
    useradd -r -u 999 -g user user

RUN mkdir /usr/app && chown user:user /usr/app
WORKDIR /usr/app

COPY --chown=user:user wsgi.py wsgi.py
COPY --chown=user:user cst cst/

USER 999
EXPOSE 3350
ENV SCRIPT_NAME=/cst
CMD ["gunicorn", "-b :5001", "wsgi"]
