from tkinter import *
import util


main_window = Tk()

        
#print(keys_elm.get(1.0, "end-1c"))

main_window.title("Meta Scripts - Valorant Autolock - metascripts.org")
main_window.configure(background="#232323")
main_window.geometry("440x230")
photo = PhotoImage(file = "metalogo.png")
main_window.iconphoto(False, photo)

l_1 = Label(main_window,text="Write keys and Characters (f1-agent 1,f2-agent 2)",background="#232323",fg="#FFFFFF")
l_1.pack(padx = 10,pady=15,anchor="w")

keys_chars = Text(main_window,height=7,width=110,fg='#7F7FFF',bg="#232323")
keys_chars.pack(padx = 10,pady=1,anchor="w")
keys_chars.insert("end-1c", "f1-agent 1,f2-agent 2")




btn = Button(main_window,width=110,bg="#111111",fg='#7F7FFF',command=util.save_settings,text="Save")
btn.pack(padx = 10,pady=1,anchor="w")


main_window.mainloop()