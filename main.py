import poplib
import ssl
import re
import email
from email.header import decode_header, make_header
from flask import Flask,render_template
from email.parser import BytesParser

pattern = '\<[^)]*\>'

# ========================================================================
# NAVER POP3 DATA
# ========================================================================
pop3_server = "pop.naver.com"
username = ""
password = ""
naver_username = username

# SSL 연결
context = ssl.create_default_context()
server = poplib.POP3_SSL(pop3_server, port=995, context=context)

# 서버 연결
server.user(username)
server.pass_(password)

num_messages, mailbox_size = server.stat()


# 가장 최근에 도착한 메시지 10개 가져오기
messages = []
naver_msg = []
for i in range(num_messages, num_messages - 10, -1):
    _, lines, _ = server.retr(i)
    message_content = b'\n'.join(lines).decode()
    messages.append(message_content)

# 메일 제목 가져오기
for message in messages:
    email_message = email.message_from_string(message)
    subject = email_message['Subject']
    if subject is None:
        subject = "광고 메일이거나 제목이 없는 메일입니다."
    decoded_subject = decode_header(subject)[0][0]

    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode()
    sender = email_message['From']
    if sender is None:
        sender = "(알수없음)"
    decoded_sender = decode_header(sender)[0][0]

    if isinstance(decoded_sender, bytes):
        decoded_sender = decoded_sender.decode()
    decoded_2_sender = re.sub(pattern = pattern, repl = '', string = decoded_sender)
    decoded_3_sender = decoded_2_sender.replace("\"","")

    message_data = {
        'subject': decoded_subject,
        'sender': decoded_3_sender
    }

    naver_msg.append(message_data)

# ========================================================================
# GOOGLE POP3 DATA
# ========================================================================
pop3_server = "pop.gmail.com"
username = ""
password = ""
google_username = username

# SSL 연결
context = ssl.create_default_context()
server = poplib.POP3_SSL(pop3_server, port=995, context=context)

# 서버 연결
server.user(username)
server.pass_(password)


# 가장 최근에 도착한 메시지 10개 가져오기
messages = []
google_msg = []
message_count = len(server.list()[1])
start_index = max(1, message_count - 9)

for i in range(start_index, message_count + 1):
    _, msg_lines, _ = server.retr(i)
    msg_content = b'\r\n'.join(msg_lines)
    msg = BytesParser().parsebytes(msg_content)

    # 제목 디코딩
    subject = msg['Subject']
    if subject is None:
        subject = "광고 메일이거나 제목이 없는 메일입니다."
    decoded_subject = decode_header(subject)[0][0]

    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode()
    sender = msg['From']
    if sender is None:
        sender = "(알수없음)"
    decoded_sender = decode_header(sender)[0][0]

    if isinstance(decoded_sender, bytes):
        decoded_sender = decoded_sender.decode()
    decoded_2_sender = re.sub(pattern = pattern, repl = '', string = decoded_sender)
    decoded_3_sender = decoded_2_sender.replace("\"","")

    message_data = {
        'subject': decoded_subject,
        'sender': decoded_3_sender
    }

    google_msg.append(message_data)

# ========================================================================
# KAKAO POP3 DATA
# ========================================================================
pop3_server = "pop.kakao.com"
username = ""
password = ""
kakao_username = username


# SSL 연결
context = ssl.create_default_context()
server = poplib.POP3_SSL(pop3_server, port=995, context=context)

# 서버 연결
server.user(username)
server.pass_(password)


# 가장 최근에 도착한 메시지 10개 가져오기
messages = []
kakao_msg = []
message_count = len(server.list()[1])
start_index = max(1, message_count - 9)

for i in range(start_index, message_count + 1):
    _, msg_lines, _ = server.retr(i)
    msg_content = b'\r\n'.join(msg_lines)
    msg = BytesParser().parsebytes(msg_content)

    # 제목 디코딩
    subject = msg['Subject']
    if subject is None:
        subject = "광고 메일이거나 제목이 없는 메일입니다."
    decoded_subject = decode_header(subject)[0][0]

    if isinstance(decoded_subject, bytes):
        try:
            decoded_subject = decoded_subject.decode('utf-8')
        except UnicodeDecodeError:
            decoded_subject = decoded_subject.decode('euc-kr')
    sender = msg['From']
    if sender is None:
        sender = "(알수없음)"
    decoded_sender = decode_header(sender)[0][0]

    if isinstance(decoded_sender, bytes):
        try:
            decoded_sender = decoded_sender.decode('utf-8')
        except UnicodeDecodeError:
            decoded_sender = decoded_sender.decode('euc-kr')
    decoded_2_sender = re.sub(pattern = pattern, repl = '', string = decoded_sender)
    decoded_3_sender = decoded_2_sender.replace("\"","")

    message_data = {
        'subject': decoded_subject,
        'sender': decoded_3_sender
    }

    kakao_msg.append(message_data)


# ========================================================================
# DAUM POP3 DATA
# ========================================================================
pop3_server = "pop.daum.net"
username = ""
password = ""
daum_username = username


# SSL 연결
context = ssl.create_default_context()
server = poplib.POP3_SSL(pop3_server, port=995, context=context)

# 서버 연결
server.user(username)
server.pass_(password)


# 가장 최근에 도착한 메시지 10개 가져오기
messages = []
daum_msg = []
message_count = len(server.list()[1])
start_index = max(1, message_count - 9)

for i in range(start_index, message_count + 1):
    _, msg_lines, _ = server.retr(i)
    msg_content = b'\r\n'.join(msg_lines)
    msg = BytesParser().parsebytes(msg_content)

    # 제목 디코딩
    subject = msg['Subject']
    if subject is None:
        subject = "광고 메일이거나 제목이 없는 메일입니다."
    decoded_subject = decode_header(subject)[0][0]

    if isinstance(decoded_subject, bytes):
        try:
            decoded_subject = decoded_subject.decode('utf-8')
        except UnicodeDecodeError:
            decoded_subject = decoded_subject.decode('euc-kr')
    sender = msg['From']
    if sender is None:
        sender = "(알수없음)"
    decoded_sender = decode_header(sender)[0][0]

    if isinstance(decoded_sender, bytes):
        try:
            decoded_sender = decoded_sender.decode('utf-8')
        except UnicodeDecodeError:
            decoded_sender = decoded_sender.decode('euc-kr')
    decoded_2_sender = re.sub(pattern = pattern, repl = '', string = decoded_sender)
    decoded_3_sender = decoded_2_sender.replace("\"","")

    message_data = {
        'subject': decoded_subject,
        'sender': decoded_3_sender
    }

    daum_msg.append(message_data)
    
# Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html', data1=naver_msg, data2=naver_username, data3=google_msg, data4=google_username, data5=kakao_msg, data6=kakao_username, data7=daum_msg, data8=daum_username)


if __name__ == '__main__':
    app.debug = True
    app.run()

# 여기까지 Flask