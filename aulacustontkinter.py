import customtkinter as ctk

janela = ctk.CTk()
janela.geometry('500x500')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

txt1 = ctk.CTkLabel(janela,text= 'Olá! Seja bem-vindo')
txt1.pack()
txt1.place(x=215,y=10)

input1 = ctk.CTkEntry(janela,placeholder_text='Digite aqui')
input1.pack()
input1.place(x=200,y=200)

bnt1 = ctk.CTkButton(janela, text="entrar",)
bnt1.pack()
bnt1.place(x=200,y=230) 
janela.mainloop()

txt2 = ctk.CTkLabel(janela,text= 'Obrigada por estar aqui!')
txt2.pack()
txt2.place(x=450,y=110)