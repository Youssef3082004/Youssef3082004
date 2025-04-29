from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
import cv2


root = Tk()
root.geometry("500x250+550+300")
root.config(bg="#FDFEFE")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\digital-campaign.ico")
root.title("Media Player")
root.resizable(False,False)

# =============================================================== Functions ======================================================
def open_image():
    try:
        file_path = filedialog.askopenfilename(title="OPEN",initialdir="C:\\Users\\Computec\\Pictures",filetypes=[("Imagies","*.png;*.jpg;*.jpeg;*.gif;")])
        if file_path == "": 
            messagebox.showwarning("WARNING","You didn't select the image to open")
        else:
            img = cv2.imread(file_path)
            dim = img.shape
            width= int(dim[1]/5)
            hight = int(dim[0]/5)
            new_img = cv2.resize(img,(width,hight))
            cv2.imshow("Image",new_img)    
            k = cv2.waitKey(0)
            if k == 27 :          
                cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","Something happened wrong")
        
def Gray_image():
    try:
        file_path = filedialog.askopenfilename(title="OPEN",initialdir="C:\\Users\\Computec\\Pictures",filetypes=[("Imagies","*.png;*.jpg;*.jpeg;*.gif;")])
        if file_path == "": 
            messagebox.showwarning("WARNING","You didn't select the image to open")
        else:
            img = cv2.imread(file_path,0)
            dim = img.shape
            width= int(dim[1]/5)
            hight = int(dim[0]/5)
            new_img = cv2.resize(img,(width,hight))
            cv2.imshow("Image",new_img)
            k = cv2.waitKey(0)
            if k == 27 :          
                    ques = messagebox.askyesno("Save","Do you want to save the changes you made")
                    if ques == YES:
                        cv2.imwrite(file_path,new_img)
                        cv2.destroyAllWindows()
                    else:
                        cv2.destroyAllWindows()                
    except:
        messagebox.showerror("Error","Something happened wrong")
        
           
def open_video():
        file_path = filedialog.askopenfilename(title="OPEN",initialdir="D:\\My Download",filetypes=[("Videos","*.mp4;*.ogg;*.m4v")])
        if file_path == "": 
            messagebox.showwarning("WARNING","You didn't select the video to open")
        else:
            video = cv2.VideoCapture(file_path)
            while True: 
                ret , frames = video.read()
                new_frames = cv2.resize(frames,(600,500))
                cv2.imshow("Video",new_frames)
                k = cv2.waitKey(1)
                if k == 27:
                    cv2.destroyAllWindows()
                    break 
    

def Gray_video():
        file_path = filedialog.askopenfilename(title="OPEN",initialdir="D:\\My Download",filetypes=[("Videos","*.mp4;*.ogg;*.m4v")])
        if file_path == "": 
            messagebox.showwarning("WARNING","You didn't select the video to open")
        else:
            video = cv2.VideoCapture(file_path,0)
            while True: 
                ret , frames = video.read()
                new_frames = cv2.resize(frames,(600,500))
                gray = cv2.cvtColor(new_frames,cv2.COLOR_BGR2GRAY)
                cv2.imshow("Video",gray)
                k = cv2.waitKey(1) 
                if k == 27:
                    cv2.destroyAllWindows()
                    break
            
            
def Exit(): 
   ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
   if ques == 1:
       root.destroy()
   else: 
       return
                   
# ====================================== Frames =============================================            
fr_1 = Frame(root,bg="#FDFEFE")
fr_1.place(x=0,y=105,width=500,height=500)     
       
# ====================================== Labels =============================================       
l1 = Label(root,text="Image Viewier",font=("Pacifico",15),background="Gold",fg="Black")
l1.pack(fill=X)  
l2 = Label(fr_1,text="Video Viewier",font=("Pacifico",15),background="Gold",fg="Black")
l2.pack(fill=X)

# ======================================= Buttons ===============================================
Button_1 = Button(root,text="Open",font=("Arial",14,"bold"),command=open_image,bd=4,justify="center",bg="#2ECC71")
Button_1.place(x=180,y=55,width=70,height=40) 

Button_2 =Button(root,text="Filter",font=("Arial",14,"bold"),command=Gray_image,bd=4,justify="center",bg="#D0D3D4") 
Button_2.place(x=260,y=55,width=70,height=40)

Button_3 =Button(fr_1,text="Open",font=("Arial",14,"bold"),command=open_video,bd=4,justify="center",bg="#2ECC71") 
Button_3.place(x=180,y=55,width=70,height=40)

Button_4 =Button(fr_1,text="Filter",font=("Arial",14,"bold"),command=Gray_video,bd=4,justify="center",bg="#D0D3D4") 
Button_4.place(x=260,y=55,width=70,height=40)

Button_5 =Button(fr_1,text="EXIT",font=("Arial",14,"bold"),command=Exit,bd=4,justify="center",bg="red") 
Button_5.place(x=220,y=100,width=70,height=40)

root.mainloop()