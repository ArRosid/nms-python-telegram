# nms-python-telegram
Network Monitoring System using Python and Telegram

This repository contain python script to doing Network Monitoring System using Python and send the notification to the Telegram


<h3>Requirement</h3>
To run this repository, you need some python library installed on your computer.
<ul>
    <li>Python 2.7</li>
    <li>pyping</li>
    <li>telepot</li>
</ul>


<h3>Setup</h3>
<ol>
    <li>Create Telegram bot, this telegram bot will used to notify us if the provisioning on Mikrotik completed. You can follow tutorial on https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0</li>
    <li>Clone this repository</li>
        <ul>
            <li>git clone https://github.com/arrosid/nms-python-telegram.git</li>
            <li>cd nms-python-telegram</li>
        </ul>
    <li>Install requirement library</li>
        <ul>
            <li>virtualenv -p python2 venv</li>
            <li>source venv/bin/activate</li>
            <li>pip install -r requirement</li>
        </ul>
    <li>Edit script.py. Fill the <i>'your_token'</i> and <i>'your_chat_id'</i></li>
    <li>Run the python script and wait for the telegram notification</li>
        <ul>
            <li>python2 script.py</li>
        </ul>
</ol>
