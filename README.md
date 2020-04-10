BBBot + OpenCV
===============

Paredão dessa semana:
```
Babu - 1
Flayslane - 2
Marcela - 3
```

Você precisa editar o arquivo `config.json` com as seguintes informações:

Se tiver somente uma conta, use o seguinte formato:

```
{
  "participant": 3,
  "contasEmParalelo": 1,
  "credentials": [
    {
      "username": "email-da-sua-conta@globo.com",
      "password": "12345678"
    }
  ]
}
```

Se tiver somente mais de uma conta, use o seguinte formato:

```
{
  "participant": 3,
  "contasEmParalelo": 1,
  "credentials": [
    {
      "username": "jackiechan@globo.com",
      "password": "12345678"
    },
    {
      "username": "brucelee@globo.com",
      "password": "12345678"
    }
  ]
}
```



PARTICIPANTE se refere à posição do participante. Caso ele seja o primeiro da lista, colocar um 1,
o do meio 2 e o último 3.


INSTALAÇÃO NO WINDOWS
=====================


1) Instale a versão 3.7.1 do Python https://www.python.org/downloads/release/python-371/
2) Rode o arquivo `instalador-windows.bat` para instalação de programas auxiliares
3) Rode o bot com `rodar-windows.bat`. Um prompt será mostrado perguntando suas informações (conta/senha globo, participante que quer votar)
4) Caso o bot dê problema, tente votar manualmente primeiro com sua conta só pra depois tentar utilizar o bot.
5) Caso o erro persista, só me mandar uma mensagem no https://twitter.com/diofeher


INSTALAÇÃO EM MAC E LINUX
=========================

Instale o Python3

Depois de instalar, rode os seguinte comandos:

```
pip3 install -r requirements.txt
```

Normalmente o Python2 já vem instalado nessas máquinas, então você precisa instalar o Python3 e ficar com as duas instalações.

Rodando o bot:

```
python3 src/bbb.py
```


TREINAMENTO DO BANCO DE DADOS
=============================

Esse bot é feito utilizando o SIFT do OpenCV. Algumas captchas não vão funcionar corretamente pois não temos todas as imagens do banco. Para ajudar nesse mapeamento, faça o seguinte:

```
export PYTHONPATH="$(pwd):$PYTHONPATH"
python3 src/classifier/download_images.py
```

Aperte ctrl+c depois de ter baixado alguns captchas. O comando seguinte vai quebrar as imagens em 5 imagens diferentes.

```
python3 src/classifier/break_images.py
```

O comando seguinte vai te permitir renomear a imagem:

```
python3 src/classifier/classify.py
```

Depois de ter terminado, coloque todas as imagens que estão em `classified` no `images_individual`


Série de vídeos explicando como o bot foi feito
======================================================

No meu canal do youtube deixei uma série de vídeos explicando passo a passo como o bot foi feito, desde a parte da quebra do captcha até a parte de interação com o servidor de captcha e o de votações.

https://www.youtube.com/watch?v=ABBy8vPZ_aU&list=PLKGzzk4_BYu0XkTs_xEyvMLolL-hndSHS


Link do Discord
================

https://discord.gg/uJkyKUX


Licença
=========

Bot foi feito somente para fins de estudo. Sinta-se livre pra utilizar. Não temos candidato preferido, então o bot é feito para todas as torcidas.

Problemas Comuns
=================

  - [PIP não é reconhecido como comando](https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/)
  - [Python não é reconhecido como comando](https://twitter.com/diofeher/status/1244586721355988992)
  - Sintaxe não é válida - Instalar o Python 3.7.1 (você provavelmente tem o Python 2 instalado)
  - No module named requests - Você precisa rodar o `instalador-windows.bat`

Total de Votos
==============

Se você precisa de auditoria do total de votos, todos os votos válidos serão computados no arquivo `votes.log`.


Contribuidores
================

  - [Nicolas França](https://twitter.com/NicolasFrancaX/)
  - [Rafael Chaguri](https://twitter.com/RafaelChaguri)
  - [Jose Arthur](https://github.com/josearthur)
