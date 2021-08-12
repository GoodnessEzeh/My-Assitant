from tkinter import *
root=Tk()
def send():
    send="You => "+e.get()
    txt.insert(END, "\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END,"\n"+"Bot => Hi")
    elif(e.get()=="Hi"):
        txt.insert(END,"\n"+"Bot => Hello")
    elif(e.get()=="How are you?"):
        txt.insert(END,"\n"+"Bot => Fine and you?")
    elif(e.get()=="Fine"):
        txt.insert(END,"\n"+"Bot => Nice to hear")
    elif(e.get()=="Can I know you?"):
        txt.insert(END,"\n"+"Bot => Well, I am GoodBot, a personal assistant to Goodness Ezeh. I am here to answer any queries patterning my boss.")
    elif(e.get()=="Where is your boss from?"):
        txt.insert(END,"\n"+"Bot => He is from the eastern part of Nigeria.")
    elif(e.get()=="How old is he?"):
        txt.insert(END,"\n"+"Bot => He clocked 29 on the 17th of June") 
    elif(e.get()=="Where does he live?"):
        txt.insert(END,"\n"+"Bot => He lives in Ichinoseki city in Iwate prefecture in Japan.")
    elif(e.get()=="What are his hobbies?"):
        txt.insert(END,"\n"+"Bot => Nice question! He likes playing soccer, watching anime, and of course, programming.")
    elif(e.get()=="What is his favourite food?"):
        txt.insert(END,"\n"+"Bot => That should be Udon. He eats it quite often")
    elif(e.get()=="Thank you for help. See you later."):
        txt.insert(END,"\n"+"Bot => You're welcome. Do have a wonderful day ahead.")                           
    else:
        txt.insert(END,"\n"+"Bot => Sorry I didnt get it")                
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Goodness Ezeh's CHATBOT")
root.mainloop()    