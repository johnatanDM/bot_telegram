import os
import telebot
import requests
import banco_de_dados 
import re
from telebot import types
from conecta import Conexao
from aiohttp import web 
from atlassian import Jira

token = os.getenv("BOT_API_TOKEN")
URL = "https://api.telegram.org/bot{}/".format(token)
jiraurl = os.getenv("JIRA_URL")
host_database = os.getenv("HOST_DATABASE")
database = os.getenv("DATABASE")
user_database = os.getenv("USER_DATABASE")
pass_user_database = os.getenv("PASS_USER_DATABASE")

def jira(porta):
    jira = Jira(
        url=jiraurl + ':' + porta,
        username='sistema',
        password= os.getenv("JIRA_SENHA_" + porta))
    return jira
bot = telebot.TeleBot(token)

def conectar():
    con=Conexao(host_database,database,user_database,pass_user_database)
    return con

def autorizado(message):
    con=conectar()
    sql=("select 1 from users where id = %s and aprovado = TRUE" % message.from_user.id)
    autorizado = con.consultar(sql)
    if len(autorizado) == 1:
        return True
    else:
        return False

@bot.message_handler(commands=['mecadastra'])
def mecadastra(message):    
    con=conectar()
    sql = ("insert into users values (%s,'%s','%s','%s')" % (message.from_user.id, message.from_user.first_name, message.from_user.username, message.from_user.last_name))
    
    if con.manipular(sql):
        bot.reply_to(message, "inserido com sucesso!!")
        teclado = types.InlineKeyboardMarkup(row_width=1)
        sim = types.InlineKeyboardButton(text=("Sim autorize"), callback_data=("Sim autorize %s, %s" % (message.from_user.username, message.from_user.id)))
        nao = types.InlineKeyboardButton(text=("Não autorize"), callback_data=("Não autorize %s, %s" % (message.from_user.username, message.from_user.id)))
        teclado.add(sim, nao)
        bot.send_message(887248892, ("Autorizar %s %s, %s para usar o Cotequinho_bot?" % (message.from_user.first_name,message.from_user.last_name , message.from_user.id)), reply_markup=teclado)

    else:
        con.rollback()
        bot.reply_to(message, "Não deu! :( ")
    con.fechar()

@bot.callback_query_handler(func=lambda m: True)
def autorize(message):
    autorize = re.match(r'Sim autorize.', message.data) 
    chat_id = message.from_user.id
    if autorize:
        con=conectar()
        sql = ("update users set aprovado = true where id = %s" % chat_id)
        print(con.manipular(sql))
        if con.manipular(sql) :
            print("Autorizado com sucesso!!")
            bot.send_message(887248892, "Autorizado com sucesso!!")
        else:
            print("Não deu pra autorizar! :( ")
            con.rollback()
            bot.send_message(887248892, "Não deu pra autorizar! :( ")
        con.fechar()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """Olá, Eu sou o Cotequinho Bot e já sei fazer algumas coisas! \n
- Você pode pedir Dump para a equipe de Banco de dados assim: \n
/dump Sistema Ambiente_origem -> Ambiente_destino \n
- Você pode pedir para o DBA lhe ajudar em uma consulta assim: \n
/sqlhelp Sistema \n
- Você também pode pedir para cadastrar um novo relógio no banco do ponto assim: \n
/novo_relogio ip: 172.123.123.123 orgao: GMF descricao: GONZAGUINHA MESSEJANA   
""")


@bot.message_handler(commands=['dump'])
def dump(message):
    if autorizado(message):
        banco_de_dados.issue_jira_dump(jira('9090'), bot, message)
    else:
        bot.reply_to(message, "Você não está autorizado a usar esse bot")


@bot.message_handler(commands=['novo_relogio'])
def novo_relogio(message):
    if autorizado(message):
        banco_de_dados.issue_jira_novo_relogio(jira('9090'), bot, message)
    else:
        bot.reply_to(message, "Você não está autorizado a usar esse bot")

@bot.message_handler(commands=['sqlhelp'])
def sql_help(message):
    if autorizado(message):
        banco_de_dados.issue_jira_sqlhelp(jira('9090'), bot, message)
    else:
        bot.reply_to(message, "Você não está autorizado a usar esse bot")

bot.polling()   

