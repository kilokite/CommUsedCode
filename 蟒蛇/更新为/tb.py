#encoding:utf-8

'''
v0.01吧
第一次写Python，问题不少，以前能用js就用js解决了2333（js NB！
一边学一边写写的，有些地方直接妥协了

现在只能同步脚本所在目录下的所有文件
因为懒，所以文件夹在服务端暂时不能同步（如果有新的文件夹要在服务端自己添加）
提取server目录也是简单粗暴直接用的replace
看样子文件夹也不能出现中文（为什么要用中文）
又 不 是 不 能 用
'''
import os
import json
import hashlib
import time
import requests
#引入模块
G_passwd = '密码' #密码要与服务端相同
G_db = open('Aupdatedb.json').read()
G_db = json.loads(G_db)
#定义全局变量
def md5(data):
    return hashlib.md5(data.encode('utf8')).hexdigest()
    
def ishave(var):
    try:
        var
        return True
    except err:
        return False

'''
print(md5("你哈"))
#没什么用（试试hash能不能用
Worktable = os.getcwd()
'''

def update(table):
    File_list = os.listdir(table)
    for File_name in File_list: #遍历文件
        if os.path.isdir(File_name):
            update(table+'/'+File_name)
            #进入下一递归
        else:
            #不是文件夹 准备上传
            File_table = table+'/'+File_name
            print("准备上传："+File_table)
            File_content = open(File_table).read()
            #读取文件
            File_hash = md5(File_content)
            '''
            try:
               o = G_db[File_table]
            except NameError:
                 G_db[File_table] = File_hash
             '''       
            if not(File_table in G_db) or G_db[File_table]!=File_hash and File_name!='tb.py':
                #判断文件是否有变化
                S_File_table =  File_table.replace(Worktable+'/','')
                #计算在server上的目录
                #↑垃圾，requests NB!
                #准备计算签名啥的
                V_time = int(time.time())
                V_token = md5(str(V_time) + S_File_table + G_passwd + File_content)
                #时间戳（秒）+ 文件路径 + 密码 + 文件内容
                values = {
                'time':V_time,
                'file_content':File_content,
                'file_name':S_File_table,
                'token':V_token

                }
                #数据准备完了，准备发送
                r = requests.post('http://blogg.zocs.cc/Aupdate.php', data=values)
                if r.text == 'OKAY':
                    #如果上传成功的话
                    G_db[File_table] = File_hash
                    print(r.text)
                    print(S_File_table)
                else:
                    print('上传失败')
                    print(r.text)
            else:
                print('文件未发生改变/或是保护文件')
    open('Aupdatedb.json','w').write(json.dumps(G_db))


            

update(Worktable)
