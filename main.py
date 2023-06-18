import getpass, poplib
import ssl
import re
from email.header import decode_header
from flask import Flask,render_template
from email.parser import BytesParser

pattern = '\<[^)]*\>'

def getMeg(pop3_server, username, password):
    # SSL 연결
    context = ssl.create_default_context()
    poplib._MAXLINE = 20480
    server = poplib.POP3_SSL(pop3_server, port=995, context=context)

    # 서버 연결
    server.user(username)
    server.pass_(password)

    result_msg = []
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
            sender = "알수없음"
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

        result_msg.append(message_data)

    return result_msg, username


google_msg, google_username = getMeg("pop.gmail.com", "INPUT_YOUR_ADDRESS", "INPUT_YOUR_PASSWORD")
daum_msg, daum_username = getMeg("pop.daum.net", "INPUT_YOUR_ADDRESS", "INPUT_YOUR_PASSWORD")
kakao_msg, kakao_username = getMeg("pop.kakao.com", "INPUT_YOUR_ADDRESS", "INPUT_YOUR_PASSWORD")
naver_msg, naver_username = getMeg("pop.naver.com", "INPUT_YOUR_ADDRESS", "INPUT_YOUR_PASSWORD")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html', data1=naver_msg, data2=naver_username, data3=google_msg, data4=google_username, data5=kakao_msg, data6=kakao_username, data7=daum_msg, data8=daum_username)

@app.route('/about.html')
def getTicket():
   return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
