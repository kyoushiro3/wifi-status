import telebot
import subprocess
import time
import os

bot = telebot.TeleBot("7100429898:AAF6ux3wBXFcdnuvXwIfaCgzG9mhBMkmYsc")

def check_local_ip_status(local_ip):
    result = os.system("ping -c 1 " + local_ip)
    if result != 0:
        return 1

def send_notification(ip_address):
    chat_id = "-4184756717"
    bot.message_handler(commands=['start', 'help'])
    bot.send_message(chat_id, text=f"{name} was down pls check.")


local_ip_addresses = {"Villa 1-AP GF":"172.16.50.241", 
                        "Villa 1-AP 2F" : "172.16.50.242", 
                        "Villa 2-AP GF":"172.16.20.241", 
                        "Villa 2-AP 2F" :"172.16.20.242", 
                        "Villa 3-AP GF":"172.16.30.241", 
                        "Villa 3-AP 2F" :"172.16.30.242", 
                        "Villa 4-AP GF":"172.16.40.241", 
                        "Villa 4-AP 2F" :"172.16.40.242", 
                        "Villa 5-AP GF":"172.29.11.241", 
                        "Villa 5-AP 2F" :"172.29.11.240", 
                        "Villa 6-AP GF":"172.29.11.242", 
                        "Villa 6-AP 2F" :"172.29.11.243", 
                        "Villa 7-AP GF":"172.29.11.246", 
                        "Villa 7-AP 2F" :"172.29.11.245", 
                        "Villa 8-AP GF":"173.16.13.241", 
                        "Villa 8-AP 2F" :"173.16.13.242", 
                        "Villa 9-AP GF":"173.16.13.243", 
                        "Villa 9-AP 2F" :"173.16.13.244", 
                        "Villa 10-AP GF":"173.16.13.246", 
                        "Villa 10-AP 2F" :"173.16.13.245"}

while True:
    for name,ip_address in local_ip_addresses.items():
        if check_local_ip_status(ip_address):
            send_notification(ip_address)
            print(name + " is unreachable!")
    time.sleep(60)