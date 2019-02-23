FROM nginx

LABEL maintainer.fullname="SOGLO Arcadius"
LABEL maintainer.email="rtsoglo@gmail.com"

ENV CODE_DIR /usr/share/nginx/html

COPY webapp/build ${CODE_DIR}/build
COPY webapp/src ${CODE_DIR}/src
COPY webapp/index.html ${CODE_DIR}/index.html

EXPOSE 80

WORKDIR ${CODE_DIR}