import poplib
import ssl
import email
from email.header import decode_header, make_header
from flask import Flask,render_template

# POP3 데이터
pop3_server = 'pop..com'
username = ''
password = ''

# SSL 연결
context = ssl.create_default_context()
server = poplib.POP3_SSL(pop3_server, port=995, context=context)

# 서버 연결
server.user(username)
server.pass_(password)

'''num_messages, mailbox_size = server.stat()'''

kakao = []

server.set_debuglevel(1)
server.max_message_size = 100 * 1024 * 1024

messages = len(server.list())

for message in range (messages):
    kakao.append(message)

'''# 가장 최근에 도착한 메시지 10개 가져오기
messages = []
msg = []
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
    msg.append(decoded_subject)'''

# Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    naver = []
    '''for i in range(0, 10, 1):
        naver.append(f"{msg[i]}")'''
    return render_template('main.html', data0=kakao)


if __name__ == '__main__':
    app.debug = True
    app.run()

# 여기까지 Flask
