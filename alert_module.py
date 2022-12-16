import requests
from datetime import timedelta

def send_tg_message (message_text, token, chat_id) :

    telegram_request = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=-100{chat_id}&text={message_text}'

    response = requests.get(telegram_request) 

    if response.status_code == 200 :
        return ("success")
    else :
        return (response.text)

def t_delta(delta):
    td = timedelta(seconds=delta)
    result = "All clear after"
    result += f" {td.days}d" if td.days else ""
    result += f" {td.seconds // 3600}h" if td.seconds // 3600 else ""
    result += f" {td.seconds // 60 % 60}m" if td.seconds // 60 % 60 else ""
    result += f" {td.seconds % 60}s" if td.seconds % 60 else ""
    return(result)
