BBBot + OpenCV = BBB-V2
===============

Paredão dessa semana:
Babu - 1
Gabi - 2
Thelma - 3


Você precisa modificar o arquivo `config.json` para poder logar no site da Globo e escolher o participante que vai ser votado:

```
{
  "participant": 2,
  "credentials": {
      "username": "<seuemail>@globo.com",
      "password": "123456789"
  }
}
```


INSTALAÇÃO NO WINDOWS
=====================

1) Instale a versão 3.7.1 do Python hhttps://www.python.org/downloads/release/python-371/
2) Rode o arquivo `instalador-windows.bat` para instalação de programas auxiliares
3) Rode o bot com `rodar-windows.bat`.
4) Caso o bot dê problema, tente votar manualmente primeiro com sua conta só pra depois tentar utilizar o bot.

INSTALAÇÃO EM MAC E LINUX
=========================

Instale o Python3 e o Node.JS

Depois de instalar essas duas dependências, rode os seguinte comandos:

```
pip3 install -r requirements.txt
```

Normalmente o Python2 já vem instalado nessas máquinas, então você precisa instalar o Python3 e ficar com as duas instalações.

Rodando o bot:

```
python3 bbb.py
```

TREINAMENTO DO ALGORITMO
========================

Esse bot é feito utilizando o SIFT do OpenCV. Algumas captchas não vão funcionar corretamente pois não temos todas as imagens do banco. Para ajudar nesse mapeamento, faça o seguinte:

1) Ele vai baixar um captcha com um nome. Esse arquivo vai ser salvo em `images/<simbolo>.png`
2) O programa vai cortar o captcha em 5 pedaços e renomear cada pra: images/<simbolo>_numero.png
3) É só puxar a versão correta pra images_individual como <simbolo>_numero.png que o programa vai identificar esse ícone
4) Abra um pull request para atualizarmos aqui :)


Troubleshooting
================
Caso o comando Python não seja achado:

`export PATH="<local da instalacao do Python>:$PATH"`
