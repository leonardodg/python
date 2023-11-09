# Install extra
> Instalar pacotes Linux - Debian
```
$ apt-get install git curl build-essential dkms perl wget -y
$ apt-get install gcc make default-libmysqlclient-dev libssl-dev -y
$ apt-get install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
                libncurses5-dev libncursesw5-dev \
                xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```
  
# PIP
> listar modulos instalados
```
$ pip freeze
```

> instalar modulos instalados
> Obs.: Ambiente virtual ativo
```
$ pip freeze -r .\requirements.txt
```

> Atulizar PIP
```
$ pip install pip --upgrade
$ python -m pip install --upgrade pip
```

# Install lib Python ( Extra ) 
> Exemplo comando install lib python
```
$ pip install name-lib
```

<!-- # Pyenv
> Seguir instruções do Pyenv
```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
``` -->


Verificar local instalação do python
> powerShell
 gcm python -Syntax

 > verificar qual python estou utilizando no ambiente virtual 
> Retuna a pasta de instalação do python
```
$  which python
```