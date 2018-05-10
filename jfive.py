#十进制转十六进制
def jfive_hex(i):

    return "0x"+"{:02x}".format(i)

def jfive_hex32(i):

    return "0x"+"{:04x}".format(i)
    
#获取时间戳
#import datatime
def jfive_get_timestamp():

   return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
   
   
#十六进制列表转带`0x`字符串
def jfive_get_hex_String(hex_list):

  return ' '.join('{:02x}'.format(x) for x in hex_list)
  
  
  

 
