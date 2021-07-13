import tkinter

def btn_check():
    
    price_sum = 0
    for i in range(4):
        if ck_val[i].get() == True:
            
            price_sum = price_sum + PRICE[i]
            text.insert("1.0", LIST[i] + " 항목이 선택됨\n")
            
            
  
   
    text.insert("end", "레벨은 " +  str(price_sum) + "입니다.")
    
  
    
win = tkinter.Tk()
win.title("Stence")
win.geometry("500x500")


LIST = ["3학년",
        "4학년",
        "5학년",
        "6학년"]

PRICE = [1,2,3,4]

ck_val = [None]*4
ck_btn = [None]*4

label = tkinter.Label(text="학년을 선택 후 확인을 클릭하세요.", font=("System",20))
label.place(x = 100, y = 20)


text = tkinter.Text(width=40, height=5, font=("System",20))
text.place(x = 100, y = 50)

for i in range(4):
    ck_val[i] = tkinter.BooleanVar()
    ck_val[i].set(False)
    ck_btn[i] = tkinter.Checkbutton(text=LIST[i], font=("System", 20),
                                 variable=ck_val[i])
    ck_btn[i].place(x = 100, y = 150+50*i)

submit = tkinter.Button(text="확인", font=("System", 20), command=btn_check)
submit.place(x = 100, y = 350)
    
win.mainloop()
