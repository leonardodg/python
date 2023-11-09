# TEMP STAGE
FROM python:3.11-slim as build
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential gcc 

WORKDIR /usr/app
COPY requirements.txt .

# Gravar Files *.pyc no disco: 1 = no
ENV PYTHONDONTWRITEBYTECODE 1

# Não fazer Buffer 
ENV PYTHONUNBUFFEERED 1

# Command Python
RUN python -m venv /usr/app/venv && \
    /usr/app/venv/bin/pip install --upgrade pip && \
    /usr/app/venv/bin/pip install --no-cache-dir -r /usr/app/requirements.txt
ENV PATH="/usr/app/venv/bin:$PATH"

# FINAL STAGE
FROM python:3.11-slim@sha256:f89d4d260b6a5caa6aa8e0e14b162deb76862890c91779c31f762b22e72a6cef

# Create USER in Linux
RUN groupadd -g 999 python && \ 
    useradd -m -u 999 -g python python

WORKDIR /usr/app
COPY --chown=999:999 --from=build /usr/app/venv ./venv
COPY --chown=999:999 src /usr/app/
COPY --chown=999:999 scripts /scripts

RUN chmod -R +x /scripts

# Muda o usuário para python
USER 999

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/usr/app/venv/bin:$PATH"

# Executa o arquivo scripts/docker-entrypoint.sh
ENTRYPOINT  ["docker-entrypoint.sh"]