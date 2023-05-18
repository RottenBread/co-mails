import poplib
import ssl
import email
from email.header import decode_header, make_header
from flask import Flask,render_template
from email.parser import BytesParser

# POP3 데이
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
    decoded_subject = decode_header(subject)[0][0]
    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode()
    naver_msg.append(decoded_subject)


# POP3 데이터
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
    decoded_subject = decode_header(subject)[0][0]
    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode('utf-8')
    google_msg.append(decoded_subject)

# Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html', data1=naver_msg, data2=naver_username, data3=google_msg, data4=google_username)


if __name__ == '__main__':
    app.debug = True
    app.run()

# 여기까지 Flask

