# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder
LABEL authors="AgniaEndie"
WORKDIR /FoxStudios-PyBid

COPY requirements.txt /FoxStudios-PyBid
#RUN --mount=type=cache,target=/root/.cache/pip \
#    pip3 install -r requirements.txt
RUN pip3 install -r requirements.txt
COPY . /FoxStudios-PyBid

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
