FROM python:3.8

WORKDIR /wc_app

COPY . /wc_app

RUN echo $(ls -l .)
RUN echo $(pwd)

CMD [ "python", "-m", "prompt" ]