FROM python:3.8

WORKDIR /wc_src

COPY . .

RUN echo $(ls -l .)
RUN echo $(pwd)

CMD [ "python", "-m", "prompt" ]