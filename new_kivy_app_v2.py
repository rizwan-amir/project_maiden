from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

import pandas as pd
import numpy as np
import cv2
Window.clearcolor=(255/255.0,182/255.0,193/255.0,0)
#Window.clearcolor=(255/255.0,255/255.0,255/255.0,0)


def getColorName(R,G,B):      
        global cname, r_pro,g_pro,b_pro
        minimum = 100
    #print(csv)
        for i in range(len(csv)-2):
            d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
            if(d<=minimum):
                minimum = d
                cname = csv.loc[i,"BRAND"]
                r_pro=int(csv.loc[i,"R"])
                g_pro=int(csv.loc[i,"G"])
                b_pro=int(csv.loc[i,"B"])
                

        
def getShadeName(R,G,B):    
        global dname
        minimum = 100
        print(len(csv))
        for i in range(len(csv)-2):
            d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
            if(d<=minimum):
                minimum = d
                dname=csv.loc[i,"SHADES NAMES"]

index_7=["BRAND","NAME","SHADES NAMES","TYPE","R","G","B"]
index_6=["BRAND","NAME","SHADES NAMES","R","G","B"]
csvp_eyeshades = pd.read_csv(r'eyeshades2.csv', names=index_7, header=None, encoding='latin1')
csvp_haircolor = pd.read_csv(r'haircolor.csv', names=index_6, header=None, encoding='latin1')
csvp_nailpolish = pd.read_csv(r'nailpolish.csv', names=index_6, header=None, encoding='latin1')
csvp_lipstick = pd.read_csv(r'lipsticks.csv', names=index_6, header=None, encoding='latin1')
a=[]
b=[]
c=[]
d=[]

#@staticmethod
def make_csv_eyeshades(a):
        #print(a)
        df2 = pd.DataFrame()
        global csv
       # print(df2)
        
        for el in a:
                
                if el==1:
                    df2=df2.append(csvp_eyeshades.loc[0:418,:], ignore_index=True)
                if el==2:
                    df2=df2.append(csvp_eyeshades.loc[419:514,:], ignore_index=True)
                if el==3:
                    df2=df2.append(csvp_eyeshades.loc[515:590,:], ignore_index=True)
                if el==4:
                    df2=df2.append(csvp_eyeshades.loc[591:602,:], ignore_index=True)
                if el==5:
                    df2=df2.append(csvp_eyeshades.loc[603:843,:], ignore_index=True)
          
        df2.to_csv('csv.csv')
        csv = pd.read_csv(r'csv.csv', names=index_7, header=None, encoding='latin1')
        print(csv)
        a.clear()

def make_csv_haircolor(d):
        
        df3 = pd.DataFrame()
        global csv

        for el in d:
                
                if el==1:
                    df3=df3.append(csvp_haircolor.loc[0:40,:], ignore_index=True)
                if el==2:
                    df3=df3.append(csvp_haircolor.loc[41:101,:], ignore_index=True)
                  
        df3.to_csv('csv.csv')
        csv = pd.read_csv(r'csv.csv', names=index_6, header=None, encoding='latin1')
        print(csv)

def make_csv_nailpolish(p):
        df4 = pd.DataFrame()
        global csv
        for p in c:        
                if p==1:
                    df4=df4.append(csvp_nailpolish.loc[0:198,:], ignore_index=True)
                if p==2:
                    df4=df4.append(csvp_nailpolish.loc[199:265,:], ignore_index=True)
                if p==3:
                    df4=df4.append(csvp_nailpolish.loc[266:775,:], ignore_index=True)
                if p==4:
                    df4=df4.append(csvp_nailpolish.loc[776:877,:], ignore_index=True)
                if p==5:
                    df4=df4.append(csvp_nailpolish.loc[878:913,:], ignore_index=True)
                  
        df4.to_csv('csv.csv')
        csv = pd.read_csv(r'csv.csv', names=index_6, header=None, encoding='latin1')
        print(csv)

def make_csv_lipstick(b):
        df5 = pd.DataFrame()
        global csv
        for p in b:
                
                if p==1:
                    df5=df5.append(csvp_lipstick.loc[0:10,:], ignore_index=True)
                if p==2:
                    df5=df5.append(csvp_lipstick.loc[11:26,:], ignore_index=True)
                if p==3:
                    df5=df5.append(csvp_lipstick.loc[27:109,:], ignore_index=True)
                if p==4:
                    df5=df5.append(csvp_lipstick.loc[110:211,:], ignore_index=True)
                if p==5:
                    df5=df5.append(csvp_lipstick.loc[212:280,:], ignore_index=True)
                  
        df5.to_csv('csv.csv')
        csv = pd.read_csv(r'csv.csv', names=index_6, header=None, encoding='latin1')
        print(csv)

class MyPopup(Popup):
        pic_add=StringProperty('none')
        def selected(self, filename):
                global pic_add
                try:
                    self.ids.uploaded_pic.source=filename[0]
                    pic_add=filename[0]
                    return pic_add
                    
                except:
                    pass
        def __init__(self,screen,**kwargs):
                super(MyPopup,self).__init__(**kwargs)
                self.screen = screen
                
class ZeroWindow(Screen):
     def selected(self, filename):
        try:
            self.ids.uploaded_pic.source=filename[0]
           
        except:
            pass
     def __init__(self,**kwargs):
        super(ZeroWindow,self).__init__(**kwargs)
        self.popup = MyPopup(self)
class FirstWindow(Screen):
        pass
    
class SecondWindow(Screen):
     def radiobox_click1(self,instance,value):
        p=1
        print(value)
        
class ThirdWindow_haircolor(Screen):
     global d
     def checkbox_click1(self,instance,value):
        p=1
        if value==True:
            d.append(p)    
                       
     def checkbox_click2(self,instance,value):
        p=2
        if value==True:
            d.append(p)
     def make_csv_haircolor_outer(self, instance):
            make_csv_haircolor(d)
    

class ThirdWindow_nailpolish(Screen):
    global c
    def checkbox_click1(self,instance,value):
        p=1
        if value==True:
            c.append(p)      
                       
    def checkbox_click2(self,instance,value):
        p=2
        if value==True:
            c.append(p) 
    def checkbox_click3(self,instance,value):
        p=3
        if value==True:
            c.append(p) 
    def checkbox_click4(self,instance,value):
        p=4
        if value==True:
            c.append(p) 
    def checkbox_click5(self,instance,value):
        p=5
        if value==True:
            c.append(p)
    def make_csv_nailpolish_outer(self, instance):
            make_csv_nailpolish(c)
            
class ThirdWindow_lipstick(Screen):
    global b
    def checkbox_click1(self,instance,value):
        p=1
        if value==True:
            b.append(p)      
                       
    def checkbox_click2(self,instance,value):
        p=2
        if value==True:
            b.append(p) 
    def checkbox_click3(self,instance,value):
        p=3
        if value==True:
            b.append(p) 
    def checkbox_click4(self,instance,value):
        p=4
        if value==True:
            b.append(p) 
    def checkbox_click5(self,instance,value):
        p=5
        if value==True:
            b.append(p)
    def make_csv_lipstick_outer(self, instance):
            make_csv_lipstick(b)
            
          
class ThirdWindow_eyeshades(Screen):
    global a  
    def checkbox_click1(self,instance,value):      
        
        p=1
        
        if value==True:
            a.append(p)   
                       
                       
    def checkbox_click2(self,instance,value):
        p=2
        if value==True:
            a.append(p)
            
    def checkbox_click3(self,instance,value):
        p=3
        if value==True:
            a.append(p)
            
    def checkbox_click4(self,instance,value):
        p=4
        if value==True:
            a.append(p)
            
    def checkbox_click5(self,instance,value):
        p=5
        if value==True:
            a.append(p)
          
            
    def make_csv_eyeshades_outer(self, instance):
            make_csv_eyeshades(a)
        
    
            
class FourthWindow(Screen):
    def __init__(self,**kwargs):
        super(FourthWindow,self).__init__(**kwargs)
        self.popup = MyPopup(self)
    def clear_csv(self,intance):
        f = open("csv.csv", "w")
        f.truncate()
        f.close()
    
       
    total_string="placeholder"      
    def coordinate(self,touch,xx,yy):
        total_string=StringProperty('h')
        r=NumericProperty(0)
        b=NumericProperty(0)
        g=NumericProperty(0)
        #print(self.popup.pic_add)
        
        
        if self.collide_point(*touch.pos):
            
            print(touch.pos)
            path=str(self.manager.ids.fourthw.ids.imi.source)
            print(""+path)
            img_path = r""+path
            img = cv2.imread(img_path)
            #print(img.size())
            #print(touch.pos[0])
            #print(touch.pos[1])
            '''
            im_x = (self.size[0] - img.shape[1]) / 2.0 + self.x
            im_y = (self.size[1] - img.shape[0]) / 2.0 + self.y
            print(im_x)
            print(im_y)
            # touch coordinates relative to image location
            im_touch_x = touch.x - im_x
            im_touch_y = touch.y - im_y
            '''
            #width:800, height:600
            width = int(xx)
            height = int(yy)
            print("width:",width,"height:",height)
            dim = (width, height)
            img = cv2.resize(img, dim)            
            print(img.shape)
            print(touch.y)
            b,g,r = img[height-int(touch.y),int(touch.x)]
            print("blue:",b)
            print("green:",g)
            print("red:",r)
            
            #print(self.ids)

            print("x axis coordinate:",touch.x)
            print("y axis coordinate:",touch.y)
            getColorName(r,g,b)
            getShadeName(r,g,b)
            b=int(b)
            g=int(g)
            r=int(r)
            
            #cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
            #cv2.imshow("image",img)
            #img_new=img[int(touch.y):int(touch.y)+400, int(touch.x):int(touch.x)+400]
            #cv2.imshow("image_new",img_new)
            total_string="Brand:" + cname  + "\nShade:" +dname
            total_string=str(total_string)
            #self.manager.ids.fifthw.ids.fifth_window_text.text=total_string
            self.ids.prod_name.text=total_string
            self.ids.cc_button.background_normal=''
            self.ids.cc_button.background_color=(r/255,g/255,b/255,1)
            
            self.ids.pro_button.background_normal=''
            self.ids.pro_button.background_color=(r_pro/255,g_pro/255,b_pro/255,1)
            #self.manager.ids.fourthw.ids.canvas_layout.my_color=(r/255,g/255,b/255,1)
            #self.manager.ids.fifthw.ids.fifth_window_text.text= total_string
           
            #print(self.manager.ids.fourthw)
            #self.manager.ids.fourthw.ids.cc_button.background_normal=''
            #self.manager.ids.fourthw.ids.cc_button.background_color=(r/255,g/255,b/255,1)
             #print(self.manager.ids.fourthw.ids)
            
            #self.manager.ids.fourthw.canvas.my_color=(r/255,g/255,b/255,1)
             
            #self.manager.ids.fourthw.ids.rect.background_normal=''
            #self.manager.ids.fourthw.ids.rect.color=(r/255,g/255,b/255,1)

            #print(self.manager.ids.secondw.ids.second_window_text)
            #self.ids.prod_name.text=total_string
            #print(self.manager.ids.fourthw)
     
             
         
    
   # def coordinate(self, touch):
    #    if self.collide_point(*touch.pos):
     #            print('Relative: {}'.format(self.to_local(*args[1].pos)))
        # The touch has occurred inside the widgets area. Do stuff!

class FifthWindow(Screen):
        total_string=StringProperty('h')
        def name_of_product(self):
                 return self.manager.ids.fourthw.ids.prod_name.text                
   

class ScreenManagement(ScreenManager):
        pass
    
#Builder.load_file('MAIDENv2.kv')

    

class MAIDENv2App(App):
    
    
    def build(self):
        
        return ScreenManagement()
if __name__ =='__main__':       

        MAIDENv2App().run()
