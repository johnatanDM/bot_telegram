import re

def issue_jira_dump(jira, bot, message):
    match = re.match(r'.+ +.+->.+', message.text)
    if match:
        titulo = message.text[6:]
        usuario = message.from_user.id
        fields = {
            'project': {
                'key': "ADDBDD"
            },
            'summary': 'Dump: %s' % titulo,
            'description': '%s' % usuario,
            'issuetype': {
                'name': "Task"
            }
        }
        jira.issue_create(fields)
        bot.reply_to(message,"Seu Dump foi registrado no nosso JIRA")
        bot.send_message(887248892, ("Fazer dump: %s" % titulo))
    else:
        bot.reply_to(message, "Por favor me informe o seu dump como no exemplo: \n \"/dump Sistema Ambiente_origem -> Ambiente_destino\"")

def issue_jira_sqlhelp(jira, bot, message):
    titulo = message.text[9:]
    usuario = message.from_user.first_name + ' ' + (message.from_user.last_name or '')
    fields = {
        'project': {
            'key': "ADDBDD"
        },
        'summary': 'SQLHelp: %s' % titulo,
        'description': '%s' % usuario,
        'issuetype': {
            'name': "Task"
        }
    }
    jira.issue_create(fields)
    bot.reply_to(message,"O DBA já foi avisado e assim que possível irá lhe atender.")
    bot.send_message(887248892, ("SQLHelp: %s, %s" % (titulo, usuario))) #johnatan
    bot.send_message(103309575, ("SQLHelp: %s, %s" % (titulo, usuario))) #adolfho

def issue_jira_sqltune(jira, bot, message):
    titulo = message.text[9:]
    usuario = message.from_user.first_name + ' ' + (message.from_user.last_name or '')
    fields = {
        'project': {
            'key': "ADDBDD"
        },
        'summary': 'SQLTune: %s' % titulo,
        'description': '%s' % usuario,
        'issuetype': {
            'name': "Task"
        }
    }
    jira.issue_create(fields)
    bot.reply_to(message,"O DBA já foi avisado e assim que possível irá lhe atender.")
    bot.send_message(887248892, ("SQLTune: %s, %s" % (titulo, usuario))) #johnatan
    bot.send_message(103309575, ("SQLTune: %s, %s" % (titulo, usuario))) #adolfho

def issue_jira_novo_relogio(jira, bot, message):
    match = re.match(r'.+(?:\d{1,3}\.){3}\d{1,3}.+', message.text)
    if match:
        titulo = message.text[14:]
        usuario = message.from_user.id
        fields = {
            'project': {
                'key': "ADDBDD"
            },
            'summary': 'Cadastrar IP relógio: %s' % titulo,
            'description': ('%s' % usuario),
            'issuetype': {
                'name': "Task"
            }
        }
        jira.issue_create(fields)
        bot.reply_to(message,"Sua requisição foi registrado no nosso JIRA")
    else: 
        bot.reply_to(message, "IP inválido")

def resposta_jira_dump(resposta_jira):
    usuario = resposta_jira["issue"]["fields"]["description"]
    mensagem = "O %s terminou" % resposta_jira["issue"]["fields"]["summary"]
    return mensagem, usuario