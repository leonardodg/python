# Install base
> Install Python 3.11 Linux - Debian
```
$ apt-get update -y
$ apt-get install git curl build-essential -y
$ apt-get install gcc make default-libmysqlclient-dev libssl-dev -y
$ apt-get install python3.11-full python3.11-dev -y
```

# Check version
## Verificar versão do python instalada
> Python 2
```
$ python --version
```
**OR**
> Python 3
```
$ python3 --version 
$ python3 -V
```

# Virtual environment

## Dependencia lib python3 venv
> Criar ambiente virtual em Python3 
> Faz com que o editor saiba onde as biblioteca estas instaladas
```
$ apt-get install python3-venv
```

> Criar modulo ambientte virtual venv
> obs: ultimo parametro nome da pasta ( ambiente ) 
> 	-m modulo
> 	venv paramentro do comando
>  Retorno - Deve criar uma pasta venv no diretorio raiz do projeto
```
$ python3 -m venv venv
```

## Ativar Ambiente virtual
```
$ source venv/bin/activate
```
**OR** 
```
$ . venv/bin/activate
```

> verificar qual python estou utilizando no ambiente virtual 
> Retuna a pasta de instalação do python
```
$  which python
```
## Desativar ambiente virtual
$ deactivate 

# Teste RUN
> Criar arquivo main.py diretorio do projeto 
> File main.py
```
print(1+1)
```
# Run test
> Return result by print 
```
$ python main.py
```