#获取所有解析接口
import requests
import re
import tkinter as tk
import webbrowser
url = "http://www.qmaile.com/"
r = requests.get(url) 
r.encoding = r.apparent_encoding
url_content = r.text
#print(r.raise_for_status())
#print(r.status_code)
#print(url_content)

#数据提取
code_re = re.compile('<option value="(.*?)" selected')
locaction_content = re.findall(code_re,url_content)#find_all函数选择所有匹配到的结果
parser_url1 = locaction_content[0]
parser_url2 = locaction_content[1]
parser_url3 = locaction_content[2]
parser_url4 = locaction_content[3]
parser_url5 = locaction_content[4]
print(locaction_content[0])
print(locaction_content[1])

#创建画板
draw_board = tk.Tk()#命名一个画板
draw_board.title("VIP电影播放")
draw_board.geometry("350x300")#画板大小
l1 = tk.Label(draw_board,text = "播放接口",font = ("Arial",12))
l1.grid()
l2 = tk.Label(draw_board,text = "播放链接",font = ("Arial",12))
l2.grid(row=5,column=0)

tp1 = tk.Entry(draw_board,text="",width=35) 
tp1.grid(row=5,column=1)

bt = tk.StringVar()#创建按钮,管理字符（按钮上的）
bt1 = tk.Radiobutton(draw_board, text = "播放接口1",variable=bt,value =parser_url1)
bt1.grid(row=0,column=1)

bt2 = tk.Radiobutton(draw_board, text = "播放接口2",variable = bt,value = parser_url2)
bt2.grid(row=1,column=1)

bt3 = tk.Radiobutton(draw_board, text = "播放接口3",variable = bt,value = parser_url3)
bt3.grid(row=2,column=1)

bt4 = tk.Radiobutton(draw_board, text = "播放接口4",variable = bt,value =parser_url4)
bt4.grid(row=3,column=1)

bt5 = tk.Radiobutton(draw_board, text = "播放接口5",variable = bt,value = parser_url5)
bt5.grid(row=4,column=1)

#播放按钮
def open_browser():
    webbrowser.open(bt.get()+tp1.get())

play1 = tk.Button(draw_board,text = "播放",font = ("Arial",10),width=8,command = open_browser)
play1.grid(row=6,column=1)

#清除按钮
def del_text():
    tp1.delete(0,"end")

clean1 = tk.Button(draw_board,text = "清除",font = ("Arial",10),width=8,command = del_text)
clean1.grid(row=8,column=1)

draw_board.mainloop()