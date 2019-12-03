import config
import fileinput
from ZulipUtil import ZulipUtil

def get_data_from_stdin():
    stdin_data=''
    for line in fileinput.input():
        stdin_data = stdin_data + line
    return stdin_data

def main():
    util = ZulipUtil(config.ZULIP_SITE_URL, config.ZULIP_USER_EMAIL, config.ZULIP_API_KEY)
    stdin_data = get_data_from_stdin()
    util.send_message_to_zulip(config.ZULIP_STREAM, config.ZULIP_SUBJECT, stdin_data)
    
if __name__ == "__main__":
    main()