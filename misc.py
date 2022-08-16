from datetime import datetime, timedelta, date
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def FlattenList(list):
  flat_list = []
  for elemnts in list:
    for subElemnts in elemnts:
      flat_list.append(subElemnts)
  return flat_list

def RemoveAllStopwords(input):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(input)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence = []
  for w in word_tokens:
    if w not in stop_words:
      filtered_sentence.append(w)

  stringData = "" 
  for x in filtered_sentence:
    stringData += x
    stringData = stringData + " "

  return stringData



user = 'root2'
password = 'Mysql127'
host = '127.0.0.1'
port = 3306
database = 'presentation'

product_Name = ['Nothing Phone1','Oppo Reno8','Poco F4']
                
product_Xpath = ['//*[@id="container"]/div/div[3]/div/div[2]/div[6]/div[4]/div/a',
                     '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/a',
                     '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div[6]/div/a']
    
product_all_review_links = ["https://www.flipkart.com/nothing-phone-1-white-256-gb/product-reviews/itmeea53a564de47?pid=MOBGCYGPPQJTUNMZ&lid=LSTMOBGCYGPPQJTUNMZVFZZ6X&marketplace=FLIPKART",
                                "https://www.flipkart.com/oppo-reno8-5g-shimmer-black-128-gb/product-reviews/itmba1bc0bf67ccc?pid=MOBGFPE5BHY8QGEH&lid=LSTMOBGFPE5BHY8QGEHQDYOMR&marketplace=FLIPKART",
                                "https://www.flipkart.com/poco-f4-5g-night-black-128-gb/product-reviews/itmde7b4cceb0e93?pid=MOBGE853HXYJ7R9K&lid=LSTMOBGE853HXYJ7R9KBAM8S5&marketplace=FLIPKART"]


Master_loc_list = ['Patna', 'Bangalore', 'Chennai', 'Bengaluru', 'Jamshedpur',
       'Chalakudy', 'Mumbai', 'New Delhi', 'Vizianagaram', 'Bhatkal',
       'Barrackpore', 'Kadiri', 'Howrah', 'Jsw Steel Plant Township',
       'Indore', 'Rajkot', 'Chittoor', 'Nashik', 'Cuttack', 'Ghaziabad',
       'Puducherry', 'Vijayawada', 'Thiruvananthapuram', 'Hyderabad',
       'Vikarabad District', 'Gurugram', 'Bhavnagar', 'Bangalore Urban',
       'Lucknow', 'Gopalpur', 'Thanjavur', 'Uttar Dinajpur',
       'Bulandshahr', 'Palghar District', 'Vadakara', 'Bagalkot',
       'Bhopal', 'Navi Mumbai', 'Sirsa', 'Coimbatore', 'Ranchi',
       'Guwahati', 'Salem District', 'Puttur', 'Pulivendula',
       'Tiruchengode', 'Marampilly', 'Thodiyoor', 'Kakinada',
       'Pallippuram Alappuzha District',
       'South Twenty Four Parganas District', 'Shillong', 'Beri',
       'Ghatal', 'Vinukonda', 'Maharajganj', 'Ponnur', 'Chamarajanagar',
       'Davanagere', 'Madurai', 'Tarakeswar', 'Pondicherry', 'Jaipur',
       'Vidisha', 'Kharagpur', 'Perinthalmanna', 'Belsor', 'Angamaly',
       'Noida', 'Sidcul Haridwar', 'Vizianagaram District', 'Hosur',
       'Ramanagara District', 'Ludhiana', 'Vaniyambadi', 'Guntur',
       'Porbandar', 'Gautam Buddh Nagar', 'Nidadavole', 'Zirakpur',
       'Hanamkonda', 'Adilabad', 'Greater Noida', 'Tezpur', 'Baleshwar',
       'Hassan', 'Kasaragod', 'Thane', 'Ahmedabad', 'Anantapur District',
       'Krishnagiri', 'Rishra', 'Ranga Reddy', 'Dibrugarh',
       'Chittoor District', 'Visakhapatnam', 'Vellore', 'Dwarka',
       'Vadodara', 'Kalaburgi', 'Palakkad', 'Tinsukia', 'Sohna',
       'Rangareddy District', 'Tadepalli', 'Nivi', 'Jodhpur', 'Bellary',
       'Gonda', 'Raipur', 'West Godavari District', 'Raichur', 'Hubli',
       'Sri Ganganagar', 'Palamu District', 'Sagar District',
       'Srivilliputhur', 'Talegaon Dabhade', 'Naugachhia', 'Tumakuru',
       'Palakkad District', 'Mahalingpur', 'Muzaffarpur District',
       'Kuppam', 'Krishnagiri District', 'Kaliaganj', 'Thiruvallur',
       'Kapurthala', 'Udupi', 'Gangwa', 'Dakshina Kannada District',
       'Kota', 'Rohtak District', 'Bundi', 'Mathura', 'Sitamarhi',
       'Chandannagar', 'Bilaspur District', 'Pune', 'Bharuch',
       'Kasargode', 'Dumka', 'Jalandhar', 'Shrirampur', 'Sira', 'Dhone',
       'Ballari', 'Tirupati', 'Trivandrum', 'Patiala', 'Sivakasi',
       'Siddipet', 'Saran District', 'Yemmiganur', 'Hisar',
       'Mayiladuthurai', 'Kalyan', 'Bolpur', 'Koduvally',
       'Papparapatti Dharmapuri District', 'Vikramasingapuram',
       'Sholapur', 'Coimbatore District', 'Yelamanchili',
       'Sonitpur District', 'Bhimavaram', 'Yadadri District',
       'Secunderabad', 'Kopargaon', 'Hingoli', 'Burdwan', 'Bidar',
       'Phulabani', 'Thrissur', 'Kulti', 'Gundlupet', 'Mangalore',
       'Dakshina Kannada', 'Sao Jose De Areal', 'Lalganj', 'Nalgonda',
       'Malkangiri', 'Bhuj', 'Kollam', 'Rourkela', 'Bilaspur', 'Khammam',
       'Sonipat', 'Gangarampur', 'Port Blair', 'Dibrugarh District',
       'Bhubaneswar', 'Thoothukkudi District', 'Kamrup Metropolitan.',
       'Sangareddy', 'Dhanbad', 'Makronia Buzurg', 'Uthangarai', 'Kochi',
       'Gurgaon', 'Mahbubnagar', 'Gorakhpur', 'Kolkata', 'Meerut',
       'Saraipali', 'Kavali', 'Baluhati', 'Bhilwara', 'Hussainabad',
       'Bhind']

top10 = ['Bengaluru','Hyderabad','Chennai','New Delhi','Mumbai', 'Ahmedabad','Ghaziabad','Lucknow','Patna','Coimbatore']

Others = []
  #64.52%
for element in Master_loc_list:
  if element not in top10:
    Others.append(element)

def get_location_dict():
  location_percnt_dict = {'Bengaluru' : 11.67,             
                'Hyderabad' : 5.71,
                'Chennai' : 5.24,
                'New Delhi' :4.29,
                'Mumbai' : 1.90, 
                'Ahmedabad': 1.67,
                'Ghaziabad' : 1.67,
                'Lucknow' : 1.19,
                'Patna' : 1.19,
                'Coimbatore' : 0.95 }
  return location_percnt_dict



def getDate(data):

    if data == 'Today':
        temp_int = 1
    else:
        temp_int = int(data[:-9])
    
    now = datetime.now()
    N = temp_int
    date_N_days_ago = now - timedelta(days=N)
    finalData = date_N_days_ago.strftime("%d/%m/%Y")

    return finalData

def getOrderDate(data):
    
    intData = int(data[:-9])
    now = datetime.now()
    N = intData
    date_N_days_ago = now - timedelta(days=N+6)
    finalData = date_N_days_ago.strftime("%d/%m/%Y")

    return finalData


Nothing_1stWeek = {'12-07-2022': 0.23,
          '13-07-2022': 0.16,
          '14-07-2022': 0.14,
          '15-07-2022': 0.10,
          '16-07-2022': 0.07,
          '17-07-2022':0.05 }

Oppo_1stWeek = {'25-07-2022': 0.23,
          '26-07-2022': 0.16,
          '27-07-2022': 0.14,
          '28-07-2022': 0.10,
          '29-07-2022': 0.07,
          '30-07-2022':0.05 }

PocoF4_1stWeek = {'27-06-2022': 0.23,
          '28-06-2022': 0.16,
          '29-06-2022': 0.14,
          '30-06-2022': 0.10,
          '01-07-2022': 0.07,
          '02-07-2022':0.05 }

def dummy_dates_list_generator(d0):
  temp = []
  d1 = date.today()
  delta = d1 - d0
  delta = delta.days

  base = datetime.today()
  date_list = []
  for x in range(delta):
    temp = base - timedelta(days = x)
    temp = temp.date().strftime('%Y-%m-%d')
    date_list.append(temp)

  return date_list

Nothing_d0 = date(2022,7,17)
Oppo_d0 = date(2022,7,30)
Poco_d0 = date(2022,7,2)

Nothing_other_dates = dummy_dates_list_generator(Nothing_d0)
Oppo_other_dates = dummy_dates_list_generator(Oppo_d0)
Poco_other_dates = dummy_dates_list_generator(Poco_d0)


def dateGenerator(class_countx,newDate,Newpercnt):
    class_count = int(class_countx*Newpercnt)
    class_list = []

    for element in range(class_count):
        class_list.append(newDate)

    return class_list
