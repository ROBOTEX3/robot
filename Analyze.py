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
   if "左" in sent:
       move = "left"
   elif "右" in sent:
       move = "right"
   elif ("後ろ" in sent) or ("さがれ" in sent):
       move = "back"
   elif ("とまれ" in sent) or ("STOP" in sent) or ("止まれ" in sent):
       move = "stop"
   elif ("行け" in sent) or ("進め" in sent) or ("前" in sent):
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