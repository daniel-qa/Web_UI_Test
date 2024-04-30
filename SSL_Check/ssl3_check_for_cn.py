import socket
import ssl
import datetime
import time
import sys
from dingtalkchatbot.chatbot import DingtalkChatbot



def need_nodify_check(base_url,expire_date,days):
    
    msg2 =''

    if( days <= 0 ):
        msg2 = base_url + u'\n==== SSL憑證已經過期 ==== \n'
        

    if( (days > 0) and (days < 14)  ):
        msg2 = base_url + u'\n==== SSL憑證即將過期 ==== \n'  +  "剩餘天數: " + str(days) + "天"
    
    print(msg2)

    if( len(msg2)>0):
        ddmsg(msg2)

def check_ssl_expiry(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)

    try:
        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        # parse the string from the certificate into a Python datetime object
        expiry_date = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        remaining_days = (expiry_date - datetime.datetime.now()).days
        
        # 2個星期前提醒
        
        print(f"The SSL certificate for {hostname} expires in {remaining_days} days.")
        
        need_nodify_check(hostname,expiry_date,remaining_days)        
        
        
    except Exception as e:
        print(f"Error occurred while checking SSL certificate for {hostname}: {e}")
    finally:
        conn.close()


# send ding msg
def ddmsg(msg, hookid=1):

    if(hookid == 1):

        # WebHook地址        
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=123"  # 自定義詞 "SSL" 替換為您的釘釘機器人 Webhook URL

    if(hookid == 2): #  正式群組
        #WebHook地址
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=456'

    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)

    #Text消息@所有人
    xiaoding.send_text(msg=msg, is_at_all=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <hostname>")
        sys.exit(1)
    
    hostname = sys.argv[1]
    
    print(hostname)
    
    check_ssl_expiry(hostname)
    
    