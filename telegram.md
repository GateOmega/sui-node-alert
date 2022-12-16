## How to create Telegram Bot?

To create an API token for a Telegram bot, you will need to create a bot using the Telegram Bot Father. 

1. Open a chat with the Bot Father by searching for @BotFather in Telegram or by clicking this link: https://t.me/BotFather
2. Send the command /newbot to the Bot Father to create a new bot.
3. The Bot Father will ask you to choose a name for your bot. Choose a name and send it to the Bot Father.
4. The Bot Father will then ask you to choose a username for your bot. Choose a username that ends with bot (e.g. my_bot) and send it to the Bot Father.
5. The Bot Father will then generate an API token for your bot and send it to you in the form of a message. This API token will be used to authenticate your bot when making API requests.
6. You can now add the bot 

> Once you have the API token for your bot, you can use it in your code to authenticate your bot when making API requests to the Telegram API. Note that the API token for your bot is a secret and should be kept confidential. Do not share it with anyone or include it in public code repositories.

## Create a new channel in Telegram and add your bot as an administrator:

1. Open the Telegram app on your device and log in to your account.
2. Tap the "Menu" icon (three horizontal lines) in the top left corner of the screen, and then tap "New Channel".
3. Enter a name and description for your channel, and select whether you want it to be public or private.
4. Tap "Create" to create your new channel.
5. In the channel settings, tap "Add Administrators" and then search for your bot using its username.
6. Tap on the bot's name and then tap "Add as Administrator" to add the bot as an administrator of the channel.
> Now you can use your bot to send messages or perform other actions in the channel.

## How to find your chat ID? (channel ID)

In Telegram, every chat (including private and public channels) has a unique identifier called a chat ID. The chat ID is a numerical value that is used to identify a specific chat.

To find the chat ID of a channel or chat room in Telegram, you can follow the steps as described below:

1. Go to https://web.telegram.org and log in to your Telegram account.
2. Navigate to the channel or chat room for which you want to find the chat ID.
3. Look at the URL of the page. The chat ID is the numerical value that appears after the "#" symbol in the URL.
For example, in the URL https://web.telegram.org/z/#-1567031322, the chat ID would be 1567031322.

> Once you have the chat ID, you can use it to send messages or perform other actions through the Telegram API or a third-party library. It's also useful for setting up alerts or notifications from your server or other external sources.
