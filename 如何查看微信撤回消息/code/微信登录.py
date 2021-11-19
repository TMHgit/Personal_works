"""
itchat -

Author 
Date 2021/11/15

"""
import time
import  os
import itchat
from itchat.content import * # 导入itchat下的content模块
import  xml.dom.minidom

temp='C:/Users/tian/Desktop/chat'+'/'+'撤回的消息'
itchat.auto_login(hotReload=True)
friends=itchat.search_friends(name=['饭王','向琪','徐慧','陈崇鸣','殷雨','杨超'])
username=[]
dict = {}
for i in friends:
    if i['UserName']!=None:
        username.append(i['UserName'])

#如果不存在文件夹，就创建
if not os.path.exists(temp):
    os.mkdir(temp)
# itchat.send('1111',toUserName=username[0])

@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE,itchat.content.RECORDING])  #监听消息
def resever_info(msg):
    print(msg)
    info=msg['Text'] #取文本消息
    msgid=msg['MsgId'] # 取出消息标识
    info_type=msg['Type'] # 获取消息数据类型
    fromUser = itchat.search_friends(userName=msg['FromUserName'])['NickName'] # 获取用户名
    ticks=msg['CreateTime'] # 获取信息发送时间
    time_local=time.localtime(ticks)
    dt=time.strftime('%Y-%m-%d %H:%M:%S',time_local) # 格式化日期
    name = msg['FileName']  # 读取语音（图片文件）文件名
    # 将消息标识和消息内容添加到字典
    #每一条消息的唯一标识作为键，消息的具体信息作为值,也是一个字典
    dict[msgid]={'info':info,'info_type':info_type,'name':name,'fromUser':fromUser,'dt':dt}
    print(f'发送人:{fromUser}:消息：{info} 消息类型:{info_type}:发送时间{dt}')


    if info_type == 'Recording':
        #保存语言
        info(temp + '/' + name)
    elif info_type == 'Picture':
        # 保存图片
        info(temp + '/'+name)

@itchat.msg_register(NOTE) # 监听系统提示
def note_info(msg): # 监听到好友撤回了一条消息
    if '撤回了一条消息' in msg['Text']:
        # 获取系统消息的Content节点值
        content=msg['Content']
        # Content值为xml,解析xml
        doc=xml.dom.minidom.parseString(content)
        #取出msgid标签的值
        result=doc.getElementsByTagName('msgid')
        #该msgid就是撤回的消息标识，通过它可以在字典中找到
        msgid=result[0].childNodes[0].nodeValue
        # 从字典中取出对应消息标识的消息类型
        msg_type=dict[msgid]['info_type']
        if msg_type == 'Recording':
            recording_info = dict[msgid]['info'] # 取出消息标识对应的消息内容
            info_name=dict[msgid]['name'] # 取出消息文件名
            fromUser=dict[msgid]['fromUser'] # 取出发送者
            dt=dict[msgid]['dt'] # 取出发送时间
            recording_info(temp + '/' + info_name) # 保存语言
            # 拼接提示消息
            send_msg = '[发送人:]' + fromUser + '\n'+ '发送时间' + dt + '\n'+'撤回了一条语言消息'
            itchat.send(send_msg,'filehelper') # 将消息发送给文件助手
            # 发送保存的语言
            itchat.send_file(temp+'/'+ info_name,'filehelper')
            del dict[msgid]
            print('保存语音')
        elif msg_type == 'Text':
            text_info=dict[msgid]['info'] # 取出消息标识对应的消息内容
            fromUser = dict[msgid]['fromUser']  # 取出发送者
            dt = dict[msgid]['dt']  # 取出发送时间
            # 拼接提示消息
            send_msg = '[发送人:]' + fromUser + '\n'+ '发送时间' + dt + '\n'+ '撤回内容'+text_info
            itchat.send(send_msg, 'filehelper')  # 将消息发送给文件助手
            del dict[msgid] # 删除字典中对应的消息
            print('保存文本')
        elif msg_type == 'Picture':
            picture_info=dict[msgid]['info']
            fromUser = dict[msgid]['fromUser']  # 取出发送者
            dt = dict[msgid]['dt']  # 取出发送时间
            info_name = dict[msgid]['name']  # 取出消息文件名
            picture_info(temp+'/'+ info_name)
            # 拼接提示消息
            send_msg = '[发送人:]' + fromUser + '\n'+ '发送时间' + dt + '\n' + '撤回了一张图片'
            itchat.send(send_msg, 'filehelper')  # 将消息发送给文件助手
            del dict[msgid]  # 删除字典中对应的消息
            print('保存图片')


itchat.run()




