# sui-node-alert
The python script simply checks whether your node is synced with the Sui blockchain and if your node's version is the same as the Sui Testnet &amp; Devnet version. 

## Installation
```
mkdir sui-alert
cd sui-alert
```
Download below files into the `sui-alert` directory.
* [sui-sync-alert.py](https://github.com/GateOmega/sui-node-alert/blob/main/sui-sync-alert.py) - The python script periodically checks the transaction count on the Sui blockchain and your node, and sends an alert via Telegram if the transaction count on your node is more than a certain threshold that you set.
* [alert-config.cfg](https://github.com/GateOmega/sui-node-alert/blob/main/alert-config.cfg) - Settings and configuration
* [alert.service](https://github.com/GateOmega/sui-node-alert/blob/main/alert.service) - Service


## Configuration
Before using `alert-config.cfg` you should collect the following information to replace the variables present in the configuration file. Update the information in the config file with your own information. 
```
nano alert-config.cfg
```

* YOUR_TELEGRAM_TOKEN: The API token for the Telegram bot. [How to create Telegram Bot?](https://github.com/GateOmega/sui-node-alert/blob/main/telegram.md)
* YOUR_CHAT_ID: The chat ID of the Telegram chat where the bot will send messages. [How to find Chat ID?](https://github.com/GateOmega/sui-node-alert/blob/main/telegram.md)
* YOUR_NODE_NAME: The name of the monitored node.
* YOUR_NODE_IP: The IP of the monitored node. 
* THRESHOLD : The threshold variable is a configuration parameter that specifies the maximum difference between the number of transactions on the Sui blockchain and the number of transactions on the monitored node that is allowed before an alert is triggered.


Important! 
> [sui] section in cfg file: You should only keep (either "Testnet" or "Devnet") that you want to receive alerts for, and comment out the other section. This will ensure that only alerts for the selected network are sent.

## Run the Script

#### Running the script as a daemon:

Simply download [alert.service](https://github.com/GateOmega/sui-node-alert/blob/main/alert.service) file.
```
wget https://github.com/GateOmega/sui-node-alert/blob/main/alert.service
```
Update <YOUR_NODE_NAME>, <USER> and change WorkingDirectory=/PATH/TO/sui-alert/`  path. 




## Create a service file


