import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
import os

def menu():

   print()
   print("******************************************************************************")
   print("        Welcome To Social Media Site User Management System            ")
   print("******************************************************************************")
   print("                                 Menu                               ")
   print("                   *************************************                     ")
   print()
   print(" -> Data Analysis:")
   print("        1) Reading file without index")
   print("        2) Reading file with new column names")
   print("        3) Sorting the values in ascending order of Names")
   print(" -> Data Visualization:")
   print("        4) Line plot")
   print("        5) Bar Plot")
   print("        6) Horizontal Bar Plot")
   print(" -> Data Manipulation:")
   print("        7) Extracting the middle row from the file ")
   print("        8) Reading 4 records from top and 6 from bottom of the file")
   print("        9) Duplicate file with new user-defined name")
   print("        10) Replacing NaN values with zeroes")
   print("        11) Create a CSV file with data frame ")
   print("        12) Read previously created CSV file " )
   print()
   print("******************************************************************************")

menu()

                                  #For Option (1)
def no_index():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1',index_col=0)
         pd.set_option("display.max_rows",None)
         pd.set_option("display.max_columns",None)
         pd.set_option("display.width",None)
         pd.set_option("expand_frame_repr",False)
         df['Mobile No.'] = df['Mobile No.'].astype('Int64')
         df.head()
         print("Reading file without index....")
         time.sleep(4)
         print(df)
                                  #For Option (2)
def new_colnames():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1',skiprows=1,names=("ID","NAME","DATE OF BIRTH","AGE","SEX","EMAIL","COUNTRY","AREA","CONTACT NUMBER","REGISTRATION DATE","ACCOUNT STATUS"))
         pd.set_option("display.max_rows",None)
         pd.set_option("display.max_columns",None)
         pd.set_option("display.width",None)
         pd.set_option("expand_frame_repr",False)
         df['CONTACT NUMBER'] = df['CONTACT NUMBER'].astype('Int64')
         df.head()
         print("Reading file with new column names....")
         time.sleep(4)
         print(df)


                                  #For Option (3)
def sort_val_asc():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
         pd.set_option("display.max_rows",None)
         pd.set_option("display.max_columns",None)
         pd.set_option("display.width",None)
         pd.set_option("expand_frame_repr",False)
         df['Mobile No.'] = df['Mobile No.'].astype('Int64')
         df.head()
         df.sort_values(by=['User Name'],inplace=True)
         print("Sorting the values in ascending oder of Name....")
         time.sleep(4)
         print(df)


                                   #For Option (4)
def line_plot():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
         df['DOR'] = pd.to_datetime(df['DOR'], infer_datetime_format=True)
         df['year']= pd.DatetimeIndex(df['DOR']).year
         dfp=df.pivot_table(columns = df['year'],aggfunc
         ='size').plot(kind='line',color='#1C86EE',marker='o',markersize=11,label='Users')
         plt.xlabel("Years")
         plt.ylabel("No. of users")
         plt.title("Number of user registration from 2018-2022")
         plt.grid(True)
         plt.legend(loc='upper left')
         plt.xticks(ticks=plt.xticks()[0].astype(int))
         print("Creating line chart....")
         time.sleep(4)
         print("Line chart created successfully!")
         time.sleep(1)
         plt.show()
                                     #For Option (5)
def bar_plot():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
         d=df.pivot_table(index = ['Age'],aggfunc ='size')
         df['age_group'] = pd.cut(df['Age'], [0,25,45,59,70],labels=['15-25', '26-45', '46-59','Above 60'])
         df['age_group'].value_counts().sort_index().plot.bar()
         plt.title("Number of users in different age group")
         plt.xlabel("Age Groups")
         plt.ylabel("No. of users")
         print("Creating bar chart....")
         time.sleep(4)
         print("Bar chart created successfully!")
         time.sleep(1)
         plt.show()


                                     #For Option (6)
def horizon_bar_plot():
         df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
         d=df.pivot_table(index = ['Country'],aggfunc ='size').plot(kind='barh',color='coral')
         plt.xlabel("No. of users")
         plt.ylabel("Countries")
         plt.title("Number of users from different countries")
         print("Creating horizontal bar chart....")
         time.sleep(4)
         print("Horizontal bar chart created successfully!")
         time.sleep(1)
         plt.show()


                                     #For Option (7)
def middle_row():
        df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1',nrows=23)
        pd.set_option("display.max_rows",None)
        pd.set_option("display.max_columns",None)
        pd.set_option("display.width",None)
        pd.set_option("expand_frame_repr",False)
        df['Mobile No.'] = df['Mobile No.'].astype('Int64')
        df.head()
        print("Fetching the middle row from the file.... ")
        time.sleep(4)
        print(df.tail(1))
                                     #For Option (8)
def top_bottom():
        df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
        pd.set_option("display.max_rows",None)
        pd.set_option("display.max_columns",None)
        pd.set_option("display.width",None)
        pd.set_option("expand_frame_repr",False)
        df['Mobile No.'] = df['Mobile No.'].astype('Int64')
        df.head()
        print("Fetching top 4 rows from the file....")
        time.sleep(4)
        print(df.head(4))
        time.sleep(1)
        print()
        print("Fetching last 6 rows from the file....")
        time.sleep(4)
        print(df.tail(6))


                                     #For Option (9)
def duplicate():
        df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
        name_input=eval(input(" -> Enter the file path and file name for your duplicate file (within double quotes and two backslashes): "))
        df.to_csv(name_input)
        pd.set_option("display.max_rows",None)
        pd.set_option("display.max_columns",None)
        pd.set_option("display.width",None)
        pd.set_option("expand_frame_repr",False)
        df['Mobile No.'] = df['Mobile No.'].astype('Int64')
        print("Please wait... Duplicate file is being created")
        time.sleep(4)
        print("Duplicate file with the name","'",os.path.basename(name_input),"'"," created successfully!")
        time.sleep(2)
        print(df)


                                    #For Option (10)
def fill_nan():
       df=pd.read_csv("social_media_site_users_data.csv",encoding='latin-1')
       pd.set_option("display.max_rows",None)
       pd.set_option("display.max_columns",None)
       pd.set_option("display.width",None)
       pd.set_option("expand_frame_repr",False)
       df['Mobile No.'] = df['Mobile No.'].astype('Int64')
       df.head()
       df["Mobile No."].fillna(0, inplace = True)
       print("Filling NaN values of the file....")
       time.sleep(4)
       print(df)
       print("Successfully replaced NaNs with zeroes!")


                                      #For Option (11)
def create_csv():
      users_df={"Name":["Ada Braun","Rakhi Soni","Derek Tyson","Anuj Sharma","Lucas Cabello"],"Age":[20,44,29,31,23],"Country":["Germany","India","Australia","India","Mexico"]}
      users=pd.DataFrame(users_df)
      print(users)
      print()
      users.to_csv("user_details.csv",index=False)
      time.sleep(1)
      print("Creating csv file of the above dataframe....")
      time.sleep(4)
      print("CSV file 'user_details.csv' created successfully!")


                                      #For Option (12)
def reading_prev_csv():
      print("Reading the previously created csv file 'user_details.csv'....")
      time.sleep(4)
      print()
      read_user_details=pd.read_csv("user_details.csv")
      print(read_user_details)


           #For choosing Options and execution of commands
while True:
    opt=" "
    opt=int(input(" -> Enter your choice (1 to 12): "))

    if opt==1:
              no_index()
    elif opt==2:
              new_colnames()
    elif opt==3:
              sort_val_asc()
    elif opt==4:
              line_plot()
    elif opt==5:
              bar_plot()
    elif opt==6:
              horizon_bar_plot()
    elif opt==7:
              middle_row()
    elif opt==8:
              top_bottom()
    elif opt==9:
            duplicate()
    elif opt==10:
            fill_nan()
    elif opt==11:
            create_csv()
    elif opt==12:
                reading_prev_csv()
    else:
        time.sleep(1)
        print("Invalid input! Please choose a valid option (1 to 12)")
        time.sleep(1)
        ch=input(" -> Do you wish to continue? -Y/N ")
        if(ch=='N' or ch=='n'):
               print("Quitting....")
               time.sleep(4)
               break
        elif(ch=='Y' or ch=='y'):
              print("Please wait....")
              time.sleep(2)
              menu()
        else:
            time.sleep(1)
            print("Invalid input! Press Y /y for 'Yes' or N/n for 'No'")
            time.sleep(1)
            ch=input(" -> Do you wish to continue? -Y/N ")
            if(ch=='N' or ch=='n'):
                  print("Quitting....")
                  time.sleep(4)
                  break
            else:
                print("Please wait....")
                time.sleep(2)
                menu()


