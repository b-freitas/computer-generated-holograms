# Computer-generated-holograms

## Description

This project is an web application in Python 3 containing source code to make holograms used in gaussian beams to generate OAM beams. 

Created by master's degree students of the NNOAM Group from FT UNICAMP - BRAZIL.

## How To Use

### Setting the enviroment

1. Após concluir o clone do projeto, abra o terminal e navegue até a raiz do repositório.

2. Para iniciar a configuração do ambiente que é necessário à execução da aplicação, crie um ambiente virtual usando o comando:

```terminal
python3 -m venv env
```

3. Ative o ambiente virtual que fará com que sua instalação python seja isolada da instalação presente no seu sistema operacional. Para isso, rode o seguinte comando:

```terminal
source env/bin/activate
```

### Installing dependencies

4. Para instalar as dependências utilizados pelo projeto, digite:

```terminal
python3 -m pip install -r requirements.txt
```

5. Configure a variável de ambiente do app no servidor web:

```terminal
$ export FLASK_APP=src/app.py
```

6. Se você estiver no Windows, digite o comando abaixo no prompt:

```terminal
> set FLASK_APP=src/app.py
```

### Running the web application

Após realizar todas as etapas anteriores, você pode iniciar a aplicação rodando o comando:

```terminal
$ flask run
```

A aplicação será iniciada após executar o comando acima. Não feche o terminal! 
Observe que a saída no terminal deve se parecer com o seguinte:

    Serving Flask app "src/app.py"
    Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    Debug mode: off
    Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


