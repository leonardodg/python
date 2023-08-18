FROM python:3.11-alpine

# Gravar Files *.pyc no disco: 1 = no
ENV PYTHONDONTWRITEBYTECODE 1

# Não fazer Buffer 
ENV PYTHONUNBUFFEERED 1

WORKDIR /usr/src/app

COPY src /usr/src/app/
COPY  scripts /scripts

# Command Python
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /usr/src/app/requirements.txt

# Create USER in Linux
RUN adduser --disabled-password --no-create-home user-py && \
    chown -R user-py:user-py /venv && \
    chown -R user-py:user-py /usr/src/app && \
    chown -R user-py:user-py /scripts && \
    chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para user-py
USER user-py

# Executa o arquivo scripts/docker-entrypoint.sh
ENTRYPOINT  ["docker-entrypoint.sh"]