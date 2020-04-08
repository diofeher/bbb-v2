BBBot V3
===============
Cada config é referente a uma instance executada.
Config0 para RodarWindows0
Config 1 para RodarWindows1

Use o Multi Instance Watcher para somar todos Votos !
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

TREINAMENTO DO ALGORITMO
========================

Esse bot é feito utilizando o SIFT do OpenCV. Algumas captchas não vão funcionar corretamente pois não temos todas as imagens do banco. Para ajudar nesse mapeamento, faça o seguinte:

1) Ele vai baixar um captcha com um nome. Esse arquivo vai ser salvo em `images/<simbolo>.png`
2) O programa vai cortar o captcha em 5 pedaços e renomear cada pra: images/<simbolo>_numero.png
3) É só puxar a versão correta pra images_individual como <simbolo>_numero.png que o programa vai identificar esse ícone
4) Abra um pull request para atualizarmos aqui :)

Dev
================
Bot original = https://github.com/diofeher/bbb-v2
  - [JAG](https://twitter.com/ze_helo)
  - [Nicolas França](https://twitter.com/NicolasFrancaX/)
  - [Rafael Chaguri](https://twitter.com/RafaelChaguri)
  
