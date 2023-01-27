# Import modules and functions

import re, time, json, requests, configparser
from datetime import datetime, timedelta

# Load configuration from sui_alert.cfg file
config = configparser.ConfigParser()
config.read('alert-config.cfg')

# Get Telegram bot token and chat ID from configuration
token = config['tg_config']['token']
chat_id = config['tg_config']['chat_id']

# Get your node name and URL from configuration
node_name = config['node_config']['node_name']
node_url = config['node_config']['node_url']

# Get Sui blockchain URL, threshold and banner from configuration
threshold = config['sui']['threshold']
network = config['sui']['network']
sui_url = config['sui']['sui_url']

# Other Variables
headers = {'Content-Type': 'application/json'}
payload_rpc_discover = json.dumps({"jsonrpc": "2.0","id": 1,"method": "rpc.discover"})
payload_txs = json.dumps({"jsonrpc": "2.0","id": 1,"method": "sui_getTotalTransactionNumber"})

# Function that sends a message through the Telegram API. 
def send_tg_message (message_text, token, chat_id) :

    telegram_request = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=-100{chat_id}&text={message_text}'

    response = requests.get(telegram_request) 

    if response.status_code == 200 :
        return ("success")
    else :
        return (response.text)
    
# Function calculates a time delta in seconds. 
def t_delta(delta):
    td = timedelta(seconds=delta)
    result = "All clear after"
    result += f" {td.days}d" if td.days else ""
    result += f" {td.seconds // 3600}h" if td.seconds // 3600 else ""
    result += f" {td.seconds // 60 % 60}m" if td.seconds // 60 % 60 else ""
    result += f" {td.seconds % 60}s" if td.seconds % 60 else ""
    return(result)

# Function to get Sui blockchain version
def sui_vcheck():
    response = requests.request("POST", sui_url, headers=headers, data=payload_rpc_discover)
    found = re.search(r'"version":"(.+?)"}', str(response.text))
    sui_version = found.group(1)
    return sui_version

# Function to get total transaction count on Sui blockchain
def sui_txs():
    response = requests.request("POST", sui_url, headers=headers, data=payload_txs)
    found = re.search(r'"result":(.+?),', str(response.text))
    sui_txs = found.group(1) 
    return sui_txs

# Function to get your node version
def node_vcheck():
    response= requests.request("POST", node_url, headers=headers, data=payload_rpc_discover)
    found = re.search(r'"version":"(.+?)"}', str(response.text))
    node_version = found.group(1)
    return node_version

# Function to get total transaction count on your node
def node_txs():
    response= requests.request("POST", node_url, headers=headers, data=payload_txs)
    found = re.search(r'"result":(.+?),', str(response.text))
    node_txs = found.group(1) 
    return(node_txs)


# Initialize state variable to 0
state = 0

# Infinite loop
while True:
    try:
        # Retrieve the URL of the monitored node, the version of the Sui testnet/devnet, the version of the monitored node, and the number of transactions processed by each node
        node_url = config['node_config']['node_url']
        sui_version = sui_vcheck()
        my_node_version = node_vcheck()
        node_tx_s = int(node_txs())
        sui_tx_s = int(sui_txs())
    except Exception as error:
        dt_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        send_tg_message(f"{dt_now}\n\U00002757 Check if your node is up and running \n{error}", token, chat_id)
        time.sleep(600)
        continue

    # Compare transaction difference to the threshold value.
    if sui_tx_s - int(threshold) < node_tx_s:
        if state == 1:
            dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            second = datetime.now().timestamp()
            delta = second - first
            send_tg_message(f"ALERT! - {dt}\n\nYour Node: {node_name}\nNetwork: {network}\n\nIs Synced: YES\U0001F4A7 \n\nSui Txs: {sui_tx_s} \nNode Txs: {node_tx_s} \
                   \nSui Version: {sui_version} \nNode Version: {my_node_version} \n\n{t_delta(delta)}", token, chat_id)
            state = 0
        time.sleep(300)

    else:
        if state == 0 :
            dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            first = datetime.now().timestamp()
            send_tg_message (f"ALERT! - {dt}\n\nYour Node: {node_name}\nNetwork: {network}\n\nIs Synced: NO\U00002757\n\nSui Txs: {sui_tx_s} \nNode Txs: {node_tx_s} \
                  \nSui Version: {sui_version} \nNode Version: {my_node_version}", token, chat_id)
            state = 1
        time.sleep(120)
