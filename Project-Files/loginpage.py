from  tkinter import *
from tkinter import messagebox
import mysql.connector
import dbConnect
from dbConnect import DBConnect
def main():
   def myfieldopen_fun(nameFIELD,NAMEVILLAGE):
      user1 = nameFIELD
      import sys
      import mysql.connector

      try:
          import Tkinter as tk
      except ImportError:
          import tkinter as tk

      try:
          import ttk
          py3 = False
      except ImportError:
          import tkinter.ttk as ttk
          py3 = True

      import myfield_data_support

      def vp_start_gui():
          '''Starting point when module is the main routine.'''
          global val, w, root
          root = tk.Tk()
          top = Toplevel1 (root)
          myfield_data_support.init(root, top)
          root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
          '''Starting point when module is imported by another program.'''
          global w, w_win, rt
          rt = root
          w = tk.Toplevel (root)
          top = Toplevel1 (w)
          myfield_data_support.init(w, top, *args, **kwargs)
          return (w, top)

      def destroy_Toplevel1():
          global w
          w.destroy()
          w = None

      class Toplevel1:
          def imports_my_1(self):
              mydb=mysql.connector.connect(host='db4free.net',user='sfmvitpune_ser',password='pk9423975167',database='sfmvitpune_db',port='3306')
              #msg = tk.messagebox.showinfo('SFAVIT','MySQL Database Connection successful')
              mycursor=mydb.cursor()
              query = ("SELECT userid , passkey , namei ,village ,district , avg_evi ,max_evi ,last_evi ,evi_year_average_value ,avg_ndwi ,max_ndwi ,last_ndwi ,ndwi_year_average_value ,avg_msavi ,max_msavi ,last_msavi ,msavi_year_average_value ,avg_rainfall  FROM INDIA2019 WHERE userid = \'"+user1+"\'")
              mycursor.execute(query)
              for(userid , passkey , namei ,village ,district , avg_evi ,max_evi ,last_evi ,evi_year_average_value ,avg_ndwi ,max_ndwi ,last_ndwi ,ndwi_year_average_value ,avg_msavi ,max_msavi ,last_msavi ,msavi_year_average_value ,avg_rainfall) in mycursor:
                  print(userid,max_evi)
                  avg_evi = str(avg_evi)
                  max_evi = str(max_evi)
                  last_evi = str(last_evi)
                  evi_year_average_value = str(evi_year_average_value)

                  avg_msavi = str(avg_msavi)
                  max_msavi = str(max_msavi)
                  last_msavi = str(last_msavi)
                  msavi_year_average_value = str(msavi_year_average_value)

                  avg_ndwi = str(avg_ndwi)
                  max_ndwi = str(max_ndwi)
                  last_ndwi = str(last_ndwi)
                  ndwi_year_average_value = str(ndwi_year_average_value)



                  self.AVG_NDVI_my.insert(1.0,avg_evi)
                  self.MAX_NDVI_my.insert(1.0,max_evi)
                  self.LAST_NDVI_my.insert(1.0,last_evi)
                  self.YEAR_NDVI_my.insert(1.0,evi_year_average_value)

                  self.AVG_NDWI_my.insert(1.0,avg_ndwi)
                  self.MAX_NDWI_my.insert(1.0,max_ndwi)
                  self.LAST_NDWI_my.insert(1.0,last_ndwi)
                  self.YEAR_NDWI_my.insert(1.0,ndwi_year_average_value)

                  self.AVG_MSAVI_my.insert(1.0,avg_msavi)
                  self.MAX_MSAVI_my.insert(1.0,max_msavi)
                  self.LAST_MSAVI_my.insert(1.0,last_msavi)
                  self.YEAR_MSAVI_my.insert(1.0,msavi_year_average_value)

                  self.username_my.insert(1.0,userid)
                  self.name_myf.insert(1.0,namei)
                  self.village_myf.insert(1.0,village)
                  self.dist_myf.insert(1.0,district)


          def backmys(self):
              root.destroy()
              mainscreen()

          def __init__(self, top=None):
              '''This class configures and populates the toplevel window.
                 top is the toplevel containing window.'''
              _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
              _fgcolor = '#000000'  # X11 color: 'black'
              _compcolor = '#d9d9d9' # X11 color: 'gray85'
              _ana1color = '#d9d9d9' # X11 color: 'gray85'
              _ana2color = '#ececec' # Closest X11 color: 'gray92'
              font12 = "-family Ringbearer -size 13 -weight bold -slant "  \
                  "roman -underline 0 -overstrike 0"
              font15 = "-family Rockwell -size 13 -weight bold -slant roman "  \
                  "-underline 0 -overstrike 0"
              font21 = "-family TR -size 21 -weight bold -slant roman "  \
                  "-underline 0 -overstrike 0"

              top.geometry("905x626+114+114")
              top.minsize(124, 1)
              top.maxsize(1596, 873)
              top.resizable(1, 1)
              top.title("New Toplevel")
              top.configure(background="#616161")

              self.Frame1 = tk.Frame(top)
              self.Frame1.place(relx=0.298, rely=0.032, relheight=0.12, relwidth=0.337)

              self.Frame1.configure(relief='ridge')
              self.Frame1.configure(borderwidth="10")
              self.Frame1.configure(relief="ridge")
              self.Frame1.configure(background="#008080")
              self.Frame1.configure(cursor="fleur")

              self.Label1 = tk.Label(self.Frame1)
              self.Label1.place(relx=0.197, rely=0.267, height=36, width=204)
              self.Label1.configure(background="#d9d9d9")
              self.Label1.configure(disabledforeground="#a3a3a3")
              self.Label1.configure(font=font21)
              self.Label1.configure(foreground="#000000")
              self.Label1.configure(text='''MY FIELD''')

              self.Frame2 = tk.Frame(top)
              self.Frame2.place(relx=0.133, rely=0.176, relheight=0.264
                      , relwidth=0.646)
              self.Frame2.configure(relief='sunken')
              self.Frame2.configure(borderwidth="10")
              self.Frame2.configure(relief="sunken")
              self.Frame2.configure(background="#008080")

              self.Label2 = tk.Label(self.Frame2)
              self.Label2.place(relx=0.085, rely=0.121, height=26, width=70)
              self.Label2.configure(background="#008080")
              self.Label2.configure(cursor="fleur")
              self.Label2.configure(disabledforeground="#a3a3a3")
              self.Label2.configure(font=font15)
              self.Label2.configure(foreground="#ffff00")
              self.Label2.configure(text='''Name :''')

              self.Label2_6 = tk.Label(self.Frame2)
              self.Label2_6.place(relx=0.171, rely=0.667, height=26, width=370)
              self.Label2_6.configure(activebackground="#f9f9f9")
              self.Label2_6.configure(activeforeground="black")
              self.Label2_6.configure(background="#008080")
              self.Label2_6.configure(cursor="fleur")
              self.Label2_6.configure(disabledforeground="#a3a3a3")
              self.Label2_6.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_6.configure(foreground="#ffff00")
              self.Label2_6.configure(highlightbackground="#d9d9d9")
              self.Label2_6.configure(highlightcolor="black")
              self.Label2_6.configure(text='''______________________________________''')

              self.Label2_8 = tk.Label(self.Frame2)
              self.Label2_8.place(relx=0.085, rely=0.485, height=26, width=80)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''District :''')

              self.Label2_9 = tk.Label(self.Frame2)
              self.Label2_9.place(relx=0.085, rely=0.303, height=26, width=70)
              self.Label2_9.configure(activebackground="#f9f9f9")
              self.Label2_9.configure(activeforeground="black")
              self.Label2_9.configure(background="#008080")
              self.Label2_9.configure(disabledforeground="#a3a3a3")
              self.Label2_9.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_9.configure(foreground="#ffff00")
              self.Label2_9.configure(highlightbackground="#d9d9d9")
              self.Label2_9.configure(highlightcolor="black")
              self.Label2_9.configure(text='''Village :''')

              self.name_myf = tk.Text(self.Frame2)
              self.name_myf.place(relx=0.239, rely=0.121, relheight=0.145
                      , relwidth=0.554)
              self.name_myf.configure(background="white")
              self.name_myf.configure(font="TkTextFont")
              self.name_myf.configure(foreground="black")
              self.name_myf.configure(highlightbackground="#d9d9d9")
              self.name_myf.configure(highlightcolor="black")
              self.name_myf.configure(insertbackground="black")
              self.name_myf.configure(selectbackground="#c4c4c4")
              self.name_myf.configure(selectforeground="black")
              self.name_myf.configure(wrap="word")

              self.dist_myf = tk.Text(self.Frame2)
              self.dist_myf.place(relx=0.239, rely=0.485, relheight=0.145
                      , relwidth=0.554)
              self.dist_myf.configure(background="white")
              self.dist_myf.configure(font="TkTextFont")
              self.dist_myf.configure(foreground="black")
              self.dist_myf.configure(highlightbackground="#d9d9d9")
              self.dist_myf.configure(highlightcolor="black")
              self.dist_myf.configure(insertbackground="black")
              self.dist_myf.configure(selectbackground="#c4c4c4")
              self.dist_myf.configure(selectforeground="black")
              self.dist_myf.configure(wrap="word")

              self.village_myf = tk.Text(self.Frame2)
              self.village_myf.place(relx=0.239, rely=0.303, relheight=0.145
                      , relwidth=0.554)
              self.village_myf.configure(background="white")
              self.village_myf.configure(font="TkTextFont")
              self.village_myf.configure(foreground="black")
              self.village_myf.configure(highlightbackground="#d9d9d9")
              self.village_myf.configure(highlightcolor="black")
              self.village_myf.configure(insertbackground="black")
              self.village_myf.configure(selectbackground="#c4c4c4")
              self.village_myf.configure(selectforeground="black")
              self.village_myf.configure(wrap="word")

              self.import_my = tk.Button(top)
              self.import_my.place(relx=0.044, rely=0.064, height=34, width=77)
              self.import_my.configure(activebackground="#ff0000")
              self.import_my.configure(activeforeground="white")
              self.import_my.configure(activeforeground="#000000")
              self.import_my.configure(background="#ff0000")
              self.import_my.configure(disabledforeground="#a3a3a3")
              self.import_my.configure(foreground="#ffffff")
              self.import_my.configure(highlightbackground="#d9d9d9")
              self.import_my.configure(highlightcolor="black")
              self.import_my.configure(pady="0")
              self.import_my.configure(text='''IMPORT''',command = self.imports_my_1)

              self.back_my = tk.Button(top)
              self.back_my.place(relx=0.155, rely=0.064, height=34, width=77)
              self.back_my.configure(activebackground="#ececec")
              self.back_my.configure(activeforeground="#000000")
              self.back_my.configure(background="#008000")
              self.back_my.configure(disabledforeground="#a3a3a3")
              self.back_my.configure(foreground="#ffffff")
              self.back_my.configure(highlightbackground="#d9d9d9")
              self.back_my.configure(highlightcolor="black")
              self.back_my.configure(pady="0")
              self.back_my.configure(text='''BACK''',command = self.backmys)

              self.Frame3 = tk.Frame(top)
              self.Frame3.place(relx=0.685, rely=0.032, relheight=0.12, relwidth=0.193)

              self.Frame3.configure(relief='sunken')
              self.Frame3.configure(borderwidth="10")
              self.Frame3.configure(relief="sunken")
              self.Frame3.configure(background="#008080")

              self.username_my = tk.Text(self.Frame3)
              self.username_my.place(relx=0.229, rely=0.267, relheight=0.453
                      , relwidth=0.537)
              self.username_my.configure(background="white")
              self.username_my.configure(font=font12)
              self.username_my.configure(foreground="black")
              self.username_my.configure(highlightbackground="#d9d9d9")
              self.username_my.configure(highlightcolor="black")
              self.username_my.configure(insertbackground="black")
              self.username_my.configure(selectbackground="#c4c4c4")
              self.username_my.configure(selectforeground="black")
              self.username_my.configure(wrap="word")

              self.Frame4 = tk.Frame(top)
              self.Frame4.place(relx=0.022, rely=0.463, relheight=0.248
                      , relwidth=0.436)
              self.Frame4.configure(relief='sunken')
              self.Frame4.configure(borderwidth="10")
              self.Frame4.configure(relief="sunken")
              self.Frame4.configure(background="#008080")

              self.Label2_6 = tk.Label(self.Frame4)
              self.Label2_6.place(relx=0.101, rely=0.129, height=26, width=140)
              self.Label2_6.configure(activebackground="#f9f9f9")
              self.Label2_6.configure(activeforeground="black")
              self.Label2_6.configure(background="#008080")
              self.Label2_6.configure(disabledforeground="#a3a3a3")
              self.Label2_6.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_6.configure(foreground="#ffff00")
              self.Label2_6.configure(highlightbackground="#d9d9d9")
              self.Label2_6.configure(highlightcolor="black")
              self.Label2_6.configure(text='''Average NDVI :''')

              self.Label2_7 = tk.Label(self.Frame4)
              self.Label2_7.place(relx=0.051, rely=0.71, height=26, width=180)
              self.Label2_7.configure(activebackground="#f9f9f9")
              self.Label2_7.configure(activeforeground="black")
              self.Label2_7.configure(background="#008080")
              self.Label2_7.configure(disabledforeground="#a3a3a3")
              self.Label2_7.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_7.configure(foreground="#ffff00")
              self.Label2_7.configure(highlightbackground="#d9d9d9")
              self.Label2_7.configure(highlightcolor="black")
              self.Label2_7.configure(text='''Last Year Average :''')

              self.Label2_7 = tk.Label(self.Frame4)
              self.Label2_7.place(relx=0.101, rely=0.516, height=26, width=130)
              self.Label2_7.configure(activebackground="#f9f9f9")
              self.Label2_7.configure(activeforeground="black")
              self.Label2_7.configure(background="#008080")
              self.Label2_7.configure(disabledforeground="#a3a3a3")
              self.Label2_7.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_7.configure(foreground="#ffff00")
              self.Label2_7.configure(highlightbackground="#d9d9d9")
              self.Label2_7.configure(highlightcolor="black")
              self.Label2_7.configure(text='''Latest NDVI :''')

              self.Label2_7 = tk.Label(self.Frame4)
              self.Label2_7.place(relx=0.076, rely=0.323, height=26, width=150)
              self.Label2_7.configure(activebackground="#f9f9f9")
              self.Label2_7.configure(activeforeground="black")
              self.Label2_7.configure(background="#008080")
              self.Label2_7.configure(disabledforeground="#a3a3a3")
              self.Label2_7.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_7.configure(foreground="#ffff00")
              self.Label2_7.configure(highlightbackground="#d9d9d9")
              self.Label2_7.configure(highlightcolor="black")
              self.Label2_7.configure(text='''Maximum NDVI :''')

              self.AVG_NDVI_my = tk.Text(self.Frame4)
              self.AVG_NDVI_my.place(relx=0.532, rely=0.129, relheight=0.155
                      , relwidth=0.415)
              self.AVG_NDVI_my.configure(background="white")
              self.AVG_NDVI_my.configure(cursor="fleur")
              self.AVG_NDVI_my.configure(font="TkTextFont")
              self.AVG_NDVI_my.configure(foreground="black")
              self.AVG_NDVI_my.configure(highlightbackground="#d9d9d9")
              self.AVG_NDVI_my.configure(highlightcolor="black")
              self.AVG_NDVI_my.configure(insertbackground="black")
              self.AVG_NDVI_my.configure(selectbackground="#c4c4c4")
              self.AVG_NDVI_my.configure(selectforeground="black")
              self.AVG_NDVI_my.configure(wrap="word")

              self.MAX_NDVI_my = tk.Text(self.Frame4)
              self.MAX_NDVI_my.place(relx=0.532, rely=0.323, relheight=0.155
                      , relwidth=0.415)
              self.MAX_NDVI_my.configure(background="white")
              self.MAX_NDVI_my.configure(font="TkTextFont")
              self.MAX_NDVI_my.configure(foreground="black")
              self.MAX_NDVI_my.configure(highlightbackground="#d9d9d9")
              self.MAX_NDVI_my.configure(highlightcolor="black")
              self.MAX_NDVI_my.configure(insertbackground="black")
              self.MAX_NDVI_my.configure(selectbackground="#c4c4c4")
              self.MAX_NDVI_my.configure(selectforeground="black")
              self.MAX_NDVI_my.configure(wrap="word")

              self.LAST_NDVI_my = tk.Text(self.Frame4)
              self.LAST_NDVI_my.place(relx=0.532, rely=0.516, relheight=0.155
                      , relwidth=0.415)
              self.LAST_NDVI_my.configure(background="white")
              self.LAST_NDVI_my.configure(font="TkTextFont")
              self.LAST_NDVI_my.configure(foreground="black")
              self.LAST_NDVI_my.configure(highlightbackground="#d9d9d9")
              self.LAST_NDVI_my.configure(highlightcolor="black")
              self.LAST_NDVI_my.configure(insertbackground="black")
              self.LAST_NDVI_my.configure(selectbackground="#c4c4c4")
              self.LAST_NDVI_my.configure(selectforeground="black")
              self.LAST_NDVI_my.configure(wrap="word")

              self.YEAR_NDVI_my = tk.Text(self.Frame4)
              self.YEAR_NDVI_my.place(relx=0.532, rely=0.71, relheight=0.155
                      , relwidth=0.415)
              self.YEAR_NDVI_my.configure(background="white")
              self.YEAR_NDVI_my.configure(font="TkTextFont")
              self.YEAR_NDVI_my.configure(foreground="black")
              self.YEAR_NDVI_my.configure(highlightbackground="#d9d9d9")
              self.YEAR_NDVI_my.configure(highlightcolor="black")
              self.YEAR_NDVI_my.configure(insertbackground="black")
              self.YEAR_NDVI_my.configure(selectbackground="#c4c4c4")
              self.YEAR_NDVI_my.configure(selectforeground="black")
              self.YEAR_NDVI_my.configure(wrap="word")

              self.Frame4_5 = tk.Frame(top)
              self.Frame4_5.place(relx=0.475, rely=0.463, relheight=0.248
                      , relwidth=0.436)
              self.Frame4_5.configure(relief='sunken')
              self.Frame4_5.configure(borderwidth="10")
              self.Frame4_5.configure(relief="sunken")
              self.Frame4_5.configure(background="#008080")
              self.Frame4_5.configure(cursor="fleur")
              self.Frame4_5.configure(highlightbackground="#d9d9d9")
              self.Frame4_5.configure(highlightcolor="black")

              self.Label2_7 = tk.Label(self.Frame4_5)
              self.Label2_7.place(relx=0.076, rely=0.129, height=26, width=150)
              self.Label2_7.configure(activebackground="#f9f9f9")
              self.Label2_7.configure(activeforeground="black")
              self.Label2_7.configure(background="#008080")
              self.Label2_7.configure(disabledforeground="#a3a3a3")
              self.Label2_7.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_7.configure(foreground="#ffff00")
              self.Label2_7.configure(highlightbackground="#d9d9d9")
              self.Label2_7.configure(highlightcolor="black")
              self.Label2_7.configure(text='''Average MSAVI :''')

              self.Label2_8 = tk.Label(self.Frame4_5)
              self.Label2_8.place(relx=0.051, rely=0.323, height=26, width=160)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Maximum MSAVI :''')

              self.Label2_8 = tk.Label(self.Frame4_5)
              self.Label2_8.place(relx=0.076, rely=0.516, height=26, width=150)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Latest MSAVI :''')

              self.Label2_8 = tk.Label(self.Frame4_5)
              self.Label2_8.place(relx=0.051, rely=0.71, height=26, width=180)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Last Year Average :''')

              self.AVG_MSAVI_my = tk.Text(self.Frame4_5)
              self.AVG_MSAVI_my.place(relx=0.532, rely=0.129, relheight=0.155
                      , relwidth=0.415)
              self.AVG_MSAVI_my.configure(background="white")
              self.AVG_MSAVI_my.configure(font="TkTextFont")
              self.AVG_MSAVI_my.configure(foreground="black")
              self.AVG_MSAVI_my.configure(highlightbackground="#d9d9d9")
              self.AVG_MSAVI_my.configure(highlightcolor="black")
              self.AVG_MSAVI_my.configure(insertbackground="black")
              self.AVG_MSAVI_my.configure(selectbackground="#c4c4c4")
              self.AVG_MSAVI_my.configure(selectforeground="black")
              self.AVG_MSAVI_my.configure(wrap="word")

              self.MAX_MSAVI_my = tk.Text(self.Frame4_5)
              self.MAX_MSAVI_my.place(relx=0.532, rely=0.323, relheight=0.155
                      , relwidth=0.415)
              self.MAX_MSAVI_my.configure(background="white")
              self.MAX_MSAVI_my.configure(font="TkTextFont")
              self.MAX_MSAVI_my.configure(foreground="black")
              self.MAX_MSAVI_my.configure(highlightbackground="#d9d9d9")
              self.MAX_MSAVI_my.configure(highlightcolor="black")
              self.MAX_MSAVI_my.configure(insertbackground="black")
              self.MAX_MSAVI_my.configure(selectbackground="#c4c4c4")
              self.MAX_MSAVI_my.configure(selectforeground="black")
              self.MAX_MSAVI_my.configure(wrap="word")

              self.LAST_MSAVI_my = tk.Text(self.Frame4_5)
              self.LAST_MSAVI_my.place(relx=0.532, rely=0.516, relheight=0.155
                      , relwidth=0.415)
              self.LAST_MSAVI_my.configure(background="white")
              self.LAST_MSAVI_my.configure(font="TkTextFont")
              self.LAST_MSAVI_my.configure(foreground="black")
              self.LAST_MSAVI_my.configure(highlightbackground="#d9d9d9")
              self.LAST_MSAVI_my.configure(highlightcolor="black")
              self.LAST_MSAVI_my.configure(insertbackground="black")
              self.LAST_MSAVI_my.configure(selectbackground="#c4c4c4")
              self.LAST_MSAVI_my.configure(selectforeground="black")
              self.LAST_MSAVI_my.configure(wrap="word")

              self.YEAR_MSAVI_my = tk.Text(self.Frame4_5)
              self.YEAR_MSAVI_my.place(relx=0.532, rely=0.71, relheight=0.155
                      , relwidth=0.415)
              self.YEAR_MSAVI_my.configure(background="white")
              self.YEAR_MSAVI_my.configure(font="TkTextFont")
              self.YEAR_MSAVI_my.configure(foreground="black")
              self.YEAR_MSAVI_my.configure(highlightbackground="#d9d9d9")
              self.YEAR_MSAVI_my.configure(highlightcolor="black")
              self.YEAR_MSAVI_my.configure(insertbackground="black")
              self.YEAR_MSAVI_my.configure(selectbackground="#c4c4c4")
              self.YEAR_MSAVI_my.configure(selectforeground="black")
              self.YEAR_MSAVI_my.configure(wrap="word")

              self.Frame4_6 = tk.Frame(top)
              self.Frame4_6.place(relx=0.243, rely=0.735, relheight=0.248
                      , relwidth=0.436)
              self.Frame4_6.configure(relief='sunken')
              self.Frame4_6.configure(borderwidth="10")
              self.Frame4_6.configure(relief="sunken")
              self.Frame4_6.configure(background="#008080")
              self.Frame4_6.configure(highlightbackground="#d9d9d9")
              self.Frame4_6.configure(highlightcolor="black")

              self.Label2_8 = tk.Label(self.Frame4_6)
              self.Label2_8.place(relx=0.076, rely=0.129, height=26, width=140)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Average NDWI :''')

              self.Label2_8 = tk.Label(self.Frame4_6)
              self.Label2_8.place(relx=0.051, rely=0.323, height=26, width=150)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Maximum NDWI :''')

              self.Label2_8 = tk.Label(self.Frame4_6)
              self.Label2_8.place(relx=0.076, rely=0.516, height=26, width=130)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Latest NDWI :''')

              self.Label2_8 = tk.Label(self.Frame4_6)
              self.Label2_8.place(relx=0.025, rely=0.71, height=26, width=180)
              self.Label2_8.configure(activebackground="#f9f9f9")
              self.Label2_8.configure(activeforeground="black")
              self.Label2_8.configure(background="#008080")
              self.Label2_8.configure(disabledforeground="#a3a3a3")
              self.Label2_8.configure(font="-family {Rockwell} -size 13 -weight bold")
              self.Label2_8.configure(foreground="#ffff00")
              self.Label2_8.configure(highlightbackground="#d9d9d9")
              self.Label2_8.configure(highlightcolor="black")
              self.Label2_8.configure(text='''Last Year Average :''')

              self.AVG_NDWI_my = tk.Text(self.Frame4_6)
              self.AVG_NDWI_my.place(relx=0.506, rely=0.129, relheight=0.155
                      , relwidth=0.415)
              self.AVG_NDWI_my.configure(background="white")
              self.AVG_NDWI_my.configure(font="TkTextFont")
              self.AVG_NDWI_my.configure(foreground="black")
              self.AVG_NDWI_my.configure(highlightbackground="#d9d9d9")
              self.AVG_NDWI_my.configure(highlightcolor="black")
              self.AVG_NDWI_my.configure(insertbackground="black")
              self.AVG_NDWI_my.configure(selectbackground="#c4c4c4")
              self.AVG_NDWI_my.configure(selectforeground="black")
              self.AVG_NDWI_my.configure(wrap="word")

              self.MAX_NDWI_my = tk.Text(self.Frame4_6)
              self.MAX_NDWI_my.place(relx=0.506, rely=0.323, relheight=0.155
                      , relwidth=0.415)
              self.MAX_NDWI_my.configure(background="white")
              self.MAX_NDWI_my.configure(font="TkTextFont")
              self.MAX_NDWI_my.configure(foreground="black")
              self.MAX_NDWI_my.configure(highlightbackground="#d9d9d9")
              self.MAX_NDWI_my.configure(highlightcolor="black")
              self.MAX_NDWI_my.configure(insertbackground="black")
              self.MAX_NDWI_my.configure(selectbackground="#c4c4c4")
              self.MAX_NDWI_my.configure(selectforeground="black")
              self.MAX_NDWI_my.configure(wrap="word")

              self.LAST_NDWI_my = tk.Text(self.Frame4_6)
              self.LAST_NDWI_my.place(relx=0.506, rely=0.516, relheight=0.155
                      , relwidth=0.415)
              self.LAST_NDWI_my.configure(background="white")
              self.LAST_NDWI_my.configure(font="TkTextFont")
              self.LAST_NDWI_my.configure(foreground="black")
              self.LAST_NDWI_my.configure(highlightbackground="#d9d9d9")
              self.LAST_NDWI_my.configure(highlightcolor="black")
              self.LAST_NDWI_my.configure(insertbackground="black")
              self.LAST_NDWI_my.configure(selectbackground="#c4c4c4")
              self.LAST_NDWI_my.configure(selectforeground="black")
              self.LAST_NDWI_my.configure(wrap="word")

              self.YEAR_NDWI_my = tk.Text(self.Frame4_6)
              self.YEAR_NDWI_my.place(relx=0.506, rely=0.71, relheight=0.155
                      , relwidth=0.415)
              self.YEAR_NDWI_my.configure(background="white")
              self.YEAR_NDWI_my.configure(font="TkTextFont")
              self.YEAR_NDWI_my.configure(foreground="black")
              self.YEAR_NDWI_my.configure(highlightbackground="#d9d9d9")
              self.YEAR_NDWI_my.configure(highlightcolor="black")
              self.YEAR_NDWI_my.configure(insertbackground="black")
              self.YEAR_NDWI_my.configure(selectbackground="#c4c4c4")
              self.YEAR_NDWI_my.configure(selectforeground="black")
              self.YEAR_NDWI_my.configure(wrap="word")

      if __name__ == '__main__':
          vp_start_gui()










   def openfield_fun():
      import sys
      try:
         import Tkinter as tk
      except ImportError:
         import tkinter as tk
      try:
         import ttk
         py3 = False
      except ImportError:
         import tkinter.ttk as ttk
         py3 = True

      import analytics_1_support

      def vp_start_gui():
         '''Starting point when module is the main routine.'''
         global val, w, root
         root = tk.Tk()
         top = Toplevel1 (root)
         analytics_1_support.init(root, top)
         root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
         '''Starting point when module is imported by another program.'''
         global w, w_win, rt
         rt = root
         w = tk.Toplevel (root)
         top = Toplevel1 (w)
         analytics_1_support.init(w, top, *args, **kwargs)
         return (w, top)

      def destroy_Toplevel1():
         global w
         w.destroy()
         w = None

      class Toplevel1:
         def imports_1(self):
            import webbrowser
            a_website = "https://kulkarnipranesh1767.users.earthengine.app/view/landsat8datadownloader"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(a_website)
            print("S")
            import pandas as pd
            import math
            from tkinter import filedialog
            import csv

            root = Tk()
            root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            print (root.filename)
            root.withdraw()
            csv_path = root.filename


            df = pd.read_csv(csv_path)


            x = 3
            i = 0
            t = []
            ndwiarr =[]
            msaviarr = []
            eviarr = []
            dates = []
            df.head()
            while(x):
               try:
                  blue = (df.loc[i,'B2'])
                  blue = blue.replace(',', '')
               except:
                  break
               red = (df.loc[i,'B4'])
               red = red.replace(',', '')
               nir = (df.loc[i,'B5'])
               nir = nir.replace(',', '')
               swir = (df.loc[i,'B6'])
               swir = swir.replace(',', '')
               evi = (float(nir)-float(red))/(float(nir)+float(red))
               #evi = (float(nir) - float(red))/((float(nir) + (6*float(red)) - (7.5*float(blue))) +1)
               ndwi = (float(nir)-float(swir))/(float(nir)+float(swir))
               msavi = ((2*float(nir))+1-(math.sqrt(((2*float(nir)+1)*(2*float(nir)+1))-(8*((float(nir)-float(red)))))))/2
               eviarr.append(evi)
               ndwiarr.append(ndwi)
               msaviarr.append(msavi)
               try:
                  date = str(df.loc[i,'system:time_start'])
                  dates.append(date)
               except:
                  break
               i = i+1


            print(eviarr)
            avg_evi = sum(eviarr)/len(eviarr)
            max_evi = max(eviarr)
            last_evi = eviarr[-1]
            second_evi = eviarr[-2]
            change_evi = 100*((last_evi- second_evi)/second_evi)
            evi_year_average = eviarr[-1:-17:-1]
            evi_year_average_value = sum(evi_year_average)/len(evi_year_average)
            print("Average EVI : ",avg_evi)
            print("Maximum EVI : ",max_evi)
            print("Latest EVI value : ",last_evi)
            print("Percentage change : ",change_evi)
            print("Last year Average EVI : ",evi_year_average_value)



            avg_ndwi = sum(ndwiarr)/len(ndwiarr)
            max_ndwi = max(ndwiarr)
            last_ndwi = ndwiarr[-1]
            second_ndwi = ndwiarr[-2]
            change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
            ndwi_year_average = ndwiarr[-1:-17:-1]
            ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)
            print("Average NDWI : ",avg_ndwi)
            print("Maximum NDWI : ",max_ndwi)
            print("Latest NDWI value : ",last_ndwi)
            print("Percentage change : ",change_ndwi)
            print("Last year Average NDWI : ",ndwi_year_average_value)


            avg_msavi = sum(msaviarr)/len(msaviarr)
            max_msavi = max(msaviarr)
            last_msavi = msaviarr[-1]
            second_msavi = msaviarr[-2]
            change_msavi = 100*((last_msavi- second_msavi)/second_msavi)
            msavi_year_average = msaviarr[-1:-17:-1]
            msavi_year_average_value = sum(msavi_year_average)/len(msavi_year_average)
            print("Average MSAVI : ",avg_msavi)
            print("Maximum MSAVI : ",max_msavi)
            print("Latest MSAVI value : ",last_msavi)
            print("Percentage change : ",change_msavi)
            print("Last year Average MSAVI : ",msavi_year_average_value)


            root = Tk()
            root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            print (root.filename)
            root.withdraw()
            csv_path = root.filename


            df2 = pd.read_csv(csv_path)

            i = 0 
            x = 4
            rainfall = []
            while(x):
               try:
                  rain = (df2.loc[i,'precipitation'])
               except:
                  break
               rain = float(rain)
               rainfall.append(rain)
               i = i+1

            avg_rainfall = sum(rainfall)/len(rainfall)
            print("Average Rainfall : ",avg_rainfall)





            print("_____________________Machine Learning Prediction_________________________________")

            print("\n\n\n\n")
            import pickle
            filename = 'finalized_kmeans_model.sav'
            loaded_model = pickle.load(open(filename, 'rb'))


            Xnew = [[avg_evi,avg_ndwi,avg_msavi,avg_rainfall]]
            # make a prediction
            ynew = loaded_model.predict_proba(Xnew)
            print(ynew)
            cluster1 = ynew[0,0]
            cluster2 = ynew[0,1]
            cluster3 = ynew[0,2]
            cluster4 = ynew[0,3]

            arr = [cluster1,cluster2,cluster3,cluster4]
            maximum = max(arr)
            index = arr.index(maximum)

            percentage_prediction = maximum*100

            print("element is in  cluster :",index+1)
            qual = str(index+1)
            print("Probability : ",percentage_prediction," %")
            confie = str(str(percentage_prediction)+" % ")
            print("\n\n\n\n")


            print("_____________________Machine Learning Prediction_________________________________")

            y = []


            for i in range(len(eviarr)):
               y.append(i)




            avg_evi = str(avg_evi)
            change_evi = str(change_evi)
            last_evi = str(last_evi)
            max_evi = str(max_evi)
            evi_year_average_value = str(evi_year_average_value)

            avg_msavi = str(avg_msavi)
            change_msavi = str(change_msavi)
            last_msavi = str(last_msavi)
            max_msavi = str(max_msavi)
            msavi_year_average_value = str(msavi_year_average_value)

            self.avg_NDVI.insert(1.0,avg_evi)
            self.per_NDVI.insert(1.0,change_evi)
            self.Lat_NDVI.insert(1.0,last_evi)
            self.max_NDVI.insert(1.0,max_evi)
            self.year_NDVI.insert(1.0,evi_year_average_value)

            self.avg_MSAVI.insert(1.0,avg_msavi)
            self.year_MSAVI.insert(1.0,msavi_year_average_value)
            self.per_MSAVI.insert(1.0,change_msavi)
            self.Lat_MSAVI.insert(1.0,last_msavi)
            self.max_MSAVI.insert(1.0,max_msavi)


            for i in range(len(eviarr)):
               DATE_L = str(dates[i])
               NDVI_L = str(eviarr[i])[0:7]
               MSAVI_L = str(msaviarr[i])[0:7]
               NDWI_L = str(ndwiarr[i])[0:7]

               s="{}   {}    {}    {}".format(DATE_L, NDVI_L, NDWI_L, MSAVI_L)
               self.index_show.insert(0,s)



            for i in range(len(eviarr)):
               DATE_L = str(dates[i])
               RAIN_L = str(rainfall[i])

               s="{}  {}".format(DATE_L, RAIN_L)
               self.rainfall_show.insert(0,s)



            self.quality.insert(1.0,qual)
            self.conf_score.insert(1.0,confie)




            import matplotlib.pyplot as plt 
          
            # line 1 points 
            x1 = y 
            y1 = eviarr 
            # plotting the line 1 points  
            plt.plot(x1, y1, label = "NDVI") 
          
            x3 = y 
            y3 = ndwiarr 
            # plotting the line 2 points  
            plt.plot(x3, y3, label = "MSAVI") 



            # naming the x axis 
            plt.xlabel('Time') 
            # naming the y axis 
            plt.ylabel('Index') 
            # giving a title to my graph 
            plt.title('Analytics') 
          
            # show a legend on the plot 
            plt.legend() 
          
            # function to show the plot 
            plt.show()


            return




















         def buts(self):
            root.destroy()
            mainscreen()









         def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
            font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
               "roman -underline 0 -overstrike 0"
            self.style = ttk.Style()
            if sys.platform == "win32":
               self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.map('.',background=
               [('selected', _compcolor), ('active',_ana2color)])

            top.geometry("1148x744+143+137")
            top.minsize(124, 1)
            top.maxsize(1596, 873)
            top.resizable(1, 1)
            top.title("New Toplevel")
            top.configure(background="#004080")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.009, rely=0.013, relheight=0.961, relwidth=0.98)

            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#5f5f5f")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")

            self.Frame2 = tk.Frame(self.Frame1)
            self.Frame2.place(relx=0.676, rely=0.028, relheight=0.119
              , relwidth=0.253)
            self.Frame2.configure(relief='ridge')
            self.Frame2.configure(borderwidth="10")
            self.Frame2.configure(relief="ridge")
            self.Frame2.configure(background="#408080")
            self.Frame2.configure(highlightbackground="#d9d9d9")
            self.Frame2.configure(highlightcolor="black")

            self.Label1 = tk.Label(self.Frame2)
            self.Label1.place(relx=0.105, rely=0.235, height=44, width=224)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {SF Fortune Wheel Extended} -size 24")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''ANALYTICS''')

            self.index_show = ScrolledListBox(self.Frame1)
            self.index_show.place(relx=0.027, rely=0.126, relheight=0.804
              , relwidth=0.348)
            self.index_show.configure(background="white")
            self.index_show.configure(disabledforeground="#a3a3a3")
            self.index_show.configure(font="TkFixedFont")
            self.index_show.configure(foreground="black")
            self.index_show.configure(highlightbackground="#d9d9d9")
            self.index_show.configure(highlightcolor="#d9d9d9")
            self.index_show.configure(selectbackground="#c4c4c4")
            self.index_show.configure(selectforeground="black")

            self.rainfall_show = ScrolledListBox(self.Frame1)
            self.rainfall_show.place(relx=0.4, rely=0.126, relheight=0.804
              , relwidth=0.17)
            self.rainfall_show.configure(background="white")
            self.rainfall_show.configure(disabledforeground="#a3a3a3")
            self.rainfall_show.configure(font="TkFixedFont")
            self.rainfall_show.configure(foreground="black")
            self.rainfall_show.configure(highlightbackground="#d9d9d9")
            self.rainfall_show.configure(highlightcolor="#d9d9d9")
            self.rainfall_show.configure(selectbackground="#c4c4c4")
            self.rainfall_show.configure(selectforeground="black")

            self.Label2 = tk.Label(self.Frame1)
            self.Label2.place(relx=0.036, rely=0.084, height=21, width=74)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            self.Label2.configure(text='''DATE''')

            self.Label2_3 = tk.Label(self.Frame1)
            self.Label2_3.place(relx=0.116, rely=0.084, height=21, width=74)
            self.Label2_3.configure(activebackground="#f9f9f9")
            self.Label2_3.configure(activeforeground="black")
            self.Label2_3.configure(background="#d9d9d9")
            self.Label2_3.configure(disabledforeground="#a3a3a3")
            self.Label2_3.configure(foreground="#000000")
            self.Label2_3.configure(highlightbackground="#d9d9d9")
            self.Label2_3.configure(highlightcolor="black")
            self.Label2_3.configure(text='''NDVI''')

            self.Label2_4 = tk.Label(self.Frame1)
            self.Label2_4.place(relx=0.196, rely=0.084, height=21, width=74)
            self.Label2_4.configure(activebackground="#f9f9f9")
            self.Label2_4.configure(activeforeground="black")
            self.Label2_4.configure(background="#d9d9d9")
            self.Label2_4.configure(disabledforeground="#a3a3a3")
            self.Label2_4.configure(foreground="#000000")
            self.Label2_4.configure(highlightbackground="#d9d9d9")
            self.Label2_4.configure(highlightcolor="black")
            self.Label2_4.configure(text='''NDWI''')

            self.Label2_5 = tk.Label(self.Frame1)
            self.Label2_5.place(relx=0.284, rely=0.084, height=21, width=74)
            self.Label2_5.configure(activebackground="#f9f9f9")
            self.Label2_5.configure(activeforeground="black")
            self.Label2_5.configure(background="#d9d9d9")
            self.Label2_5.configure(disabledforeground="#a3a3a3")
            self.Label2_5.configure(foreground="#000000")
            self.Label2_5.configure(highlightbackground="#d9d9d9")
            self.Label2_5.configure(highlightcolor="black")
            self.Label2_5.configure(text='''MSAVI''')

            self.Label2_6 = tk.Label(self.Frame1)
            self.Label2_6.place(relx=0.4, rely=0.084, height=21, width=74)
            self.Label2_6.configure(activebackground="#f9f9f9")
            self.Label2_6.configure(activeforeground="black")
            self.Label2_6.configure(background="#d9d9d9")
            self.Label2_6.configure(disabledforeground="#a3a3a3")
            self.Label2_6.configure(foreground="#000000")
            self.Label2_6.configure(highlightbackground="#d9d9d9")
            self.Label2_6.configure(highlightcolor="black")
            self.Label2_6.configure(text='''DATE''')

            self.Label2_2 = tk.Label(self.Frame1)
            self.Label2_2.place(relx=0.489, rely=0.084, height=21, width=74)
            self.Label2_2.configure(activebackground="#f9f9f9")
            self.Label2_2.configure(activeforeground="black")
            self.Label2_2.configure(background="#d9d9d9")
            self.Label2_2.configure(disabledforeground="#a3a3a3")
            self.Label2_2.configure(foreground="#000000")
            self.Label2_2.configure(highlightbackground="#d9d9d9")
            self.Label2_2.configure(highlightcolor="black")
            self.Label2_2.configure(text='''Rainfall''')

            self.Frame3 = tk.Frame(self.Frame1)
            self.Frame3.place(relx=0.613, rely=0.182, relheight=0.245
              , relwidth=0.351)
            self.Frame3.configure(relief='groove')
            self.Frame3.configure(borderwidth="2")
            self.Frame3.configure(relief="groove")
            self.Frame3.configure(background="#004040")
            self.Frame3.configure(highlightbackground="#d9d9d9")
            self.Frame3.configure(highlightcolor="black")

            self.Label3 = tk.Label(self.Frame3)
            self.Label3.place(relx=0.025, rely=0.057, height=21, width=124)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#004040")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Rockwell} -size 13")
            self.Label3.configure(foreground="#ffff00")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(text='''Average NDVI :''')

            self.Label3_2 = tk.Label(self.Frame3)
            self.Label3_2.place(relx=0.025, rely=0.571, height=21, width=134)
            self.Label3_2.configure(activebackground="#f9f9f9")
            self.Label3_2.configure(activeforeground="black")
            self.Label3_2.configure(background="#004040")
            self.Label3_2.configure(disabledforeground="#a3a3a3")
            self.Label3_2.configure(font="-family {Rockwell} -size 13")
            self.Label3_2.configure(foreground="#ffff00")
            self.Label3_2.configure(highlightbackground="#d9d9d9")
            self.Label3_2.configure(highlightcolor="black")
            self.Label3_2.configure(text='''Percent Change :''')

            self.Label3_3 = tk.Label(self.Frame3)
            self.Label3_3.place(relx=0.025, rely=0.4, height=21, width=124)
            self.Label3_3.configure(activebackground="#f9f9f9")
            self.Label3_3.configure(activeforeground="black")
            self.Label3_3.configure(background="#004040")
            self.Label3_3.configure(disabledforeground="#a3a3a3")
            self.Label3_3.configure(font="-family {Rockwell} -size 13")
            self.Label3_3.configure(foreground="#ffff00")
            self.Label3_3.configure(highlightbackground="#d9d9d9")
            self.Label3_3.configure(highlightcolor="black")
            self.Label3_3.configure(text='''Latest NDVI :''')

            self.Label3_4 = tk.Label(self.Frame3)
            self.Label3_4.place(relx=0.025, rely=0.229, height=21, width=134)
            self.Label3_4.configure(activebackground="#f9f9f9")
            self.Label3_4.configure(activeforeground="black")
            self.Label3_4.configure(background="#004040")
            self.Label3_4.configure(disabledforeground="#a3a3a3")
            self.Label3_4.configure(font="-family {Rockwell} -size 13")
            self.Label3_4.configure(foreground="#ffff00")
            self.Label3_4.configure(highlightbackground="#d9d9d9")
            self.Label3_4.configure(highlightcolor="black")
            self.Label3_4.configure(text='''Maximum NDVI :''')

            self.Label3_5 = tk.Label(self.Frame3)
            self.Label3_5.place(relx=0.025, rely=0.743, height=21, width=124)
            self.Label3_5.configure(activebackground="#f9f9f9")
            self.Label3_5.configure(activeforeground="black")
            self.Label3_5.configure(background="#004040")
            self.Label3_5.configure(disabledforeground="#a3a3a3")
            self.Label3_5.configure(font="-family {Rockwell} -size 10")
            self.Label3_5.configure(foreground="#ffff00")
            self.Label3_5.configure(highlightbackground="#d9d9d9")
            self.Label3_5.configure(highlightcolor="black")
            self.Label3_5.configure(text='''Last Year Average :''')

            self.per_NDVI = tk.Text(self.Frame3)
            self.per_NDVI.place(relx=0.38, rely=0.571, relheight=0.137
              , relwidth=0.491)
            self.per_NDVI.configure(background="white")
            self.per_NDVI.configure(font="TkTextFont")
            self.per_NDVI.configure(foreground="black")
            self.per_NDVI.configure(highlightbackground="#d9d9d9")
            self.per_NDVI.configure(highlightcolor="black")
            self.per_NDVI.configure(insertbackground="black")
            self.per_NDVI.configure(selectbackground="#c4c4c4")
            self.per_NDVI.configure(selectforeground="black")
            self.per_NDVI.configure(wrap="word")

            self.Lat_NDVI = tk.Text(self.Frame3)
            self.Lat_NDVI.place(relx=0.38, rely=0.4, relheight=0.137, relwidth=0.491)

            self.Lat_NDVI.configure(background="white")
            self.Lat_NDVI.configure(font="TkTextFont")
            self.Lat_NDVI.configure(foreground="black")
            self.Lat_NDVI.configure(highlightbackground="#d9d9d9")
            self.Lat_NDVI.configure(highlightcolor="black")
            self.Lat_NDVI.configure(insertbackground="black")
            self.Lat_NDVI.configure(selectbackground="#c4c4c4")
            self.Lat_NDVI.configure(selectforeground="black")
            self.Lat_NDVI.configure(wrap="word")

            self.max_NDVI = tk.Text(self.Frame3)
            self.max_NDVI.place(relx=0.38, rely=0.229, relheight=0.137
              , relwidth=0.491)
            self.max_NDVI.configure(background="white")
            self.max_NDVI.configure(font="TkTextFont")
            self.max_NDVI.configure(foreground="black")
            self.max_NDVI.configure(highlightbackground="#d9d9d9")
            self.max_NDVI.configure(highlightcolor="black")
            self.max_NDVI.configure(insertbackground="black")
            self.max_NDVI.configure(selectbackground="#c4c4c4")
            self.max_NDVI.configure(selectforeground="black")
            self.max_NDVI.configure(wrap="word")

            self.year_NDVI = tk.Text(self.Frame3)
            self.year_NDVI.place(relx=0.38, rely=0.743, relheight=0.137
              , relwidth=0.491)
            self.year_NDVI.configure(background="white")
            self.year_NDVI.configure(font="TkTextFont")
            self.year_NDVI.configure(foreground="black")
            self.year_NDVI.configure(highlightbackground="#d9d9d9")
            self.year_NDVI.configure(highlightcolor="black")
            self.year_NDVI.configure(insertbackground="black")
            self.year_NDVI.configure(selectbackground="#c4c4c4")
            self.year_NDVI.configure(selectforeground="black")
            self.year_NDVI.configure(wrap="word")

            self.avg_NDVI = tk.Text(self.Frame3)
            self.avg_NDVI.place(relx=0.38, rely=0.057, relheight=0.137
              , relwidth=0.491)
            self.avg_NDVI.configure(background="white")
            self.avg_NDVI.configure(font="TkTextFont")
            self.avg_NDVI.configure(foreground="black")
            self.avg_NDVI.configure(highlightbackground="#d9d9d9")
            self.avg_NDVI.configure(highlightcolor="black")
            self.avg_NDVI.configure(insertbackground="black")
            self.avg_NDVI.configure(selectbackground="#c4c4c4")
            self.avg_NDVI.configure(selectforeground="black")
            self.avg_NDVI.configure(wrap="word")

            self.Frame4 = tk.Frame(self.Frame1)
            self.Frame4.place(relx=0.613, rely=0.434, relheight=0.273
              , relwidth=0.351)
            self.Frame4.configure(relief='groove')
            self.Frame4.configure(borderwidth="2")
            self.Frame4.configure(relief="groove")
            self.Frame4.configure(background="#004040")
            self.Frame4.configure(highlightbackground="#d9d9d9")
            self.Frame4.configure(highlightcolor="black")

            self.Label4 = tk.Label(self.Frame4)
            self.Label4.place(relx=0.025, rely=0.051, height=26, width=139)
            self.Label4.configure(activebackground="#f9f9f9")
            self.Label4.configure(activeforeground="black")
            self.Label4.configure(background="#004040")
            self.Label4.configure(disabledforeground="#ffff00")
            self.Label4.configure(font="-family {Rockwell} -size 13")
            self.Label4.configure(foreground="#ffff00")
            self.Label4.configure(highlightbackground="#d9d9d9")
            self.Label4.configure(highlightcolor="black")
            self.Label4.configure(text='''Average MSAVI :''')

            self.Label4_2 = tk.Label(self.Frame4)
            self.Label4_2.place(relx=0.025, rely=0.667, height=26, width=139)
            self.Label4_2.configure(activebackground="#f9f9f9")
            self.Label4_2.configure(activeforeground="black")
            self.Label4_2.configure(background="#004040")
            self.Label4_2.configure(disabledforeground="#ffff00")
            self.Label4_2.configure(font="-family {Rockwell} -size 10")
            self.Label4_2.configure(foreground="#ffff00")
            self.Label4_2.configure(highlightbackground="#d9d9d9")
            self.Label4_2.configure(highlightcolor="black")
            self.Label4_2.configure(text='''Last Year Average :''')

            self.Label4_3 = tk.Label(self.Frame4)
            self.Label4_3.place(relx=0.025, rely=0.513, height=26, width=139)
            self.Label4_3.configure(activebackground="#f9f9f9")
            self.Label4_3.configure(activeforeground="black")
            self.Label4_3.configure(background="#004040")
            self.Label4_3.configure(disabledforeground="#ffff00")
            self.Label4_3.configure(font="-family {Rockwell} -size 13")
            self.Label4_3.configure(foreground="#ffff00")
            self.Label4_3.configure(highlightbackground="#d9d9d9")
            self.Label4_3.configure(highlightcolor="black")
            self.Label4_3.configure(text='''Percent Change :''')

            self.Label4_4 = tk.Label(self.Frame4)
            self.Label4_4.place(relx=0.025, rely=0.359, height=26, width=139)
            self.Label4_4.configure(activebackground="#f9f9f9")
            self.Label4_4.configure(activeforeground="black")
            self.Label4_4.configure(background="#004040")
            self.Label4_4.configure(disabledforeground="#ffff00")
            self.Label4_4.configure(font="-family {Rockwell} -size 13")
            self.Label4_4.configure(foreground="#ffff00")
            self.Label4_4.configure(highlightbackground="#d9d9d9")
            self.Label4_4.configure(highlightcolor="black")
            self.Label4_4.configure(text='''Latest MSAVI :''')

            self.Label4_5 = tk.Label(self.Frame4)
            self.Label4_5.place(relx=0.025, rely=0.205, height=26, width=149)
            self.Label4_5.configure(activebackground="#f9f9f9")
            self.Label4_5.configure(activeforeground="black")
            self.Label4_5.configure(background="#004040")
            self.Label4_5.configure(disabledforeground="#ffff00")
            self.Label4_5.configure(font="-family {Rockwell} -size 13")
            self.Label4_5.configure(foreground="#ffff00")
            self.Label4_5.configure(highlightbackground="#d9d9d9")
            self.Label4_5.configure(highlightcolor="black")
            self.Label4_5.configure(text='''Maximum MSAVI :''')

            self.avg_MSAVI = tk.Text(self.Frame4)
            self.avg_MSAVI.place(relx=0.43, rely=0.051, relheight=0.123
              , relwidth=0.466)
            self.avg_MSAVI.configure(background="white")
            self.avg_MSAVI.configure(font="TkTextFont")
            self.avg_MSAVI.configure(foreground="black")
            self.avg_MSAVI.configure(highlightbackground="#d9d9d9")
            self.avg_MSAVI.configure(highlightcolor="black")
            self.avg_MSAVI.configure(insertbackground="black")
            self.avg_MSAVI.configure(selectbackground="#c4c4c4")
            self.avg_MSAVI.configure(selectforeground="black")
            self.avg_MSAVI.configure(wrap="word")

            self.year_MSAVI = tk.Text(self.Frame4)
            self.year_MSAVI.place(relx=0.43, rely=0.667, relheight=0.123
              , relwidth=0.466)
            self.year_MSAVI.configure(background="white")
            self.year_MSAVI.configure(font="TkTextFont")
            self.year_MSAVI.configure(foreground="black")
            self.year_MSAVI.configure(highlightbackground="#d9d9d9")
            self.year_MSAVI.configure(highlightcolor="black")
            self.year_MSAVI.configure(insertbackground="black")
            self.year_MSAVI.configure(selectbackground="#c4c4c4")
            self.year_MSAVI.configure(selectforeground="black")
            self.year_MSAVI.configure(wrap="word")

            self.per_MSAVI = tk.Text(self.Frame4)
            self.per_MSAVI.place(relx=0.43, rely=0.513, relheight=0.123
              , relwidth=0.466)
            self.per_MSAVI.configure(background="white")
            self.per_MSAVI.configure(font="TkTextFont")
            self.per_MSAVI.configure(foreground="black")
            self.per_MSAVI.configure(highlightbackground="#d9d9d9")
            self.per_MSAVI.configure(highlightcolor="black")
            self.per_MSAVI.configure(insertbackground="black")
            self.per_MSAVI.configure(selectbackground="#c4c4c4")
            self.per_MSAVI.configure(selectforeground="black")
            self.per_MSAVI.configure(wrap="word")

            self.Lat_MSAVI = tk.Text(self.Frame4)
            self.Lat_MSAVI.place(relx=0.43, rely=0.359, relheight=0.123
              , relwidth=0.466)
            self.Lat_MSAVI.configure(background="white")
            self.Lat_MSAVI.configure(font="TkTextFont")
            self.Lat_MSAVI.configure(foreground="black")
            self.Lat_MSAVI.configure(highlightbackground="#d9d9d9")
            self.Lat_MSAVI.configure(highlightcolor="black")
            self.Lat_MSAVI.configure(insertbackground="black")
            self.Lat_MSAVI.configure(selectbackground="#c4c4c4")
            self.Lat_MSAVI.configure(selectforeground="black")
            self.Lat_MSAVI.configure(wrap="word")

            self.max_MSAVI = tk.Text(self.Frame4)
            self.max_MSAVI.place(relx=0.43, rely=0.205, relheight=0.123
              , relwidth=0.466)
            self.max_MSAVI.configure(background="white")
            self.max_MSAVI.configure(font="TkTextFont")
            self.max_MSAVI.configure(foreground="black")
            self.max_MSAVI.configure(highlightbackground="#d9d9d9")
            self.max_MSAVI.configure(highlightcolor="black")
            self.max_MSAVI.configure(insertbackground="black")
            self.max_MSAVI.configure(selectbackground="#c4c4c4")
            self.max_MSAVI.configure(selectforeground="black")
            self.max_MSAVI.configure(wrap="word")

            self.Frame5 = tk.Frame(self.Frame1)
            self.Frame5.place(relx=0.604, rely=0.783, relheight=0.175
              , relwidth=0.378)
            self.Frame5.configure(relief='groove')
            self.Frame5.configure(borderwidth="2")
            self.Frame5.configure(relief="groove")
            self.Frame5.configure(background="#004040")
            self.Frame5.configure(highlightbackground="#d9d9d9")
            self.Frame5.configure(highlightcolor="black")

            self.Label5 = tk.Label(self.Frame5)
            self.Label5.place(relx=0.024, rely=0.08, height=36, width=190)
            self.Label5.configure(activebackground="#f9f9f9")
            self.Label5.configure(activeforeground="black")
            self.Label5.configure(background="#004040")
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(font="-family {Rockwell} -size 19 -weight bold")
            self.Label5.configure(foreground="#80ff00")
            self.Label5.configure(highlightbackground="#d9d9d9")
            self.Label5.configure(highlightcolor="black")
            self.Label5.configure(text='''Quality Index :''')

            self.Label5_10 = tk.Label(self.Frame5)
            self.Label5_10.place(relx=0.024, rely=0.48, height=36, width=230)
            self.Label5_10.configure(activebackground="#f9f9f9")
            self.Label5_10.configure(activeforeground="black")
            self.Label5_10.configure(background="#004040")
            self.Label5_10.configure(disabledforeground="#a3a3a3")
            self.Label5_10.configure(font="-family {Rockwell} -size 19 -weight bold")
            self.Label5_10.configure(foreground="#80ff00")
            self.Label5_10.configure(highlightbackground="#d9d9d9")
            self.Label5_10.configure(highlightcolor="black")
            self.Label5_10.configure(text='''Confidence Score :''')

            self.quality = tk.Text(self.Frame5)
            self.quality.place(relx=0.518, rely=0.08, relheight=0.352
              , relwidth=0.362)
            self.quality.configure(background="#870c78")
            self.quality.configure(font="-family {Rockwell Extra Bold} -size 21 -weight bold")
            self.quality.configure(foreground="#ffffff")
            self.quality.configure(highlightbackground="#d9d9d9")
            self.quality.configure(highlightcolor="black")
            self.quality.configure(insertbackground="black")
            self.quality.configure(selectbackground="#c4c4c4")
            self.quality.configure(selectforeground="black")
            self.quality.configure(wrap="word")

            self.conf_score = tk.Text(self.Frame5)
            self.conf_score.place(relx=0.588, rely=0.48, relheight=0.352
              , relwidth=0.362)
            self.conf_score.configure(background="#870c78")
            self.conf_score.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
            self.conf_score.configure(foreground="#ffffff")
            self.conf_score.configure(highlightbackground="#d9d9d9")
            self.conf_score.configure(highlightcolor="black")
            self.conf_score.configure(insertbackground="black")
            self.conf_score.configure(selectbackground="#c4c4c4")
            self.conf_score.configure(selectforeground="black")
            self.conf_score.configure(wrap="word")

            self.Label6 = tk.Label(self.Frame1)
            self.Label6.place(relx=0.64, rely=0.727, height=30, width=363)
            self.Label6.configure(activebackground="#f9f9f9")
            self.Label6.configure(activeforeground="black")
            self.Label6.configure(background="#5f5f5f")
            self.Label6.configure(disabledforeground="#a3a3a3")
            self.Label6.configure(font="-family {Rockwell Extra Bold} -size 15 -weight bold")
            self.Label6.configure(foreground="#00ffff")
            self.Label6.configure(highlightbackground="#d9d9d9")
            self.Label6.configure(highlightcolor="black")
            self.Label6.configure(text='''Machine Learning Prediction''')

            self.import_but = tk.Button(self.Frame1)
            self.import_but.place(relx=0.036, rely=0.014, height=34, width=127)
            self.import_but.configure(activebackground="#ececec")
            self.import_but.configure(activeforeground="#000000")
            self.import_but.configure(background="#ff0000")
            self.import_but.configure(disabledforeground="#a3a3a3")
            self.import_but.configure(font=font9)
            self.import_but.configure(foreground="#ffffff")
            self.import_but.configure(highlightbackground="#d9d9d9")
            self.import_but.configure(highlightcolor="black")
            self.import_but.configure(pady="0")
            self.import_but.configure(text='''IMPORT''',command = self.imports_1)

            self.back_but = tk.Button(self.Frame1)
            self.back_but.place(relx=0.169, rely=0.014, height=34, width=127)
            self.back_but.configure(activebackground="#ececec")
            self.back_but.configure(activeforeground="black")
            self.back_but.configure(background="#008000")
            self.back_but.configure(disabledforeground="#a3a3a3")
            self.back_but.configure(font="-family {Segoe UI} -size 14")
            self.back_but.configure(foreground="#ffffff")
            self.back_but.configure(highlightbackground="#d9d9d9")
            self.back_but.configure(highlightcolor="black")
            self.back_but.configure(pady="0")
            self.back_but.configure(text='''BACK''',command = self.buts)

            self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
            top.configure(menu = self.menubar)

      # The following code is added to facilitate the Scrolled widgets you specified.
      class AutoScroll(object):
         '''Configure the scrollbars for a widget.'''

         def __init__(self, master):
            #  Rozen. Added the try-except clauses so that this class
            #  could be used for scrolled entry widget for which vertical
            #  scrolling is not supported. 5/7/14.
            try:
               vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
            except:
               pass
            hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

            #self.configure(yscrollcommand=_autoscroll(vsb),
            #    xscrollcommand=_autoscroll(hsb))
            try:
               self.configure(yscrollcommand=self._autoscroll(vsb))
            except:
               pass
            self.configure(xscrollcommand=self._autoscroll(hsb))

            self.grid(column=0, row=0, sticky='nsew')
            try:
               vsb.grid(column=1, row=0, sticky='ns')
            except:
               pass
            hsb.grid(column=0, row=1, sticky='ew')

            master.grid_columnconfigure(0, weight=1)
            master.grid_rowconfigure(0, weight=1)

            # Copy geometry methods of master  (taken from ScrolledText.py)
            if py3:
               methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()
            else:
               methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                + tk.Place.__dict__.keys()

            for meth in methods:
               if meth[0] != '_' and meth not in ('config', 'configure'):
                  setattr(self, meth, getattr(master, meth))

         @staticmethod
         def _autoscroll(sbar):
            '''Hide and show scrollbar as needed.'''
            def wrapped(first, last):
               first, last = float(first), float(last)
               if first <= 0 and last >= 1:
                  sbar.grid_remove()
               else:
                  sbar.grid()
                  sbar.set(first, last)
            return wrapped

         def __str__(self):
            return str(self.master)

      def _create_container(func):
         '''Creates a ttk Frame with a given master, and use this new frame to
         place the scrollbars and the widget.'''
         def wrapped(cls, master, **kw):
            container = ttk.Frame(master)
            container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
            container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
            return func(cls, container, **kw)
         return wrapped

      class ScrolledListBox(AutoScroll, tk.Listbox):
         '''A standard Tkinter Listbox widget with scrollbars that will
         automatically show/hide as needed.'''
         @_create_container
         def __init__(self, master, **kw):
            tk.Listbox.__init__(self, master, **kw)
            AutoScroll.__init__(self, master)
         def size_(self):
            sz = tk.Listbox.size(self)
            return sz

      import platform
      def _bound_to_mousewheel(event, widget):
         child = widget.winfo_children()[0]
         if platform.system() == 'Windows' or platform.system() == 'Darwin':
            child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
         else:
            child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
            child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
            child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

      def _unbound_to_mousewheel(event, widget):
         if platform.system() == 'Windows' or platform.system() == 'Darwin':
            widget.unbind_all('<MouseWheel>')
            widget.unbind_all('<Shift-MouseWheel>')
         else:
            widget.unbind_all('<Button-4>')
            widget.unbind_all('<Button-5>')
            widget.unbind_all('<Shift-Button-4>')
            widget.unbind_all('<Shift-Button-5>')

      def _on_mousewheel(event, widget):
         if platform.system() == 'Windows':
            widget.yview_scroll(-1*int(event.delta/120),'units')
         elif platform.system() == 'Darwin':
            widget.yview_scroll(-1*int(event.delta),'units')
         else:
            if event.num == 4:
               widget.yview_scroll(-1, 'units')
            elif event.num == 5:
               widget.yview_scroll(1, 'units')

      def _on_shiftmouse(event, widget):
         if platform.system() == 'Windows':
            widget.xview_scroll(-1*int(event.delta/120), 'units')
         elif platform.system() == 'Darwin':
            widget.xview_scroll(-1*int(event.delta), 'units')
         else:
            if event.num == 4:
               widget.xview_scroll(-1, 'units')
            elif event.num == 5:
               widget.xview_scroll(1, 'units')

      if __name__ == '__main__':
         vp_start_gui()










   def openwater_fun():
      import pandas as pd
      import math
      from tkinter import filedialog
      import csv

      root = Tk()
      root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
      print (root.filename)
      root.withdraw()
      csv_path = root.filename


      df = pd.read_csv(csv_path)


      x = 3
      i = 0
      t = []
      ndwiarr =[]
      msaviarr = []
      eviarr = []
      dates = []
      df.head()
      while(x):
         try:
            blue = (df.loc[i,'B2'])
            blue = blue.replace(',', '')
         except:
            break
         red = (df.loc[i,'B4'])
         red = red.replace(',', '')
         nir = (df.loc[i,'B5'])
         nir = nir.replace(',', '')
         swir = (df.loc[i,'B6'])
         swir = swir.replace(',', '')
         evi = (float(nir)-float(red))/(float(nir)+float(red))
         #evi = (float(nir) - float(red))/((float(nir) + (6*float(red)) - (7.5*float(blue))) +1)
         ndwi = (float(nir)-float(swir))/(float(nir)+float(swir))
         msavi = ((2*float(nir))+1-(math.sqrt(((2*float(nir)+1)*(2*float(nir)+1))-(8*((float(nir)-float(red)))))))/2
         eviarr.append(evi)
         ndwiarr.append(ndwi)
         msaviarr.append(msavi)
         try:
            date = str(df.loc[i,'system:time_start'])
            dates.append(date)
         except:
            break
         i = i+1


      avg_ndwi = sum(ndwiarr)/len(ndwiarr)
      max_ndwi = max(ndwiarr)
      last_ndwi = ndwiarr[-1]
      second_ndwi = ndwiarr[-2]
      change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
      ndwi_year_average = ndwiarr[-1:-17:-1]
      ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)
      print("\n\n\n\n\n\n\n\n\n\n\n")
      print("Date          NDWI\n")
      for i in range(len(eviarr)):
         print(dates[i],"\t\t",ndwiarr[i])
      print("_______________________________________________________")
      print("\n\n\n\n\n\n\n")
      print("Average NDWI : ",avg_ndwi)
      print("Maximum NDWI : ",max_ndwi)
      print("Latest NDWI value : ",last_ndwi)
      print("Percentage change : ",change_ndwi)
      print("Last year Average NDWI : ",ndwi_year_average_value)


      y = []


      for i in range(len(eviarr)):
         y.append(i)


      import matplotlib.pyplot as plt 
        
      # line 1 points 
      x1 = y 
      y1 = ndwiarr
      # plotting the line 1 points  
      plt.plot(x1, y1, label = "NDWI") 
        



      # naming the x axis 
      plt.xlabel('Time') 
      # naming the y axis 
      plt.ylabel('Index') 
      # giving a title to my graph 
      plt.title('Analytics') 
        
      # show a legend on the plot 
      plt.legend() 
        
      # function to show the plot 
      plt.show() 

   def mainscreen():
            #! /usr/bin/env python
      #  -*- coding: utf-8 -*-
      #
      # GUI module generated by PAGE version 4.26
      #  in conjunction with Tcl version 8.6
      #    Dec 14, 2019 12:55:40 AM +0530  platform: Windows NT

      import sys

      try:
         import Tkinter as tk
      except ImportError:
         import tkinter as tk

      try:
         import ttk
         py3 = False
      except ImportError:
         import tkinter.ttk as ttk
         py3 = True

      import main_screen_support

      def vp_start_gui():
         '''Starting point when module is the main routine.'''
         global val, w, root
         root = tk.Tk()
         top = Toplevel1 (root)
         main_screen_support.init(root, top)
         root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
         '''Starting point when module is imported by another program.'''
         global w, w_win, rt
         rt = root
         w = tk.Toplevel (root)
         top = Toplevel1 (w)
         main_screen_support.init(w, top, *args, **kwargs)
         return (w, top)

      def destroy_Toplevel1():
         global w
         w.destroy()
         w = None








      class Toplevel1:
         def abouts(self):
            root.destroy()
            print("About")


         def openfield(self):
            root.destroy()
            openfield_fun()

         def myfieldopen(self):
            nameFIELD = self.name_FIELD.get();
            NAMEVILLAGE = self.NAME_VILLAGE.get();
            print("open my field")
            myfieldopen_fun(nameFIELD,NAMEVILLAGE)


         def openwater(self):
            print("Open Water")
            openwater_fun()


         def exits(self):
            root.destroy()
            exit()

         def backs(self):
            root.destroy()
            main()

         def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'

            top.geometry("1149x728+50+152")
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1, 1)
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.035, rely=0.014, relheight=0.941
              , relwidth=0.936)
            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="7")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#6a6a6a")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")

            self.about_b = tk.Button(self.Frame1)
            self.about_b.place(relx=0.084, rely=0.774, height=43, width=106)
            self.about_b.configure(activebackground="#696969")
            self.about_b.configure(activeforeground="white")
            self.about_b.configure(activeforeground="#000000")
            self.about_b.configure(background="#808040")
            self.about_b.configure(disabledforeground="#a3a3a3")
            self.about_b.configure(font="-family {Segoe UI} -size 16")
            self.about_b.configure(foreground="#000000")
            self.about_b.configure(highlightbackground="#d9d9d9")
            self.about_b.configure(highlightcolor="black")
            self.about_b.configure(pady="0")
            self.about_b.configure(text='''About''',command = self.abouts)

            self.Frame2 = tk.Frame(self.Frame1)
            self.Frame2.place(relx=0.037, rely=0.263, relheight=0.46, relwidth=0.479)

            self.Frame2.configure(relief='ridge')
            self.Frame2.configure(borderwidth="5")
            self.Frame2.configure(relief="ridge")
            self.Frame2.configure(background="#7e7e7e")
            self.Frame2.configure(highlightbackground="#d9d9d9")
            self.Frame2.configure(highlightcolor="black")

            self.Label1 = tk.Label(self.Frame2)
            self.Label1.place(relx=0.058, rely=0.127, height=56, width=182)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 14")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''Username:''')

            self.Label2 = tk.Label(self.Frame2)
            self.Label2.place(relx=0.058, rely=0.381, height=56, width=182)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 14")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            self.Label2.configure(text='''Village:''')

            self.fieldname_open = tk.Button(self.Frame2)
            self.fieldname_open.place(relx=0.33, rely=0.635, height=63, width=206)
            self.fieldname_open.configure(activebackground="#ececec")
            self.fieldname_open.configure(activeforeground="#000000")
            self.fieldname_open.configure(background="#0080ff")
            self.fieldname_open.configure(disabledforeground="#a3a3a3")
            self.fieldname_open.configure(font="-family {Segoe UI} -size 16")
            self.fieldname_open.configure(foreground="#000000")
            self.fieldname_open.configure(highlightbackground="#d9d9d9")
            self.fieldname_open.configure(highlightcolor="black")
            self.fieldname_open.configure(pady="0")
            self.fieldname_open.configure(text='''Open''',command = self.myfieldopen)

            self.name_FIELD = tk.Entry(self.Frame2)
            self.name_FIELD.place(relx=0.485, rely=0.127,height=56, relwidth=0.454)
            self.name_FIELD.configure(background="white")
            self.name_FIELD.configure(disabledforeground="#a3a3a3")
            self.name_FIELD.configure(font="TkFixedFont")
            self.name_FIELD.configure(foreground="#000000")
            self.name_FIELD.configure(highlightbackground="#d9d9d9")
            self.name_FIELD.configure(highlightcolor="black")
            self.name_FIELD.configure(insertbackground="black")
            self.name_FIELD.configure(selectbackground="#c4c4c4")
            self.name_FIELD.configure(selectforeground="black")

            self.NAME_VILLAGE = tk.Entry(self.Frame2)
            self.NAME_VILLAGE.place(relx=0.485, rely=0.381, height=56
              , relwidth=0.454)
            self.NAME_VILLAGE.configure(background="white")
            self.NAME_VILLAGE.configure(disabledforeground="#a3a3a3")
            self.NAME_VILLAGE.configure(font="TkFixedFont")
            self.NAME_VILLAGE.configure(foreground="#000000")
            self.NAME_VILLAGE.configure(highlightbackground="#d9d9d9")
            self.NAME_VILLAGE.configure(highlightcolor="black")
            self.NAME_VILLAGE.configure(insertbackground="black")
            self.NAME_VILLAGE.configure(selectbackground="#c4c4c4")
            self.NAME_VILLAGE.configure(selectforeground="black")

            self.Frame3 = tk.Frame(self.Frame1)
            self.Frame3.place(relx=0.549, rely=0.263, relheight=0.328
              , relwidth=0.395)
            self.Frame3.configure(relief='ridge')
            self.Frame3.configure(borderwidth="5")
            self.Frame3.configure(relief="ridge")
            self.Frame3.configure(background="#7c7c7c")
            self.Frame3.configure(highlightbackground="#d9d9d9")
            self.Frame3.configure(highlightcolor="black")

            self.field_open = tk.Button(self.Frame3)
            self.field_open.place(relx=0.212, rely=0.489, height=83, width=236)
            self.field_open.configure(activebackground="#9c9c9c")
            self.field_open.configure(activeforeground="#000000")
            self.field_open.configure(background="#008080")
            self.field_open.configure(disabledforeground="#a3a3a3")
            self.field_open.configure(font="-family {Segoe UI} -size 16")
            self.field_open.configure(foreground="#000000")
            self.field_open.configure(highlightbackground="#d9d9d9")
            self.field_open.configure(highlightcolor="black")
            self.field_open.configure(pady="0")
            self.field_open.configure(text='''Open''',command = self.openfield)

            self.Label3 = tk.Label(self.Frame3)
            self.Label3.place(relx=0.047, rely=0.089, height=76, width=372)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#d9d9d9")
            self.Label3.configure(borderwidth="7")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 18")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(relief="ridge")
            self.Label3.configure(state='active')
            self.Label3.configure(text='''Analyse The Field''')

            self.Frame4 = tk.Frame(self.Frame1)
            self.Frame4.place(relx=0.549, rely=0.613, relheight=0.328
              , relwidth=0.395)
            self.Frame4.configure(relief='ridge')
            self.Frame4.configure(borderwidth="5")
            self.Frame4.configure(relief="ridge")
            self.Frame4.configure(background="#7c7c7c")
            self.Frame4.configure(highlightbackground="#d9d9d9")
            self.Frame4.configure(highlightcolor="black")

            self.water_open = tk.Button(self.Frame4)
            self.water_open.place(relx=0.235, rely=0.533, height=83, width=236)
            self.water_open.configure(activebackground="#ececec")
            self.water_open.configure(activeforeground="#000000")
            self.water_open.configure(background="#008080")
            self.water_open.configure(disabledforeground="#a3a3a3")
            self.water_open.configure(font="-family {Segoe UI} -size 16")
            self.water_open.configure(foreground="#000000")
            self.water_open.configure(highlightbackground="#d9d9d9")
            self.water_open.configure(highlightcolor="black")
            self.water_open.configure(pady="0")
            self.water_open.configure(text='''Open''',command = self.openwater)

            self.Label4 = tk.Label(self.Frame4)
            self.Label4.place(relx=0.094, rely=0.089, height=76, width=352)
            self.Label4.configure(activebackground="#f9f9f9")
            self.Label4.configure(activeforeground="black")
            self.Label4.configure(background="#d9d9d9")
            self.Label4.configure(borderwidth="7")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font="-family {Segoe UI} -size 18")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(highlightbackground="#d9d9d9")
            self.Label4.configure(highlightcolor="black")
            self.Label4.configure(relief="ridge")
            self.Label4.configure(state='active')
            self.Label4.configure(text='''Analyse The Water Source''')

            self.Label5 = tk.Label(self.Frame1)
            self.Label5.place(relx=0.214, rely=0.073, height=106, width=592)
            self.Label5.configure(activebackground="#f9f9f9")
            self.Label5.configure(activeforeground="black")
            self.Label5.configure(background="#80ffff")
            self.Label5.configure(borderwidth="7")
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(font="-family {Rockwell} -size 22 -weight bold")
            self.Label5.configure(foreground="#000000")
            self.Label5.configure(highlightbackground="#d9d9d9")
            self.Label5.configure(highlightcolor="black")
            self.Label5.configure(relief="raised")
            self.Label5.configure(state='active')
            self.Label5.configure(text='''SATELLITE FIELD ANALYSER''')

            self.exit_but = tk.Button(self.Frame1)
            self.exit_but.place(relx=0.353, rely=0.774, height=43, width=106)
            self.exit_but.configure(activebackground="#696969")
            self.exit_but.configure(activeforeground="white")
            self.exit_but.configure(activeforeground="#000000")
            self.exit_but.configure(background="#ff0000")
            self.exit_but.configure(disabledforeground="#a3a3a3")
            self.exit_but.configure(font="-family {Segoe UI} -size 16")
            self.exit_but.configure(foreground="#000000")
            self.exit_but.configure(highlightbackground="#d9d9d9")
            self.exit_but.configure(highlightcolor="black")
            self.exit_but.configure(pady="0")
            self.exit_but.configure(text='''EXIT''',command = self.exits)

            self.back_but = tk.Button(self.Frame1)
            self.back_but.place(relx=0.223, rely=0.774, height=43, width=106)
            self.back_but.configure(activebackground="#696969")
            self.back_but.configure(activeforeground="white")
            self.back_but.configure(activeforeground="#000000")
            self.back_but.configure(background="#008000")
            self.back_but.configure(disabledforeground="#a3a3a3")
            self.back_but.configure(font="-family {Segoe UI} -size 16")
            self.back_but.configure(foreground="#000000")
            self.back_but.configure(highlightbackground="#d9d9d9")
            self.back_but.configure(highlightcolor="black")
            self.back_but.configure(pady="0")
            self.back_but.configure(text='''BACK''',command = self.backs)

      if __name__ == '__main__':
         vp_start_gui()







   def process(newusername,newpassword,namefield,villagename,districtname):
      import webbrowser
 
      a_website = "https://kulkarnipranesh1767.users.earthengine.app/view/landsat8datadownloader"
      chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
      webbrowser.get(chrome_path).open(a_website)




      newusername= newusername
      newpassword= newpassword
      namefield=namefield
      villagename=villagename
      districtname=districtname
      import pandas as pd
      import math
      import matplotlib.pyplot as plt
      
      from tkinter import filedialog
      import csv



      root = Tk()
      root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
      print (root.filename)
      root.withdraw()
      csv_path = root.filename



      df = pd.read_csv(csv_path)



      x = 3
      i = 0
      t = []
      ndwiarr =[]
      msaviarr = []
      eviarr = []
      dates = []
      df.head()
      while(x):
         try:
            blue = (df.loc[i,'B2'])
            blue = blue.replace(',', '')
         except:
            break
         red = (df.loc[i,'B4'])
         red = red.replace(',', '')
         nir = (df.loc[i,'B5'])
         nir = nir.replace(',', '')
         swir = (df.loc[i,'B6'])
         swir = swir.replace(',', '')
         evi = (float(nir)-float(red))/(float(nir)+float(red))
         ndwi = (float(nir)-float(swir))/(float(nir)+float(swir))
         msavi = ((2*float(nir))+1-(math.sqrt(((2*float(nir)+1)*(2*float(nir)+1))-(8*((float(nir)-float(red)))))))/2
         i = i+1
         eviarr.append(evi)
         ndwiarr.append(ndwi)
         msaviarr.append(msavi)
         try:
            date = str(df.loc[i,'system:time_start'])
            dates.append(date)
         except:
            break

      avg_evi = sum(eviarr)/len(eviarr)
      y = []


      for i in range(len(eviarr)):
         y.append(i)


      max_evi = max(eviarr)
      last_evi = eviarr[-1]
      second_evi = eviarr[-2]
      change_evi = 100*((last_evi- second_evi)/second_evi)
      evi_year_average = eviarr[-1:-17:-1]
      evi_year_average_value = sum(evi_year_average)/len(evi_year_average)

      avg_ndwi = sum(ndwiarr)/len(ndwiarr)
      max_ndwi = max(ndwiarr)
      last_ndwi = ndwiarr[-1]
      second_ndwi = ndwiarr[-2]
      change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
      ndwi_year_average = ndwiarr[-1:-17:-1]
      ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)



      avg_msavi = sum(msaviarr)/len(msaviarr)
      max_msavi = max(msaviarr)
      last_msavi = msaviarr[-1]
      second_msavi = msaviarr[-2]
      change_msavi = 100*((last_msavi- second_msavi)/second_msavi)
      msavi_year_average = msaviarr[-1:-17:-1]
      msavi_year_average_value = sum(msavi_year_average)/len(msavi_year_average)


      root = Tk()
      root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
      print (root.filename)
      root.withdraw()
      csv_path = root.filename

      df2 = pd.read_csv(csv_path)

      i = 0
      x = 4
      rainfall = []
      while(x):
         try:
            rain = (df2.loc[i,'precipitation'])
         except:
            break
         rain = float(rain)
         rainfall.append(rain)
         i = i+1
      avg_rainfall = sum(rainfall)/len(rainfall)
      database = DBConnect(host='db4free.net',user='sfmvitpune_ser',password='pk9423975167',database='sfmvitpune_db',port='3306')
      new_user = {'userid': newusername, 'passkey': newpassword , 'namei' : namefield ,'village' : villagename ,'district' : districtname, 'avg_evi': avg_evi,'max_evi': max_evi,'last_evi' : last_evi,'evi_year_average_value' : evi_year_average_value,'avg_ndwi' : avg_ndwi,'max_ndwi' : max_ndwi,'last_ndwi' : last_ndwi,'ndwi_year_average_value' : ndwi_year_average_value,'avg_msavi' : avg_msavi,'max_msavi' : max_msavi,'last_msavi' : last_msavi,'msavi_year_average_value' : msavi_year_average_value,'avg_rainfall' : avg_rainfall}
      database.insert(new_user,'INDIA2019')
      print("Data Has been added successfully")
      mainscreen()



























   def addwindow(newusername,newpassword,namefield,villagename,districtname):
      print(newusername,newpassword,namefield,villagename,districtname)
      #! /usr/bin/env python
      #  -*- coding: utf-8 -*-
      #
      # GUI module generated by PAGE version 4.26
      #  in conjunction with Tcl version 8.6
      #    Dec 13, 2019 10:41:14 PM +0530  platform: Windows NT

      import sys

      try:
         import Tkinter as tk
      except ImportError:
         import tkinter as tk

      try:
         import ttk
         py3 = False
      except ImportError:
         import tkinter.ttk as ttk
         py3 = True

      import add_window_support

      def vp_start_gui():
         '''Starting point when module is the main routine.'''
         global val, w, root
         root = tk.Tk()
         top = Toplevel1 (root)
         add_window_support.init(root, top)
         root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
         '''Starting point when module is imported by another program.'''
         global w, w_win, rt
         rt = root
         w = tk.Toplevel (root)
         top = Toplevel1 (w)
         add_window_support.init(w, top, *args, **kwargs)
         return (w, top)

      def destroy_Toplevel1():
         global w
         w.destroy()
         w = None

      class Toplevel1:
         def addmyfields(self):
            root.destroy()
            process(newusername,newpassword,namefield,villagename,districtname)
         def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'

            top.geometry("701x531+281+99")
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1, 1)
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.014, rely=0.019, relheight=0.951
              , relwidth=0.963)
            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#414141")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")

            self.addmyfiel_b = tk.Button(self.Frame1)
            self.addmyfiel_b.place(relx=0.222, rely=0.119, height=103, width=366)
            self.addmyfiel_b.configure(activebackground="#9d9d9d")
            self.addmyfiel_b.configure(activeforeground="#000000")
            self.addmyfiel_b.configure(background="#808040")
            self.addmyfiel_b.configure(borderwidth="10")
            self.addmyfiel_b.configure(disabledforeground="#a3a3a3")
            self.addmyfiel_b.configure(font="-family {Segoe UI} -size 24 -slant italic -underline 1")
            self.addmyfiel_b.configure(foreground="#000000")
            self.addmyfiel_b.configure(highlightbackground="#d9d9d9")
            self.addmyfiel_b.configure(highlightcolor="black")
            self.addmyfiel_b.configure(pady="0")
            self.addmyfiel_b.configure(text='''Add My Field''',command = self.addmyfields)

            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.03, rely=0.455, height=76, width=632)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#959595")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 18")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''1.This will Redirect you to the web browser .''')

            self.Label2 = tk.Label(self.Frame1)
            self.Label2.place(relx=0.03, rely=0.614, height=76, width=632)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#818181")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 19")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            self.Label2.configure(text='''2.Select Your Field on the map.''')

            self.Label3 = tk.Label(self.Frame1)
            self.Label3.place(relx=0.03, rely=0.792, height=66, width=632)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#727272")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 19")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(text='''3.Downlod CSV format data.''')

      if __name__ == '__main__':
         vp_start_gui()








   def nextwindow(newusername,newpassword):
      print(newusername)
      print(newpassword)
            #! /usr/bin/env python
      #  -*- coding: utf-8 -*-
      #
      # GUI module generated by PAGE version 4.26
      #  in conjunction with Tcl version 8.6
      #    Dec 13, 2019 10:19:38 PM +0530  platform: Windows NT

      import sys

      try:
         import Tkinter as tk
      except ImportError:
         import tkinter as tk

      try:
         import ttk
         py3 = False
      except ImportError:
         import tkinter.ttk as ttk
         py3 = True

      import unknown_support

      def vp_start_gui():
         '''Starting point when module is the main routine.'''
         global val, w, root
         root = tk.Tk()
         top = Toplevel1 (root)
         unknown_support.init(root, top)
         root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
         '''Starting point when module is imported by another program.'''
         global w, w_win, rt
         rt = root
         w = tk.Toplevel (root)
         top = Toplevel1 (w)
         unknown_support.init(w, top, *args, **kwargs)
         return (w, top)

      def destroy_Toplevel1():
         global w
         w.destroy()
         w = None

      class Toplevel1:
         def saves(self):
            namefield=self.name_field.get();
            villagename = self.village_name.get()
            districtname= self.District_name.get()
            root.destroy()
            addwindow(newusername,newpassword,namefield,villagename,districtname)
         def exits(self):
            exit()






         def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'

            top.geometry("863x712+361+136")
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1, 1)
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.012, rely=0.014, relheight=0.948
              , relwidth=0.956)
            self.Frame1.configure(relief='raised')
            self.Frame1.configure(borderwidth="15")
            self.Frame1.configure(relief="raised")
            self.Frame1.configure(background="#818181")
            self.Frame1.configure(highlightbackground="#d9d9d9")
            self.Frame1.configure(highlightcolor="black")

            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.109, rely=0.296, height=56, width=212)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#555555")
            self.Label1.configure(borderwidth="3")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 17")
            self.Label1.configure(foreground="#ffffff")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(relief="ridge")
            self.Label1.configure(text='''Name:''')

            self.Label2 = tk.Label(self.Frame1)
            self.Label2.place(relx=0.109, rely=0.444, height=56, width=212)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#595959")
            self.Label2.configure(borderwidth="3")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 16")
            self.Label2.configure(foreground="#ffffff")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
            self.Label2.configure(relief="ridge")
            self.Label2.configure(text='''Village''')

            self.Label3 = tk.Label(self.Frame1)
            self.Label3.place(relx=0.109, rely=0.578, height=56, width=212)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#5c5c5c")
            self.Label3.configure(borderwidth="3")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 16")
            self.Label3.configure(foreground="#ffffff")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(relief="ridge")
            self.Label3.configure(text='''District''')

            self.exit = tk.Button(self.Frame1)
            self.exit.place(relx=0.158, rely=0.756, height=63, width=206)
            self.exit.configure(activebackground="#ececec")
            self.exit.configure(activeforeground="#000000")
            self.exit.configure(background="#0080ff")
            self.exit.configure(borderwidth="7")
            self.exit.configure(disabledforeground="#a3a3a3")
            self.exit.configure(font="-family {Segoe UI} -size 14")
            self.exit.configure(foreground="#000000")
            self.exit.configure(highlightbackground="#d9d9d9")
            self.exit.configure(highlightcolor="black")
            self.exit.configure(pady="0")
            self.exit.configure(text='''Exit''',command = self.exits)

            self.save = tk.Button(self.Frame1)
            self.save.place(relx=0.558, rely=0.756, height=63, width=206)
            self.save.configure(activebackground="#ececec")
            self.save.configure(activeforeground="#000000")
            self.save.configure(background="#ff0000")
            self.save.configure(borderwidth="7")
            self.save.configure(disabledforeground="#a3a3a3")
            self.save.configure(font="-family {Segoe UI} -size 14")
            self.save.configure(foreground="#000000")
            self.save.configure(highlightbackground="#d9d9d9")
            self.save.configure(highlightcolor="black")
            self.save.configure(pady="0")
            self.save.configure(text='''Save''',command = self.saves)

            self.name_field = tk.Entry(self.Frame1)
            self.name_field.place(relx=0.509, rely=0.296,height=54, relwidth=0.393)
            self.name_field.configure(background="#fafafa")
            self.name_field.configure(disabledforeground="#a3a3a3")
            self.name_field.configure(font="TkFixedFont")
            self.name_field.configure(foreground="#000000")
            self.name_field.configure(highlightbackground="#d9d9d9")
            self.name_field.configure(highlightcolor="black")
            self.name_field.configure(insertbackground="black")
            self.name_field.configure(selectbackground="#c4c4c4")
            self.name_field.configure(selectforeground="black")

            self.District_name = tk.Entry(self.Frame1)
            self.District_name.place(relx=0.509, rely=0.578, height=54
              , relwidth=0.393)
            self.District_name.configure(background="white")
            self.District_name.configure(disabledforeground="#a3a3a3")
            self.District_name.configure(font="TkFixedFont")
            self.District_name.configure(foreground="#000000")
            self.District_name.configure(highlightbackground="#d9d9d9")
            self.District_name.configure(highlightcolor="black")
            self.District_name.configure(insertbackground="black")
            self.District_name.configure(selectbackground="#c4c4c4")
            self.District_name.configure(selectforeground="black")

            self.village_name = tk.Entry(self.Frame1)
            self.village_name.place(relx=0.509, rely=0.444, height=54
              , relwidth=0.393)
            self.village_name.configure(background="white")
            self.village_name.configure(disabledforeground="#a3a3a3")
            self.village_name.configure(font="TkFixedFont")
            self.village_name.configure(foreground="#000000")
            self.village_name.configure(highlightbackground="#d9d9d9")
            self.village_name.configure(highlightcolor="black")
            self.village_name.configure(insertbackground="black")
            self.village_name.configure(selectbackground="#c4c4c4")
            self.village_name.configure(selectforeground="black")

            self.Label4 = tk.Label(self.Frame1)
            self.Label4.place(relx=0.206, rely=0.059, height=106, width=552)
            self.Label4.configure(activebackground="#f9f9f9")
            self.Label4.configure(activeforeground="black")
            self.Label4.configure(background="#d9d9d9")
            self.Label4.configure(borderwidth="8")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font="-family {Segoe UI} -size 21 -weight bold")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(highlightbackground="#d9d9d9")
            self.Label4.configure(highlightcolor="black")
            self.Label4.configure(relief="groove")
            self.Label4.configure(text='''New Field Registration''')

      if __name__ == '__main__':
         vp_start_gui()







   def newuser1():
            #! /usr/bin/env python
      #  -*- coding: utf-8 -*-
      #
      # GUI module generated by PAGE version 4.26
      #  in conjunction with Tcl version 8.6
      #    Dec 13, 2019 09:31:24 PM +0530  platform: Windows NT

      import sys

      try:
         import Tkinter as tk
      except ImportError:
         import tkinter as tk

      try:
         import ttk
         py3 = False
      except ImportError:
         import tkinter.ttk as ttk
         py3 = True

      import new_user_page_support

      def vp_start_gui():
         '''Starting point when module is the main routine.'''
         global val, w, root
         root = tk.Tk()
         top = Toplevel1 (root)
         new_user_page_support.init(root, top)
         root.mainloop()

      w = None
      def create_Toplevel1(root, *args, **kwargs):
         '''Starting point when module is imported by another program.'''
         global w, w_win, rt
         rt = root
         w = tk.Toplevel (root)
         top = Toplevel1 (w)
         new_user_page_support.init(w, top, *args, **kwargs)
         return (w, top)

      def destroy_Toplevel1():
         global w
         w.destroy()
         w = None

      class Toplevel1:
         def backs(self):
            root.destroy()
            main()

         def exits(self):
            exit()

         def succeeds(self):
            newusername=self.new_username.get();
            newpassword = self.new_password.get()
            confirmpassword = self.confirm_password.get()
            root.destroy()

            if newpassword == confirmpassword:
               nextwindow(newusername,newpassword)
            else:
               newuser1()




         def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
            font10 = "-family Subway -size 30 -weight bold -slant italic "  \
               "-underline 0 -overstrike 0"

            top.geometry("1244x819+96+74")
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1, 1)
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.024, rely=0.037, relheight=0.91, relwidth=0.945)

            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#585858")
            self.Frame1.configure(highlightbackground="#e7faf4")
            self.Frame1.configure(highlightcolor="#648840")

            self.Frame2 = tk.Frame(self.Frame1)
            self.Frame2.place(relx=0.051, rely=0.242, relheight=0.678
              , relwidth=0.668)
            self.Frame2.configure(relief='ridge')
            self.Frame2.configure(borderwidth="10")
            self.Frame2.configure(relief="ridge")
            self.Frame2.configure(background="#d9d9d9")
            self.Frame2.configure(highlightbackground="#d9d9d9")
            self.Frame2.configure(highlightcolor="black")
            self.Frame2.configure(padx="10")
            self.Frame2.configure(pady="10")

            self.fra43_fra44_lab48 = tk.Label(self.Frame2)
            self.fra43_fra44_lab48.place(relx=0.153, rely=0.158, height=56
              , width=152)
            self.fra43_fra44_lab48.configure(activebackground="#f9f9f9")
            self.fra43_fra44_lab48.configure(activeforeground="black")
            self.fra43_fra44_lab48.configure(background="#c4c4c4")
            self.fra43_fra44_lab48.configure(disabledforeground="#a3a3a3")
            self.fra43_fra44_lab48.configure(font="-family {Segoe UI} -size 14")
            self.fra43_fra44_lab48.configure(foreground="#000000")
            self.fra43_fra44_lab48.configure(highlightbackground="#d9d9d9")
            self.fra43_fra44_lab48.configure(highlightcolor="black")
            self.fra43_fra44_lab48.configure(relief="ridge")
            self.fra43_fra44_lab48.configure(text='''USERNAME:''')

            self.Label3 = tk.Label(self.Frame2)
            self.Label3.place(relx=0.153, rely=0.317, height=56, width=152)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(activeforeground="black")
            self.Label3.configure(background="#b1b1b1")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 13")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(highlightbackground="#d9d9d9")
            self.Label3.configure(highlightcolor="black")
            self.Label3.configure(relief="ridge")
            self.Label3.configure(text='''PASSWORD:''')

            self.Label4 = tk.Label(self.Frame2)
            self.Label4.place(relx=0.127, rely=0.475, height=56, width=192)
            self.Label4.configure(activebackground="#f9f9f9")
            self.Label4.configure(activeforeground="black")
            self.Label4.configure(background="#666666")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(font="-family {Segoe UI} -size 10")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(highlightbackground="#d9d9d9")
            self.Label4.configure(highlightcolor="black")
            self.Label4.configure(relief="ridge")
            self.Label4.configure(text='''CONFIRM PASSWORD''')

            self.succeed_but = tk.Button(self.Frame2)
            self.succeed_but.place(relx=0.102, rely=0.713, height=93, width=606)
            self.succeed_but.configure(activebackground="#ececec")
            self.succeed_but.configure(activeforeground="#000000")
            self.succeed_but.configure(background="#008080")
            self.succeed_but.configure(borderwidth="10")
            self.succeed_but.configure(cursor="fleur")
            self.succeed_but.configure(disabledforeground="#a3a3a3")
            self.succeed_but.configure(font="-family {Segoe UI} -size 20 -slant italic")
            self.succeed_but.configure(foreground="#000000")
            self.succeed_but.configure(highlightbackground="#d9d9d9")
            self.succeed_but.configure(highlightcolor="black")
            self.succeed_but.configure(padx="10")
            self.succeed_but.configure(pady="0")
            self.succeed_but.configure(text='''Sign up & Add Field''',command = self.succeeds)

            self.new_username = tk.Entry(self.Frame2)
            self.new_username.place(relx=0.484, rely=0.158, height=46
              , relwidth=0.372)
            self.new_username.configure(background="white")
            self.new_username.configure(disabledforeground="#a3a3a3")
            self.new_username.configure(font="TkFixedFont")
            self.new_username.configure(foreground="#000000")
            self.new_username.configure(highlightbackground="#d9d9d9")
            self.new_username.configure(highlightcolor="black")
            self.new_username.configure(insertbackground="#000000")
            self.new_username.configure(selectbackground="#c4c4c4")
            self.new_username.configure(selectforeground="black")

            self.new_password = tk.Entry(self.Frame2)
            self.new_password.place(relx=0.484, rely=0.317, height=46
              , relwidth=0.372)
            self.new_password.configure(background="white")
            self.new_password.configure(disabledforeground="#a3a3a3")
            self.new_password.configure(font="TkFixedFont")
            self.new_password.configure(foreground="#000000")
            self.new_password.configure(highlightbackground="#d9d9d9")
            self.new_password.configure(highlightcolor="black")
            self.new_password.configure(insertbackground="black")
            self.new_password.configure(selectbackground="#c4c4c4")
            self.new_password.configure(selectforeground="black")

            self.confirm_password = tk.Entry(self.Frame2)
            self.confirm_password.place(relx=0.484, rely=0.475, height=46
              , relwidth=0.372)
            self.confirm_password.configure(background="white")
            self.confirm_password.configure(disabledforeground="#a3a3a3")
            self.confirm_password.configure(font="TkFixedFont")
            self.confirm_password.configure(foreground="#000000")
            self.confirm_password.configure(highlightbackground="#d9d9d9")
            self.confirm_password.configure(highlightcolor="black")
            self.confirm_password.configure(insertbackground="black")
            self.confirm_password.configure(selectbackground="#c4c4c4")
            self.confirm_password.configure(selectforeground="black")

            self.back = tk.Button(self.Frame1)
            self.back.place(relx=0.757, rely=0.362, height=53, width=156)
            self.back.configure(activebackground="#ececec")
            self.back.configure(activeforeground="#000000")
            self.back.configure(background="#008000")
            self.back.configure(borderwidth="10")
            self.back.configure(disabledforeground="#a3a3a3")
            self.back.configure(font="-family {Segoe UI} -size 14")
            self.back.configure(foreground="#000000")
            self.back.configure(highlightbackground="#d9d9d9")
            self.back.configure(highlightcolor="black")
            self.back.configure(pady="0")
            self.back.configure(text='''Back''',command = self.backs)

            self.exit = tk.Button(self.Frame1)
            self.exit.place(relx=0.757, rely=0.483, height=53, width=156)
            self.exit.configure(activebackground="#ececec")
            self.exit.configure(activeforeground="#000000")
            self.exit.configure(background="#ff0000")
            self.exit.configure(borderwidth="10")
            self.exit.configure(disabledforeground="#a3a3a3")
            self.exit.configure(font="-family {Segoe UI} -size 14")
            self.exit.configure(foreground="#000000")
            self.exit.configure(highlightbackground="#d9d9d9")
            self.exit.configure(highlightcolor="black")
            self.exit.configure(pady="0")
            self.exit.configure(text='''Exit''',command = self.exits)

            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.136, rely=0.04, height=126, width=612)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="#868686")
            self.Label1.configure(background="#adadad")
            self.Label1.configure(borderwidth="10")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font=font10)
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(relief="ridge")
            self.Label1.configure(text='''New User Registration''')

      if __name__ == '__main__':
         vp_start_gui()



























































   #! /usr/bin/env python
   #  -*- coding: utf-8 -*-
   #
   # GUI module generated by PAGE version 4.26
   #  in conjunction with Tcl version 8.6
   #    Dec 13, 2019 07:35:55 PM +0530  platform: Windows NT

   import sys

   try:
      import Tkinter as tk
   except ImportError:
      import tkinter as tk

   try:
      import ttk
      py3 = False
   except ImportError:
      import tkinter.ttk as ttk
      py3 = True

   import loginpage_support

   def vp_start_gui():
      '''Starting point when module is the main routine.'''
      global val, w, root
      root = tk.Tk()
      top = Toplevel1 (root)
      loginpage_support.init(root, top)
      root.mainloop()

   w = None
   def create_Toplevel1(root, *args, **kwargs):
      '''Starting point when module is imported by another program.'''
      global w, w_win, rt
      rt = root
      w = tk.Toplevel (root)
      top = Toplevel1 (w)
      loginpage_support.init(w, top, *args, **kwargs)
      return (w, top)

   def destroy_Toplevel1():
      global w
      w.destroy()
      w = None

   class Toplevel1:
      def newuser(self):
         root.destroy()
         newuser1()

      def loginuser(self):
         name=self.user_e.get();               # taking username input
         password1=self.password_e.get();           # taking password input
         try :
            u='\''+name+'\''
            mydb=mysql.connector.connect(host='db4free.net',user='sfmvitpune_ser',password='pk9423975167',database='sfmvitpune_db',port='3306')
            msg = tk.messagebox.showinfo('SFAVIT','MySQL Database Connection successful')
            mycursor=mydb.cursor()
            query = ("SELECT passkey FROM INDIA2019 WHERE userid ="+u)
            mycursor.execute(query)
            for(passkey) in mycursor:
               s="{}".format(passkey)
               s=str(s[2:len(s)-3])
               if s==password1:
                  msg = tk.messagebox.showinfo('SFAVIT','Access Granted')
                  root.destroy()
                  mainscreen()
               else:
                  msg = tk.messagebox.showerror("SFAVIT",'Incorrect Password')
         except:
            msg=tk.messagebox.showerror("Login Page","Server Connection Failed. Please contact the administrator");
            os._exit(1)

      def __init__(self, top=None):
         '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
         _fgcolor = '#000000'  # X11 color: 'black'
         _compcolor = '#d9d9d9' # X11 color: 'gray85'
         _ana1color = '#d9d9d9' # X11 color: 'gray85'
         _ana2color = '#ececec' # Closest X11 color: 'gray92'
         font11 = "-family {Agency FB} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

         top.geometry("760x671+269+72")
         top.minsize(148, 1)
         top.maxsize(1924, 1055)
         top.resizable(1, 1)
         top.title("New Toplevel")
         top.configure(background="#d9d9d9")
         top.configure(highlightbackground="#d9d9d9")
         top.configure(highlightcolor="black")

         self.Frame1 = tk.Frame(top)
         self.Frame1.place(relx=0.013, rely=0.015, relheight=0.976
               , relwidth=0.954)
         self.Frame1.configure(relief='groove')
         self.Frame1.configure(borderwidth="2")
         self.Frame1.configure(relief="groove")
         self.Frame1.configure(background="#454545")
         self.Frame1.configure(highlightbackground="#d9d9d9")
         self.Frame1.configure(highlightcolor="black")

         self.Frame3 = tk.Frame(self.Frame1)
         self.Frame3.place(relx=0.138, rely=0.153, relheight=0.282
               , relwidth=0.752)
         self.Frame3.configure(relief='groove')
         self.Frame3.configure(borderwidth="2")
         self.Frame3.configure(relief="groove")
         self.Frame3.configure(background="#b2b2b2")
         self.Frame3.configure(highlightbackground="#d9d9d9")
         self.Frame3.configure(highlightcolor="black")

         self.Label3 = tk.Label(self.Frame3)
         self.Label3.place(relx=0.055, rely=0.162, height=136, width=502)
         self.Label3.configure(activebackground="#f9f9f9")
         self.Label3.configure(activeforeground="black")
         self.Label3.configure(background="#d9d9d9")
         self.Label3.configure(disabledforeground="#a3a3a3")
         self.Label3.configure(font=font11)
         self.Label3.configure(foreground="#000000")
         self.Label3.configure(highlightbackground="#d9d9d9")
         self.Label3.configure(highlightcolor="black")
         self.Label3.configure(text='''FIELD ANALYSIS USING SATELLITE  DATA''')

         self.Frame4 = tk.Frame(self.Frame1)
         self.Frame4.place(relx=0.166, rely=0.489, relheight=0.42, relwidth=0.71)
         self.Frame4.configure(relief='groove')
         self.Frame4.configure(borderwidth="2")
         self.Frame4.configure(relief="groove")
         self.Frame4.configure(background="#b2b2b2")
         self.Frame4.configure(highlightbackground="#d9d9d9")
         self.Frame4.configure(highlightcolor="black")

         self.user_namel = tk.Label(self.Frame4)
         self.user_namel.place(relx=0.078, rely=0.145, height=46, width=162)
         self.user_namel.configure(activebackground="#f9f9f9")
         self.user_namel.configure(activeforeground="black")
         self.user_namel.configure(background="#d9d9d9")
         self.user_namel.configure(disabledforeground="#a3a3a3")
         self.user_namel.configure(foreground="#000000")
         self.user_namel.configure(highlightbackground="#d9d9d9")
         self.user_namel.configure(highlightcolor="black")
         self.user_namel.configure(text='''USERNAME:''')

         self.password_label = tk.Label(self.Frame4)
         self.password_label.place(relx=0.078, rely=0.436, height=46, width=162)
         self.password_label.configure(activebackground="#f9f9f9")
         self.password_label.configure(activeforeground="black")
         self.password_label.configure(background="#d9d9d9")
         self.password_label.configure(disabledforeground="#a3a3a3")
         self.password_label.configure(foreground="#000000")
         self.password_label.configure(highlightbackground="#d9d9d9")
         self.password_label.configure(highlightcolor="black")
         self.password_label.configure(text='''PASSWORD:''')

         self.user_e = tk.Entry(self.Frame4)
         self.user_e.place(relx=0.466, rely=0.145,height=44, relwidth=0.396)
         self.user_e.configure(background="white")
         self.user_e.configure(disabledforeground="#a3a3a3")
         self.user_e.configure(font="TkFixedFont")
         self.user_e.configure(foreground="#000000")
         self.user_e.configure(highlightbackground="#d9d9d9")
         self.user_e.configure(highlightcolor="black")
         self.user_e.configure(insertbackground="black")
         self.user_e.configure(selectbackground="#c4c4c4")
         self.user_e.configure(selectforeground="black")

         self.password_e = tk.Entry(self.Frame4)
         self.password_e.place(relx=0.466, rely=0.436,height=44, relwidth=0.396)
         self.password_e.configure(background="white")
         self.password_e.configure(disabledforeground="#a3a3a3")
         self.password_e.configure(font="TkFixedFont")
         self.password_e.configure(foreground="#000000")
         self.password_e.configure(highlightbackground="#d9d9d9")
         self.password_e.configure(highlightcolor="black")
         self.password_e.configure(insertbackground="black")
         self.password_e.configure(selectbackground="#c4c4c4")
         self.password_e.configure(selectforeground="black")

         self.newuser_e = tk.Button(self.Frame4)
         self.newuser_e.place(relx=0.155, rely=0.727, height=43, width=136)
         self.newuser_e.configure(activebackground="#ececec")
         self.newuser_e.configure(activeforeground="#000000")
         self.newuser_e.configure(background="#ff0000")
         self.newuser_e.configure(disabledforeground="#a3a3a3")
         self.newuser_e.configure(foreground="#000000")
         self.newuser_e.configure(highlightbackground="#d9d9d9")
         self.newuser_e.configure(highlightcolor="black")
         self.newuser_e.configure(pady="0")
         self.newuser_e.configure(command = self.newuser,text='''NEW''')

         self.submit_e = tk.Button(self.Frame4)
         self.submit_e.place(relx=0.524, rely=0.727, height=43, width=146)
         self.submit_e.configure(activebackground="#ececec")
         self.submit_e.configure(activeforeground="#000000")
         self.submit_e.configure(background="#00ff80")
         self.submit_e.configure(disabledforeground="#a3a3a3")
         self.submit_e.configure(foreground="#000000")
         self.submit_e.configure(highlightbackground="#d9d9d9")
         self.submit_e.configure(highlightcolor="black")
         self.submit_e.configure(pady="0")
         self.submit_e.configure(command = self.loginuser,text='''SUBMIT''')

   if __name__ == '__main__':
      vp_start_gui()




main()
