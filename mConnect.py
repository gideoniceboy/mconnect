from tkinter import *
import numpy as n
import cv2 as cv
import requests as r

#created by Morphine
#creating screen


class App:
	"""docstring for ClassName"""
	def __init__(self):
		self.root = Tk()
		self.root.geometry("500x400+400+90")
		self.root.title("mConnect")
		self.root.resizable(0,0)
		self.root.configure(background="powder blue")


		#menu bar
		self.menu_bar = Menu(self.root,tearoff=0)
		self.file_menu = Menu(self.menu_bar,tearoff=0)
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Exit",command=exit)
		self.menu_bar.add_cascade(label="File",menu=self.file_menu)
		#configure
		self.settings = Menu(self.menu_bar,tearoff=0)
		self.menu_bar.add_cascade(label="Configure",menu=self.settings)

		#about
		self.about = Menu(self.menu_bar,tearoff=0)
		self.about.add_command(label="Version",command=self.version)
		self.about.add_command(label="About",command=self.about_bar)
		self.menu_bar.add_cascade(label="Help",menu=self.about)

		#Themes 1. hacker theme
		self.hacker = Menu(self.menu_bar,tearoff=0)
		self.hacker.add_command(label="Morphix",command=self.morphix)
		self.hacker.add_command(label="Hacker",command=self.hacker_theme)
		#self.acker.add_command(label="Turk",command=turk)
		self.hacker.add_command(label="Default",command=self.default)
		self.settings.add_cascade(label="Theme",menu=self.hacker)
		self.root.config(menu=self.menu_bar)

		#canvas
		self.c = Canvas(self.root,width=500,height=500,bg="powder blue")
		self.c.pack()
		self.c1 = Canvas(self.root,width=500,height=500,bg="powder blue")
		self.c1.pack()

		#bottom frame
		self.f = Frame(self.root,width=500,height=100,bg="steel Blue")
		self.f.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

		self.l1=Label(self.c,text="Smart Android Webcam Connect",bg="powder blue",fg="white",font=("arial",10,"bold"))
		self.l1.grid(row=0,column=0)

		self.l2=Label(self.f,text="Powered by @morphine",bg="steel Blue",fg="white",font=("arial",10,"italic"))
		self.l2.pack(side=BOTTOM)



		self.btn = Button(self.f,text="Connect",fg="white",bg="steel Blue",padx=70,pady=70,command=self.onclick,font=("arial",10,"bold"))
		self.btn.place(relx=0.25,rely=0.25)

		self.btn1 = Button(self.f,text="Exit the Program",fg="white",bg="steel Blue",padx=10,pady=10,command=exit,font=("arial",6,"bold"))
		self.btn1.place(relx=0.75,rely=0.85)

		self.btn3 = Button(self.f,text="How Do i Connect?",fg="white",bg="steel Blue",padx=10,pady=10,command=self.how,font=("arial",6,"bold"))
		self.btn3.place(relx=0.02,rely=0.85)

		self.e = Entry(self.f,bd=10,bg="powder blue",fg="blue",font=("arial",10,"bold"))
		self.e.insert(0,"192.168.43.1:8080")
		self.e.pack()

		self.l3=Label(self.f,text="Enter Your IP address here",bg="steel Blue",fg="white",font=("arial",10,"bold"))
		self.l3.pack()


		self.root.mainloop()





	def version(self):
	    self.root = Tk()
	    self.root.title("Version")
	    self.root.geometry("400x50")
	    self.root.config(bg="purple")
	    self.li = Label(self.root,text="45.01.5",font=("san serif",30,"bold"),bg="purple",fg="white")
	    self.li.pack()
	def about_bar(self):
	    self.root = Tk()
	    self.root.title("About")
	    self.root.geometry("1000x100")
	    self.root.config(bg="purple")
	    self.li = Label(self.root,text="This software was developed by gideoniceboy in 2020.",font=("san serif",20,"bold"),bg="purple",fg="white")
	    self.li.pack()
	    self.lj = Label(self.root,text="For more feeds or updates based on this software visit http://gideoniceboy.netlify.com",font=("san serif",20,"bold"),bg="purple",fg="white")
	    self.lj.pack()
	# def turk(self):
	#     self.root.config(bg="#33FF33")
	#     self.e.config(bg="#0F0F0F", fg="#33FF33",insertbackground="#33FF33")
	#     self.btn1.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	#     self.btn.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	#     self.btn3.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	#     self.f.config(bg="indigo")
	#     self.c.config(bg="#33FF33")
	#     self.c1.config(bg="#33FF33")
	#     self.l1.config(bg="#33FF33",fg="indigo")
	#     self.l2.config(bg="#33FF33",fg="indigo")
	#     self.l3.config(bg="indigo",fg="white")
	def default(self):
	    self.root.config(bg="powder blue")
	    self.e.config(bg="powder blue", fg="blue",insertbackground="#33FF33")
	    self.btn1.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn3.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.f.config(bg="steel Blue")
	    self.c.config(bg="powder blue")
	    self.c1.config(bg="powder blue")
	    self.l1.config(bg="powder blue",fg="white")
	    self.l2.config(bg="steel Blue",fg="white")
	    self.l3.config(bg="steel Blue",fg="white")
	def hacker_theme(self):
	    self.root.config(bg="#0F0F0F")
	    self.e.config(bg="#0F0F0F", fg="#33FF33",insertbackground="#33FF33")
	    self.btn1.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn3.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.f.config(bg="#0F0F0F")
	    self.c.config(bg="#0F0F0F")
	    self.c1.config(bg="#0F0F0F")
	    self.l1.config(bg="#0F0F0F",fg="#FFFFFF")
	    self.l2.config(bg="#0F0F0F",fg="#FFFFFF")
	    self.l3.config(bg="#0F0F0F",fg="#FFFFFF")
	    
	def morphix(self):
	    self.root.config(bg="indigo")
	    self.e.config(bg="indigo", fg="violet",insertbackground="indigo")
	    self.btn1.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.btn3.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
	    self.f.config(bg="purple")
	    self.c.config(bg="purple")
	    self.c1.config(bg="purple")
	    self.l1.config(bg="indigo",fg="#FFFFFF")
	    self.l2.config(bg="purple",fg="#FFFFFF")
	    self.l3.config(bg="purple",fg="#FFFFFF")


	#function
	def onclick(self):
	    ip="http://"+str(self.e.get())+"/shot.jpg"

	    running = True
	    while running:
	        self.btn.config(text="Connect")
	        img = r.get(ip)
	        video = n.array(bytearray(img.content),dtype = n.uint8)
	        render = cv.imdecode(video,-1)
	        if running:
	           cv.imshow('Connected',render)
	           self.btn.config(text="Connected")
	        else:
	           cv.imshow('Lost connections',render)
	           btn.config(text="Disconnected")
	        if(cv.waitKey(1) and 0xff == ord('q')):
	            
	           break
	def how(self):
	    #creating screen
	    self.root = Tk()
	    self.root.geometry("650x150+300+10")
	    self.root.title("Help")
	    self.root.resizable(0,0)
	    self.root.configure(background="powder blue")

	    self.f = Frame(self.root,width=800,height=100,bg="steel Blue")
	    self.f.place(relwidth=0.85,relheight=0.85,relx=0.1,rely=0.1)

	    self.li=Label(self.f,text="First: download and install an ip webcam app on your mobile.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
	    self.li.grid(row=1,column=0)
	    
	    self.lj=Label(self.f,text="Second: connet your mobile hotspot to pc.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
	    self.lj.grid(row=2,column=0)
	    
	    self.lk=Label(self.f,text="Third: Open ip webcam app and press 'Start server'.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
	    self.lk.grid(row=3,column=0)

	    self.ll=Label(self.f,text="Fourth: Enter the ip address you see on your mobile and enter it on mConnect.",bg="steel Blue",fg="white",font=("arial",10,"bold")) 
	    self.ll.grid(row=4,column=0)

	    self.lm=Label(self.f,text="Last: press connect button and enjoy.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
	    self.lm.grid(row=5,column=0)
	    
	    self.root.config(menu=self.menu_bar)


apps = App()






