import os,sys

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
  
  
#获取特定后缀文件

def jfive_get_paths(root_path,postfix):
    path_set = set()
    for dir_path, dir_names,file_names in  os.walk(root_path):
        for fname in file_names:
            total_path = os.path.join(dir_path,fname)
            fname = fname.lower()
            if os.path.splitext(fname)[1] == postfix:
                print('找到文件{0}：{1}'.format(postfix,fname))
                path_set.add(total_path)
    return path_set

 
