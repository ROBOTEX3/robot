#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import cStringIO

host = '127.0.0.1'
port = 10500

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

new_list = []
xml_buff = ""
in_recoguout = False

while True:
      data = cStringIO.StringIO(sock.recv(4096))
      line = data.readline()
      while line:
            if line.startswith("<RECOGOUT>"):
                  in_recoguout = True
                  #xml_buff + new_buff[1]
            elif line.startswith("</RECOGOUT>"):
                  if xml_buff.find('CLASSID') > 0:
                        in_recoguout = False
                        xml_buff = ""
                        print("Talk again")
                        break
                  new_list = xml_buff.split(" WORD=")
                  new_list.pop(0)
                  new_list.pop(0)
                  new_list.pop()
                  xml_buff = ''.join(new_list)
                  xml_buff = xml_buff.replace("\"", "")
                  print(xml_buff)
                  in_recoguout = False
                  xml_buff = ""
            else:
                  if in_recoguout:
                        if line.find("WORD=") > 0:
                              xml_buff += line
            line = data.readline()
            
sock.close()
