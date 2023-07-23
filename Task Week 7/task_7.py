# Name :  Yati Maheshwari
# Task-7
# Creat script in python program using web scrapping  generate report of colleges Data like College name, URL,address,email id,phone number.

try:
    import pandas as pd
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import requests
    from lxml import etree
    my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", 
                  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
    url = 'https://targetstudy.com/colleges/engineering-colleges-in-india.html'
    session = requests.Session()
except ImportError as ie:
    print("It cannot import module and submodule", ie)

class extract_clg_data:
    def __init__(self,College_Name,State,City, URL , Address , Phone_number):
        self.College_Name = College_Name
        self.State = State
        self.City = City
        self.URL_ =URL
        self.Address = Address
        # self.Email_ID = Email_Id
        self.Phone_Number = Phone_number
object = []
# all college data
def report_of_clg_data():
    try:
        for i in range(0,6000,10):
            response = session.get('https://targetstudy.com/colleges/computer-and-it-colleges-in-india.html?recNo={}'.format(i),headers=my_headers)
            # soup = BeautifulSoup(response.text,'html.parser')
            soup = BeautifulSoup(response.content, "html.parser")
            dom = etree.HTML(str(soup))
            clg_url = dom.xpath("//div[@class = 'col-12']//div[@class='media-body']//h5//a")
            for i in clg_url:
                # print(i.get('href'))
                clg_url_open= session.get(i.get('href'),headers=my_headers)
                soup_ = BeautifulSoup(clg_url_open.content,"html.parser")
                dom_ =etree.HTML(str(soup_))
                clg_name_path = dom_.xpath("//div[@class = 'media-body align-items-center align-self-md-end']//h1")
                clg_name_path_1 = dom_.xpath("//div[@class = 'align-self-end col-lg-12']//h1")
                if len(clg_name_path) > 0:
                    clg_name = clg_name_path[0].text
                elif len(clg_name_path_1) > 0:
                    clg_name = clg_name_path_1[0].text
                else:
                    clg_name = None
                # print(clg_name)
                # clg_url_path = dom_.xpath("//div[@class = 'tab-pane active']/a")
                clg_url_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[5]//div//a")
                clg_url_path_1 = dom_.xpath("//ul[@class ='list-group pmd-list']//li[4]//div//a")
                if len(clg_url_path) > 0:
                    clg_url = clg_url_path[0].get('href')
                elif len(clg_url_path_1)>0:
                    clg_url = clg_url_path_1[0].get('href')
                else:
                    clg_url = None
                # print(clg_url)
                clg_address_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[1]//div//h5")
                if len(clg_address_path) > 0 :
                    clg_address = clg_address_path[0].text
                else:
                    clg_address = None
                # print(clg_address)
                clg_phn_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[2]//div//h5/text()")
                if len(clg_phn_path) > 0 :
                    clg_phn = clg_phn_path
                else:
                    clg_phn = None
                # print(clg_phn)
                clg_city_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[4]//a")
                clg_city_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[4]//a")
                if len(clg_city_path) > 0 :
                    clg_city = clg_city_path[0].text
                elif len(clg_city_path_1) > 0:
                    clg_city = clg_city_path_1[0].text
                else:
                    clg_city = None
                # print(clg_city)
                clg_state_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_state_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[3]//a")
                if len(clg_state_path) > 0 :
                    clg_state = clg_state_path[0].text
                elif len(clg_state_path_1)>0:
                    clg_state = clg_state_path_1[0].text
                else:
                    clg_state = None
                # print(clg_city)

                object.append(extract_clg_data(clg_name,clg_state,clg_city,clg_url,clg_address,clg_phn).__dict__)
                # print('yes')
    except Exception as ex:
        print(ex)
# report_of_clg_data()

# dataframe = pd.DataFrame(object)
# dataframe.to_csv('College_Data.csv')
# print('data')


# Mumbai college data
def report_of_Mumbai_clg():
    try:
        for i in range(0,80,10):
            response = session.get('https://targetstudy.com/colleges/engineering-colleges-in-mumbai.html?recNo={}'.format(i),headers=my_headers)
            # soup = BeautifulSoup(response.text,'html.parser')
            soup = BeautifulSoup(response.content, "html.parser")
            dom = etree.HTML(str(soup))
            clg_url = dom.xpath("//div[@class = 'col-12']//div[@class='media-body']//h5//a")
            for i in clg_url:
                # print(i.get('href'))
                clg_url_open= session.get(i.get('href'),headers=my_headers)
                soup_ = BeautifulSoup(clg_url_open.content,"html.parser")
                dom_ =etree.HTML(str(soup_))
                clg_name_path = dom_.xpath("//div[@class = 'media-body align-items-center align-self-md-end']//h1")
                clg_name_path_1 = dom_.xpath("//div[@class = 'align-self-end col-lg-12']//h1")
                if len(clg_name_path) > 0:
                    clg_name = clg_name_path[0].text
                elif len(clg_name_path_1) > 0:
                    clg_name = clg_name_path_1[0].text
                else:
                    clg_name = None
                # print(clg_name)
                # clg_url_path = dom_.xpath("//div[@class = 'tab-pane active']/a")
                clg_url_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[5]//div//a")
                clg_url_path_1 = dom_.xpath("//ul[@class ='list-group pmd-list']//li[4]//div//a")
                if len(clg_url_path) > 0:
                    clg_url = clg_url_path[0].get('href')
                elif len(clg_url_path_1)>0:
                    clg_url = clg_url_path_1[0].get('href')
                else:
                    clg_url = None
                # print(clg_url)
                clg_address_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[1]//div//h5")
                if len(clg_address_path) > 0 :
                    clg_address = clg_address_path[0].text
                else:
                    clg_address = None
                # print(clg_address)
                clg_phn_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[2]//div//h5/text()")
                if len(clg_phn_path) > 0 :
                    clg_phn = clg_phn_path
                else:
                    clg_phn = None
                # print(clg_phn)
                clg_city_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[4]//a")
                # clg_city_path_2 = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_city_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[4]//a")
                if len(clg_city_path) > 0 :
                    clg_city = clg_city_path[0].text
                elif len(clg_city_path_1) > 0:
                    clg_city = clg_city_path_1[0].text
                # elif len (clg_city_path_2) > 0:
                #     clg_city = clg_city_path_2[0].text
                else:
                    clg_city = None
                # print(clg_city)
                clg_state_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_state_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[3]//a")
                if len(clg_state_path) > 0 :
                    clg_state = clg_state_path[0].text
                elif len(clg_state_path_1)>0:
                    clg_state = clg_state_path_1[0].text
                else:
                    clg_state = None
                # print(clg_city)

                object.append(extract_clg_data(clg_name,clg_state,clg_city,clg_url,clg_address,clg_phn).__dict__)
                # print('yes')
    except Exception as ex:
        print(ex)

# Delhi college data
def report_of_Delhi_clg():
    try:
        for i in range(0,160,10):
            response = session.get('https://targetstudy.com/colleges/computer-and-it-colleges-in-delhi.html?recNo={}'.format(i),headers=my_headers)
            # soup = BeautifulSoup(response.text,'html.parser')
            soup = BeautifulSoup(response.content, "html.parser")
            dom = etree.HTML(str(soup))
            clg_url = dom.xpath("//div[@class = 'col-12']//div[@class='media-body']//h5//a")
            for i in clg_url:
                # print(i.get('href'))
                clg_url_open= session.get(i.get('href'),headers=my_headers)
                soup_ = BeautifulSoup(clg_url_open.content,"html.parser")
                dom_ =etree.HTML(str(soup_))
                clg_name_path = dom_.xpath("//div[@class = 'media-body align-items-center align-self-md-end']//h1")
                clg_name_path_1 = dom_.xpath("//div[@class = 'align-self-end col-lg-12']//h1")
                if len(clg_name_path) > 0:
                    clg_name = clg_name_path[0].text
                elif len(clg_name_path_1) > 0:
                    clg_name = clg_name_path_1[0].text
                else:
                    clg_name = None
                # print(clg_name)
                # clg_url_path = dom_.xpath("//div[@class = 'tab-pane active']/a")
                clg_url_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[5]//div//a")
                clg_url_path_1 = dom_.xpath("//ul[@class ='list-group pmd-list']//li[4]//div//a")
                if len(clg_url_path) > 0:
                    clg_url = clg_url_path[0].get('href')
                elif len(clg_url_path_1)>0:
                    clg_url = clg_url_path_1[0].get('href')
                else:
                    clg_url = None
                # print(clg_url)
                clg_address_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[1]//div//h5")
                if len(clg_address_path) > 0 :
                    clg_address = clg_address_path[0].text
                else:
                    clg_address = None
                # print(clg_address)
                clg_phn_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[2]//div//h5/text()")
                if len(clg_phn_path) > 0 :
                    clg_phn = clg_phn_path
                else:
                    clg_phn = None
                # print(clg_phn)
                clg_city_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[4]//a")
                clg_city_path_2 = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_city_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[4]//a")
                if len(clg_city_path) > 0 :
                    clg_city = clg_city_path[0].text
                elif len(clg_city_path_1) > 0:
                    clg_city = clg_city_path_1[0].text
                elif len (clg_city_path_2) > 0:
                    clg_city = clg_city_path_2[0].text
                else:
                    clg_city = None
                # print(clg_city)
                clg_state_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_state_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[3]//a")
                if len(clg_state_path) > 0 :
                    clg_state = clg_state_path[0].text
                elif len(clg_state_path_1)>0:
                    clg_state = clg_state_path_1[0].text
                else:
                    clg_state = None
                # print(clg_city)

                object.append(extract_clg_data(clg_name,clg_state,clg_city,clg_url,clg_address,clg_phn).__dict__)
                # print('yes')
    except Exception as ex:
        print(ex)

# Kokata College Data
def report_of_kolkata_clg():
    try:
        for i in range(0,110,10):
            response = session.get('https://targetstudy.com/colleges/computer-and-it-colleges-in-kolkata.html?recNo={}'.format(i),headers=my_headers)
            # soup = BeautifulSoup(response.text,'html.parser')
            soup = BeautifulSoup(response.content, "html.parser")
            dom = etree.HTML(str(soup))
            clg_url = dom.xpath("//div[@class = 'col-12']//div[@class='media-body']//h5//a")
            for i in clg_url:
                # print(i.get('href'))
                clg_url_open= session.get(i.get('href'),headers=my_headers)
                soup_ = BeautifulSoup(clg_url_open.content,"html.parser")
                dom_ =etree.HTML(str(soup_))
                clg_name_path = dom_.xpath("//div[@class = 'media-body align-items-center align-self-md-end']//h1")
                clg_name_path_1 = dom_.xpath("//div[@class = 'align-self-end col-lg-12']//h1")
                if len(clg_name_path) > 0:
                    clg_name = clg_name_path[0].text
                elif len(clg_name_path_1) > 0:
                    clg_name = clg_name_path_1[0].text
                else:
                    clg_name = None
                # print(clg_name)
                # clg_url_path = dom_.xpath("//div[@class = 'tab-pane active']/a")
                clg_url_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[5]//div//a")
                clg_url_path_1 = dom_.xpath("//ul[@class ='list-group pmd-list']//li[4]//div//a")
                if len(clg_url_path) > 0:
                    clg_url = clg_url_path[0].get('href')
                elif len(clg_url_path_1)>0:
                    clg_url = clg_url_path_1[0].get('href')
                else:
                    clg_url = None
                # print(clg_url)
                clg_address_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[1]//div//h5")
                if len(clg_address_path) > 0 :
                    clg_address = clg_address_path[0].text
                else:
                    clg_address = None
                # print(clg_address)
                clg_phn_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[2]//div//h5/text()")
                if len(clg_phn_path) > 0 :
                    clg_phn = clg_phn_path
                else:
                    clg_phn = None
                # print(clg_phn)
                clg_city_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[4]//a")
                clg_city_path_2 = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_city_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[4]//a")
                if len(clg_city_path) > 0 :
                    clg_city = clg_city_path[0].text
                elif len(clg_city_path_1) > 0:
                    clg_city = clg_city_path_1[0].text
                elif len (clg_city_path_2) > 0:
                    clg_city = clg_city_path_2[0].text
                else:
                    clg_city = None
                # print(clg_city)
                clg_state_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_state_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[3]//a")
                if len(clg_state_path) > 0 :
                    clg_state = clg_state_path[0].text
                elif len(clg_state_path_1)>0:
                    clg_state = clg_state_path_1[0].text
                else:
                    clg_state = None
                # print(clg_city)

                object.append(extract_clg_data(clg_name,clg_state,clg_city,clg_url,clg_address,clg_phn).__dict__)
                # print('yes')
    except Exception as ex:
        print(ex)
# Chennai College data
def report_of_Chennai_clg():
    try:
        for i in range(0,170,10):
            response = session.get('https://targetstudy.com/colleges/computer-and-it-colleges-in-chennai.html?recNo={}'.format(i),headers=my_headers)
            # soup = BeautifulSoup(response.text,'html.parser')
            soup = BeautifulSoup(response.content, "html.parser")
            dom = etree.HTML(str(soup))
            clg_url = dom.xpath("//div[@class = 'col-12']//div[@class='media-body']//h5//a")
            for i in clg_url:
                # print(i.get('href'))
                clg_url_open= session.get(i.get('href'),headers=my_headers)
                soup_ = BeautifulSoup(clg_url_open.content,"html.parser")
                dom_ =etree.HTML(str(soup_))
                clg_name_path = dom_.xpath("//div[@class = 'media-body align-items-center align-self-md-end']//h1")
                clg_name_path_1 = dom_.xpath("//div[@class = 'align-self-end col-lg-12']//h1")
                if len(clg_name_path) > 0:
                    clg_name = clg_name_path[0].text
                elif len(clg_name_path_1) > 0:
                    clg_name = clg_name_path_1[0].text
                else:
                    clg_name = None
                # print(clg_name)
                # clg_url_path = dom_.xpath("//div[@class = 'tab-pane active']/a")
                clg_url_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[5]//div//a")
                clg_url_path_1 = dom_.xpath("//ul[@class ='list-group pmd-list']//li[4]//div//a")
                if len(clg_url_path) > 0:
                    clg_url = clg_url_path[0].get('href')
                elif len(clg_url_path_1)>0:
                    clg_url = clg_url_path_1[0].get('href')
                else:
                    clg_url = None
                # print(clg_url)
                clg_address_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[1]//div//h5")
                if len(clg_address_path) > 0 :
                    clg_address = clg_address_path[0].text
                else:
                    clg_address = None
                # print(clg_address)
                clg_phn_path = dom_.xpath("//ul[@class ='list-group pmd-list']//li[2]//div//h5/text()")
                if len(clg_phn_path) > 0 :
                    clg_phn = clg_phn_path
                else:
                    clg_phn = None
                # print(clg_phn)
                clg_city_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[4]//a")
                clg_city_path_2 = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_city_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[4]//a")
                if len(clg_city_path) > 0 :
                    clg_city = clg_city_path[0].text
                elif len(clg_city_path_1) > 0:
                    clg_city = clg_city_path_1[0].text
                elif len (clg_city_path_2) > 0:
                    clg_city = clg_city_path_2[0].text
                else:
                    clg_city = None
                # print(clg_city)
                clg_state_path = dom_.xpath("//ol[@class = 'breadcrumb breadcrumb-light']//li[3]//a")
                clg_state_path_1 = dom_.xpath("//ol[@class = 'breadcrumb']//li[3]//a")
                if len(clg_state_path) > 0 :
                    clg_state = clg_state_path[0].text
                elif len(clg_state_path_1)>0:
                    clg_state = clg_state_path_1[0].text
                else:
                    clg_state = None
                # print(clg_city)

                object.append(extract_clg_data(clg_name,clg_state,clg_city,clg_url,clg_address,clg_phn).__dict__)
                # print('yes')
    except Exception as ex:
        print(ex)

def Mumbai_clg_data():
    try:    
        # df = pd.read_csv('College_Data.csv')
        report_of_Mumbai_clg()
        dataframe = pd.DataFrame(object)
        # mumbai_df = df[df['City'] == 'Mumbai'].reset_index()
        return dataframe.to_csv('Mumbai_College_data.csv')
    except Exception as ex:
        print(ex)
    
def Delhi_clg_data():
    try:
        # df = pd.read_csv('College_Data.csv')
        report_of_Delhi_clg()
        dataframe = pd.DataFrame(object)
        # arr_=['Delhi','New Delhi']
        # df = df.loc[df['City'].isin(arr_)].reset_index()
        return dataframe.to_csv('Delhi_College_Data.csv')
    except Exception as ex:
        print(ex)

def Kalkatta_clg_data():
    try:
        report_of_kolkata_clg()
        dataframe = pd.DataFrame(object)
        # dataframe = dataframe[dataframe['City'] == 'kolkata']
        return dataframe.to_csv('Kolkata_College_Data.csv')
    except Exception as ex:
        print(ex)

def Chennai_clg_data():
    try:    
        report_of_Chennai_clg()
        dataframe = pd.DataFrame(object)
        # dataframe = dataframe[dataframe['City'] == 'Chennai']
        return dataframe.to_csv('Chennai_College_Data.csv')
    except Exception as ex:
        print(ex)
def State_cap_clg_data():
    try:
        df = pd.read_csv('College_Data.csv')
    # report_of_clg_data()
    # dataframe = pd.DataFrame(object)
        list_ = ['Bhopal','Chennai','New Delhi','Delhi','Port Blair','Dispur','Patna','Raipur','Daman','Ahmedabad','Shimla','Ranchi','Jammu','Bangalore','Trivandrum','Mumbai','Imphal','Shillong','Kohima','Bhubaneswar','Jaipur','Hyderabad','Agartala']
        df_1 = df.loc[df['City'].isin(list_)]
        df_2 =df[df["City"].isnull()]
        frame = [ df_1,df_2]
        new_df = pd.concat(frame).reset_index(drop=True)
        return new_df.to_csv('State_capital_College_Data.csv')
    except Exception as ex:
        print(ex)
def All_clg_data():
    try:
        df = pd.read_csv('College_Data.csv')
    # report_of_clg_data()
    # dataframe = pd.DataFrame(object)
        return df.to_csv('All_College_Data.csv')
    except Exception as ex:
        print(ex)
def scrap_clg_data():
    try:
        print('Enter 1 for tire 1 city = Mumbai, Delhi, Kolkata, Chennai')
        print('\n\nEnter 2 for : Capital of every state')
        print('\n\nEnter 3 for : Total city of every state')
        choice = int(input("\n\n Enter a number 1, 2, 3 here : "))
        print("You select number : " , choice)
        def view_clg_data(choice):
            if choice == 1:
                City = str(input("Enter City name as given: "))
                if City == 'Mumbai':
                    return Mumbai_clg_data()
                elif City == 'Delhi':
                    return Delhi_clg_data()
                elif City == 'Kolkata':
                    return Kalkatta_clg_data()
                elif City == 'Chennai':
                    return Chennai_clg_data()
                else:
                    print('select city as given enter 1')
            elif choice == 2:
                return State_cap_clg_data()
            elif choice == 3:
                return All_clg_data()
            else:
                print('Select from 1,2,3')
        view_clg_data(choice)
    except Exception as ex:
        print('input error', ex)
scrap_clg_data()
input('press any key to exit')