# bot_telegram
Bot de Telegram com integração com o JIRA

INSTALAÇÃO
Instalar dependencias:
-Python 3.6+
-PyTelegramBotAPI
  pip3 install pyTelegramBotAPI
-Psycopg2
  pip3 install psycopg2
-Aiohttp
  pip install aiohttp
-Atlassian-python-api
  pip install atlassian-python-api
  
  
VARIÁVEIS DE AMBIENTE

Por questão de segurança, o bot utiliza da biblioteca "os" do Python para importar os dados de conexão com o banco de dados bem como os dados de acesso ao Jira e o token da api para bots do Telegram

export BOT_API_TOKEN="(TOKEN DO SEU BOT NO TELEGRAM"
export JIRA_URL="(URL DO SEU SERVIDOR JIRA)"
export JIRA_SENHA='(SENHA DO SEU USUARIO NO JIRA)'
export HOST_DATABASE="(HOST DO SEU BANCO DE DADOS POSTGRESQL)"
export DATABASE='(NOME DO BANCO DE DADOS POSTGRESQL)'
export USER_DATABASE="(USUÁRIO DO SEU BANCO DE DADOS)"
export PASS_USER_DATABASE="(SENHA DO SEU BANCO DE DADOS)"


TOKEN DO BOT PARA TELEGRAM

Para utilizar a API do Telegram para bot você precisa criálo no Telegram. Para isso basta falar com o BotFather com o comando /newbot e responder os dados que ele pede como nome por exemplo.


WEBHOOK RESPOSTA JIRA

Este sistema pode ser dividido em duas partes. A primeira é o próprio Bot com todos os comandos que está programado para responder e interagir. A segunda é um webhook para que o Bot interaja com a API do Jira.
Os passos para configurar um webhook no Jira podem ser encontrados na documentação no site da Atlassian:
https://developer.atlassian.com/server/jira/platform/webhooks/

Para iniciar o nosso webhook basta executar:
python resposta_jira.py


INICIAR O BOT

Para iniciar o nosso bot basta executar:
python bot.py
