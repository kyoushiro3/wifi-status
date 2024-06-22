#This Python script utilizes the Telebot library to monitor the status of a list of local IP addresses and send notifications via Telegram if any of the IPs are unreachable.

## Requirements

- Python
- Telebot library

## Setup

1. Obtain a Telegram Bot token and replace `"your_bot_token_here"` with your actual token.
2. Add your Telegram chat ID in the `chat_id` variable within the `send_notification` function.
3. Update the `local_ip_addresses` dictionary with the names and corresponding IP addresses of the devices you want to monitor.
4. Adjust the time interval in the `time.sleep()` function based on your IP list.

## Usage

- Run the script to continuously check the status of the listed IP addresses.
- If an IP is unreachable, a notification will be sent to the specified Telegram chat.