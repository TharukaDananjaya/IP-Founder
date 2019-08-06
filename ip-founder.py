import socket


def pc_info():
     host_name =  "www.esoft.com" # you can change you expext web site
     ip_address = socket.gethostbyname(host_name)
     try:
         print ("Name :"  ,host_name)
         print ("IP Address :" , ip_address)
     except socket.error:
         print (host_name, socket.error)



if __name__ == '__main__':
     pc_info()
