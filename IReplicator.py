#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import tkinter,tkinter.filedialog,turtle
from tkinter import*
import re
import shutil
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import tkinter.messagebox
import os
import sys
import subprocess
import tkinter.font
import webbrowser
import tkinter.ttk
from threading import Thread
import time
from bs4 import BeautifulSoup
from PIL import Image ,ImageTk
from urllib.request import urlopen

root = tkinter.Tk()
root.title('153546 ')
root.configure(background = 'black')
root.geometry("390x135+200+300")

myfont = tkinter.font.Font(family="Segoe UI Light", size=12,weight = 'bold')
myfont1 = tkinter.font.Font(family="Segoe UI Light", size=10)
global download_btn,download_frame,Open
global streams,video,status_var,status
global dlocation,Bytes,maxbytes,cv,download_frame
global Opn,checkframe,buttonframe,progressbar,ftype,space,textframe,download_btn




global known_files,unknown_files
global Opn
Opn = Button(root,text= 'Open output folder ',fg= 'white', bg ='blue',padx =3,pady =3)
known_files =  {}
unknown_files = {}
def callback():
    if tkinter.messagebox.askokcancel("Quit", "Quit **** DM ?"):
        root.destroy()


Label(root,text='Url:',fg = 'white',bg = 'black',font = myfont).grid(row =0,column=0,padx=3,pady=3)
e = Text (root,fg= 'blue', bg = 'red',height = 1,width =30,padx=3,pady=5)
e.grid(row=0,column=1,padx=3,pady=3,sticky = E)
e.focus()

global cv,t
cv = tkinter.Canvas(root,width = 420,height = 400)
t = turtle.RawTurtle(cv)

global screen,x,y,dlocation
screen = t.getscreen()
screen.bgcolor("light gray")
x,y = -195,160
dlocation = "C:\\A08's Downloader\\"
def WriteText(text,clr):
    global x,y,t
    t.color('light gray')
    t.setx(x)
    t.sety(y)
    t.color(clr)
    t.write(text,move = False ,font = ("Arial",15,"normal"))
    y-=25
def Write_H(text,clr,sub):
     global x,y,t
     newline ="\n"
     t.color('light gray')
     t.setx(x)
     t.sety(y)
     t.color(clr)
     x=x+sub
     t.write(text,font = ("cambria",10,"normal"))
def Write(text,clr,sub):
     global x,y,t
     newline ="\n"
     t.color('light gray')
     t.setx(x)
     t.sety(y)
     t.color(clr)
     y=y-sub
     t.write(text,font = ("cambria",10,"normal"))
     

global stop;
stop = False;

def select():
    global dlocation,space
    dlocation = tkinter.filedialog.askdirectory(parent=root,initialdir="C:\\A08's Downloader\\",title='Select Output Folder')+'\\'
    tkinter.messagebox.showinfo('Target','Locked on ' + str(dlocation))

   
global ftype
ftype = Label(root,text='Filetype:',fg = 'white',bg = 'black',font = myfont)
ftype.grid(row =7,column=0,padx=3,pady=3)
global checkframe
checkframe = Frame(root,width=100,height=20,background = 'black',borderwidth = 1)
checkframe.grid(row = 7,column= 1,sticky = W)

var1= tkinter.IntVar()
var2= tkinter.IntVar()
var3= tkinter.IntVar()
var4= tkinter.IntVar()
var5 = tkinter.IntVar()
c1 = Checkbutton(checkframe ,text= 'mp3',fg = 'medium sea green',bg = 'black',variable = var1).pack(side = LEFT)
c2= Checkbutton(checkframe ,text= 'jpg',fg = 'medium sea green',bg = 'black',variable = var2).pack(side = LEFT)
c3 = Checkbutton(checkframe ,text= 'mp4',fg = 'medium sea green',bg = 'black',variable = var3).pack(side = LEFT)
c4 = Checkbutton(checkframe ,text= 'pdf',fg = 'medium sea green',bg = 'black',variable = var4).pack(side = LEFT)
c5 = Checkbutton(checkframe ,text= 'png',fg = 'medium sea green',bg = 'black',variable = var5).pack(side = LEFT)


global buttonframe
buttonframe = Frame(root,bg = "black");
buttonframe.grid(row=8,column=1,columnspan = 2,sticky = W);



button = Button(root,text= 'Select Output Folder',fg= 'black', bg ='yellow',padx=3,pady=3,font = myfont1)
button.configure(command = select)
button.grid(row = 8,column=0)

global used
used = False





global download_links,final_links
final_links = {}
download_links = {}

def find_links(Tag,location,Type):
    global f
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent','Mozilla/5.0')]
        f = opener.open(e.get(1.0,END))
    except ValueError as Argument:
        global status_var,status
        satus_var = Argument
        status = Label(root,textvariable=status_var,fg = 'white',bg = 'black',font = myfont)
        progressbar.grid_forget()
        root.update_idletasks()

    soup = BeautifulSoup(f.read())
    WriteText('fetching ' + Type,'Red')
    for link in soup.find_all(str(Tag)):
        url= f.geturl()
        temp_link = str(link.get(str(location)))
        if(re.search('^h',temp_link)):
            if not(re.search(r'\.((...)|(....))$',temp_link)):
                root.update()
                try:
                    temp_link = urllib.request.urlopen(temp_link).geturl()
                except Exception as error:
                    global space
                    if not str(link.string) == 'None':
                        space.insert('end','\n')
                        space.insert('end',str(error) + ':')
                        space.insert('end','\n')
                        space.insert("end",str(link.string)[0:35])
                        space.insert('end','\n')
                        space.insert('end','\n')
                       
                    else:
                        pass
                    pass

                root.update_idletasks()
                if not str(link.string) == 'None':
                    space.insert("end","found: " + str(link.string)[0:35])
                    space.insert('end','\n')
                else:
                    pass
                download_links[temp_link] = str(link.string)
                
            else:
                if not str(link.string) == 'None':
                    space.insert("end","found: " + str(link.string)[0:35])
                    space.insert('end','\n')
                else:
                    pass
                download_links[temp_link] = str(link.string)
                root.update_idletasks()
                        

        else:
            URL = re.split('/',url)
            domain = str(URL[0])+'//'+str(URL[1])+str(URL[2])
            temp_link = domain+ temp_link
            download_links[temp_link] = str(link.string)
        root.update_idletasks()
        
    for link in download_links:
           if (re.search(r'\.'+str(Type)+'$',str(link))):
                final_links[str(link)]=download_links[link]

global known_down_status,unknown_down_status,k_finish,uk_finish
known_down_status = False
unknown_down_status   = False
k_finish = False
un_finish = False
    
def known_finish():
    
    global known_down_status,k_finish,space,indeterminate_progressbar,un_finish
    known_down_status = True
    global known_files,known,dlocation
    count = 0
    for i in known_files:
        if(known_files[i].get() == 1):
            count+=1
    if count == 0:
        k_finish =True
   
    for i in known_files:
        if(known_files[i].get() == 1):
            if (os.path.exists(dlocation+known[i]+'.'+i[-3:])):
                global space
                space.insert(1.0,known[i]+'.'+i[-3:]+'Already Exists\n\n\n')
                space.tag_configure('select',foreground = 'red')
                space.tag_add('select','1.0','1.200')
            else:
                
            
                file = open(dlocation+known[i]+'.'+i[-3:],'wb')
                try:
                    space.insert(END,'downloading.. : '+known[i]+'\n')
                    if(file.write(urllib.request.urlopen(i).read())):
                        space.insert(END,'finished downloading : '+known[i]+'\n')

                 
                except Exception as e:
                    space.insert(1.0,str(e))
                    root.update()
                    pass
                    root.update()
    
    k_finish = True
    print(k_finish,un_finish)
    if(k_finish == True and un_finish == True):
        
        space.insert(1.0,'\n   ******FINISHED DOWNLOADING******* \n\n  Click Open to Open the download folder\n\n')
        space.tag_add('finish','2.0','2.200')
        space.tag_add('open','4.0','4.300')
        space.tag_configure('finish',foreground = 'darkgreen')
        space.tag_configure('open',foreground = 'red')
        root.update()
        print('1')
        tl.geometry("620x635+610+40")

    known_down_status = False
    

def unknown_finish():
    
    global unknown_down_status,indeterminate_progressbar,status,un_finish
    unknown_down_status = True
    global unknown_files,unknown,dloaction,space
    count = 0
    for i in unknown_files:
        if(unknown_files[i].get() == 1):
            count+=1
    if count == 0:
        un_finish =True
        
    for i in unknown_files:
        if(unknown_files[i].get() == 1):
            if (os.path.exists(dlocation+unknown[i])):
                global space
                space.insert(1.0,dlocation+unknown[i]+'Already Exists\n\n\n')
                space.tag_configure('select',foreground = 'red')
                space.tag_add('select','1.0','1.200')
            else:

            
                file = open(dlocation+unknown[i],'wb')
                try:
                    space.insert(END,'downloading.. : '+i[-15:]+'\n')
                    if(file.write(urllib.request.urlopen(i).read())):
                        space.insert(END,'finished downloading : '+i[-15:]+'\n')
                        
                    
                except Exception as e:
                    space.insert(1.0,str(e))
                    root.update()
                    pass

    unknown_down_status = False
    un_finish =True

    print(k_finish,un_finish)
    if(k_finish == True and un_finish == True):

        space.insert(1.0,'\n   ******FINISHED DOWNLOADING******* \n\n  Click Open to Open the download folder\n\n')
        space.tag_add('finish','2.0','2.200')
        space.tag_add('open','4.0','4.300')
        space.tag_configure('finish',foreground = 'darkgreen')
        space.tag_configure('open',foreground = 'red')
        root.update()
        print('2')
        global tl
        tl.geometry("620x610+610+40")



def finish():
    global status_var,download_btn,Open,known_down_status,unknown_down_status,known_files,sapce,indeterminate_progressbar
    root.update()
    download_btn.pack_forget()
    root.update()
    count = 0
    
    
    for i in known_files:
        count+=known_files[i].get()
    for i in unknown_files:
        count+= unknown_files[i].get()

    if count != 0:
        if known_down_status == False and unknown_down_status == False:
            t_known   = Thread(target = known_finish)
            t_unknown = Thread(target= unknown_finish)
            t_known.start()
            t_unknown.start()
            space.delete(1.0,END)
            space.insert(1.0,'Please wait.. Download is in progress.\n')
            indeterminate_progressbar.grid(row=15,column=0,columnspan =2 ,padx=3,pady=3)
            indeterminate_progressbar.start()
            
        else:
            space.insert (END,'already downloading..\n')
    else:
        #space.delete(1.0)
        space.insert(1.0,'Select Something.. \n')
        space.tag_configure('select',foreground = 'red')
        space.tag_add('select','1.0','1.200')
    download_btn.pack(side = 'left')
    
    root.update()
def check():
    print (e.get(1.0,END))
    if var1.get()==0 and var2.get()==0 and var3.get()==0 and var4.get()==0 and var5.get()==0:
        if e.get(1.0,END)==None:
            tkinter.messagebox.showinfo('Error','Enter an URL \n select a file type')
        
        else:
            tkinter.messagebox.showinfo('Error','Select a file type ')
    else:
        if e.get(1.0,END)!=None:
            download()

    


def download():
    global status_var,status;
    status_var= StringVar()
    status_var.set('Please Wait While Downloading')

    



    root.geometry("390x135+200+300")
    global progressbar,final_links,indeterminate_progressbar,textframe,tl
    tl = tkinter.Toplevel(bg ='black')
    textframe = Frame(tl)
    download_frame = Frame(tl)
    download_btn = Button(download_frame,text = '   Download   ',fg = 'white',bg = 'blue',font = myfont1,padx = 3,pady = 3)
    Open = Button(download_frame,text = "   Open   ",fg = 'white',bg = 'red',font = myfont1,padx = 3,pady = 3)
    indeterminate_progressbar = tkinter.ttk.Progressbar(tl,orient=HORIZONTAL,length=300,mode= 'indeterminate')
    status = Label(tl,textvariable=status_var,fg = 'white',bg = 'black',font = myfont)
    download_btn.configure(command = finish)
    Open.configure(command = OPEN)
    tl.geometry("620x635+610+40")
    Open.pack(side = 'right')
    
    
    space = Text(textframe,fg = 'blue',height =35,width = 75)
    space.pack(side = 'left')
    scb = Scrollbar(textframe,orient ='vertical')
    scb.pack(side = 'right',fill = 'y')
    textframe.grid(row = 2,columnspan = 2,padx = 3,pady = 4)

    ftype.grid_forget()
    
    status_var.set('Hold on.. I\'m searching..')
    status.grid(row=8,column=0,columnspan =2 ,padx=3,pady=3)
    indeterminate_progressbar.grid(row=9,column=0,columnspan =2 ,padx=3,pady=3)
    indeterminate_progressbar.start()

    root.update()

    
    if var1.get()==1:
               find_links('a','href','mp3')
               root.update_idletasks()
    if var2.get()==1:
               find_links('img','src','jpg')
               root.update_idletasks()
    if var3.get()==1:
               find_links('video','src','mp4')
               root.update_idletasks()
    if var4.get()==1:
               find_links('a','href','pdf')
               root.update_idletasks()
    if var5.get()==1:
               find_links('img','src','png')
               root.update_idletasks()

    root.update()
    global final_links,known,unknown
    known = {}
    unknown = {}
    for link in final_links:
        if(final_links[link]== 'None'):
            t_link = re.sub(r'[][:*<>%-]','',link)
            a  = re.split(r'/',t_link)
            try:
                filename = re.sub(r'[/|\<>":*?]','',str(a[-2])+"-"+str(a[-1]))
            except:
                pass
            unknown[str(link)] = filename
            root.update()
        else:
            known[str(link)] = re.sub(r'[/|\<>":*?]','',final_links[link])
        root.update()
    
   
  
    space.delete(1.0,END)
    lb= Label(space,text ='Known:',bg = 'white' ,fg = 'darkgreen',font = tkinter.font.Font(family = 'Corbel',size = 15,weight = 'bold'))
    space.window_create('end',window= lb)
    space.insert('end','\n')
    global known_files
    global known_images
    known_images = []
    for i in unknown:
        url = i
        image_bytes = urlopen(url).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
        pil_image = Image.open(data_stream)
        pil_image = pil_image.resize((300, 300), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(pil_image)
        known_images.append(tk_image)

    j = 0

    print(len(known))
    
    for i in known:
        a = tkinter.IntVar()
        
        if (re.search(r'\.(...)$',i).group()=='.jpg' or re.search(r'\.(...)$',i).group()=='.png'):
              cb = Checkbutton(textframe,image = known_images[j],bg = 'white',variable = a,fg = 'blue')
              j+=1

        else:
              cb = Checkbutton(textframe,bg = 'white',variable = a,fg = 'blue',text = '{}'.format(known[i]+'\n'+str(i)[-40:]),font = tkinter.font.Font(family = 'Segoe Print',size = 9))  
        known_files[i] = a
        space.window_create("end",window = cb)
        space.insert('end','\n')
        space.update()


                
                
    lb= Label(space,text ='Unknown:',bg = 'white',fg = 'darkgreen',font = tkinter.font.Font(family = 'Corbel',size = 15,weight = 'bold'))
    space.window_create('end',window =lb)
    space.insert('end','\n')
    global unknown_files
    global unknown_images
    unknown_images = []

    print(len(unknown))
    for i in unknown:
        url = i
        image_bytes = urlopen(url).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
        pil_image = Image.open(data_stream)
        pil_image = pil_image.resize((100, 100), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(pil_image)
        unknown_images.append(tk_image)

    j = 0
    for i in unknown:
        a = tkinter.IntVar()
        
        if (re.search(r'\.(...)$',i).group()=='.jpg' or re.search(r'\.(...)$',i).group()=='.png'):
                  
            cb = Checkbutton(textframe,image = unknown_images[j],bg = 'white',fg= 'red',variable = a)
            j+=1
        
        else:
                    
            cb = Checkbutton(textframe,bg = 'white',fg= 'red',variable = a,text = '{}'.format(str(i)[-40:]),font = tkinter.font.Font(family = 'Segoe Print',size = 9))
        unknown_files[i] = a
        space.window_create("end",window = cb)
        space.insert('end','')
        space.update()
        

    scb.config(command = space.yview)
    status.grid_forget()
    download_btn.pack(side = 'left')
    download_frame.grid(row = 12,columnspan = 2 ,padx = 3,pady =3)
    indeterminate_progressbar.grid_remove()
    root.update()
    

def browser(s):
    webbrowser.open(s,new = True);
def OPEN():
    global dlocation
    os.startfile(dlocation);

go = Button(buttonframe,text = 'GO --> ',fg= 'black', bg ='green',padx=3,pady=3)
go.configure(command = check)
go.pack(side='left')

def stop():
    
    PFRAME.grid_forget()
    down.grid_forget()
    global stop
    stop = True;


root.protocol("WM_DELETE_WINDOW",callback)
root.resizable(width= False ,height = False)
root.mainloop()
