import socket, re

def show(line):
   for x in line:
      print x," ",
   print


def catchSent(clientsock):
  flag=False
  answer=[]
  while True:
    recv_data = clientsock.recv(512)
    # print ">>",recv_data
    if re.search('<RECOGOUT>',recv_data):
       flag=True
    elif (flag==True):
       tmp = re.findall('<WHYPO WORD="[^"]+"',recv_data)
       # print ">>> ",tmp
       for one in tmp:
          answer.append(one.split('"')[1])
       if re.search('</RECOGOUT>',recv_data):
          return(answer)

def analyze(sent):
   move = "S"
   if "��" in sent:
       move = "left"
   elif "�E" in sent:
       move = "right"
   elif ("���" in sent) or ("������" in sent):
       move = "back"
   elif ("�Ƃ܂�" in sent) or ("STOP" in sent) or ("�~�܂�" in sent):
       move = "stop"
   elif ("�s��" in sent) or ("�i��" in sent) or ("�O" in sent):
       move = "go"
   elif ("balse" in sent):
       move = "quit"
   else:
       move = "other"
   return(move)

while True:
     sent = catchSent(clientsock)
     show(sent)
     print "==>", analyze(sent)