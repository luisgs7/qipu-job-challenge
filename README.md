## Web App que Possibilita Realizar Operações de Adição e Remoção de Valores em uma Lista Encadeada, desenvolvida em Python

#### 01 - É necessário que se tenha o docker e docker-compose instalado para inicializar o projeto.

#### 02 - Inicialmente crie um arquivo na raiz do projeto com o nome ``` .env ``` e adicione as seguintes informações a ele, estas são variáves de ambientes, que não devem ser versionadas:
```
SECRET_KEY=django-insecure-m6n1s9q@3%@4j-$7!^omy+h9a#8s32ov#_x27ad28p7+11y1i@
DEBUG_APP=True
ALLOWED_HOSTS=*
```

#### 03 - Em seguida realize o build do projeto com o seguinte comando:
```
docker-compose build
```

#### 04 - Para inicializar o projeto, utilize o comando abaixo na raiz do projeto:
```
docker-compose up
```
##### Se preferir pode adicionar o parâmetro ```-d``` no final do comando, para deixar o terminal livre

#### 05 - Para acessar a página web acesse a seguinte url:
```
http://0.0.0.0:8080/
```

## Projeto inicializado

<img src="https://github.com/luisgs7/Qipu-job-challenge/blob/main/screen/qipu.png">

* Este app foi realizado o deploy no heroku, entretanto ele não funciona muito bem, pois os dados são rapidamente perdidos, mas de forma local funciona corretamente, link abaixo:
https://qipu-challenge.herokuapp.com/
