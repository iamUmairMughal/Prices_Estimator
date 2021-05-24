from .apps import model_reg
import numpy as np


def predict_price(values):

    km_driven = values.get('km_driven')
    year = values.get('year')
    brand_name = values.get('brand_name')
    model_name = values.get('model_name')
    condition_name = values.get('condition')
    fuel_name = values.get('fuel_type')
    city_name = values.get('city_name')
    transaction_name = values.get('transaction_type')


    brands_columns = ['Brand_BMW', 'Brand_Changan', 'Brand_Chevrolet', 'Brand_Classic & Antiques', 'Brand_Daewoo', 'Brand_Daihatsu', 'Brand_FAW', 'Brand_Honda', 'Brand_Hyundai', 'Brand_KIA', 'Brand_Land Rover', 'Brand_Lexus', 'Brand_Mazda', 'Brand_Mercedes', 'Brand_Mitsubishi', 'Brand_Nissan', 'Brand_Other Brands', 'Brand_Porsche', 'Brand_Range Rover', 'Brand_Subaru', 'Brand_Suzuki', 'Brand_Toyota', 'Brand_Audi']
    city_columns = ['Registered City_Ali Masjid', 'Registered City_Askoley', 'Registered City_Attock', 'Registered City_Badin', 'Registered City_Bagh', 'Registered City_Bahawalnagar', 'Registered City_Bahawalpur', 'Registered City_Bela', 'Registered City_Bhimber', 'Registered City_Chilas', 'Registered City_Chiniot', 'Registered City_Chitral', 'Registered City_Dera Ghazi Khan', 'Registered City_Dera Ismail Khan', 'Registered City_Faisalabad', 'Registered City_Gujranwala', 'Registered City_Gujrat', 'Registered City_Haripur', 'Registered City_Hyderabad', 'Registered City_Islamabad', 'Registered City_Jhelum', 'Registered City_Kandhura', 'Registered City_Karachi', 'Registered City_Karak', 'Registered City_Kasur', 'Registered City_Khairpur', 'Registered City_Khanewal', 'Registered City_Khanpur', 'Registered City_Khaplu', 'Registered City_Khushab', 'Registered City_Kohat', 'Registered City_Lahore', 'Registered City_Larkana', 'Registered City_Lasbela', 'Registered City_Mandi Bahauddin', 'Registered City_Mardan', 'Registered City_Mirpur', 'Registered City_Multan', 'Registered City_Muzaffarabad', 'Registered City_Muzaffargarh', 'Registered City_Nawabshah', 'Registered City_Nowshera', 'Registered City_Okara', 'Registered City_Pakpattan', 'Registered City_Peshawar', 'Registered City_Quetta', 'Registered City_Rahimyar Khan', 'Registered City_Rawalpindi', 'Registered City_Sahiwal', 'Registered City_Sargodha', 'Registered City_Sheikh�pura', 'Registered City_Sialkot', 'Registered City_Sukkar', 'Registered City_Sukkur', 'Registered City_Swabi', 'Registered City_Tank', 'Registered City_Vehari', 'Registered City_Wah', 'Registered City_unknown']
    transaction_columns = ['Transaction Type_Installment/Leasing',	'Transaction Type_Cash']
    models_columns = ['Model_2 Series', 'Model_200 D', 'Model_240 Gd', 'Model_250 D', 'Model_3 Series', 'Model_323', 'Model_350Z', 'Model_5 Series', 'Model_6 Series', 'Model_626', 'Model_7 Series', 'Model_808', 'Model_86', 'Model_929', 'Model_A Class', 'Model_A1', 'Model_A3', 'Model_A5', 'Model_AD Van', 'Model_APV', 'Model_Accent', 'Model_Accord', 'Model_Acty', 'Model_Acura', 'Model_Airwave', 'Model_Allion', 'Model_Alphard Hybrid', 'Model_Alto', 'Model_Alto Lapin', 'Model_Aqua', 'Model_Atrai Wagon', 'Model_Auris', 'Model_Avanza', 'Model_Axela', 'Model_Aygo', 'Model_Azwagon', 'Model_B B', 'Model_B2200', 'Model_BR-V', 'Model_Baleno', 'Model_Beat', 'Model_Bego', 'Model_Belta', 'Model_Blue Bird', 'Model_Bluebird Sylphy', 'Model_Bolan', 'Model_Boon', 'Model_C Class', 'Model_C-HR', 'Model_CR-V', 'Model_CR-Z', 'Model_CT200h', 'Model_Cami', 'Model_Camry', 'Model_Cappuccino', 'Model_Carisma', 'Model_Carol', 'Model_Carol Eco', 'Model_Carrier', 'Model_Carry', 'Model_Cast', 'Model_Cayenne', 'Model_Celica', 'Model_Cervo', 'Model_Charade', 'Model_Charmant', 'Model_Chitral', 'Model_Ciaz', 'Model_Cielo', 'Model_City Aspire', 'Model_City IDSI', 'Model_City IVTEC', 'Model_City Vario', 'Model_Civic EXi', 'Model_Civic Hybrid', 'Model_Civic Prosmetic', 'Model_Civic VTi', 'Model_Civic VTi Oriel', 'Model_Civic VTi Oriel Prosmatec', 'Model_Classic', 'Model_Clipper', 'Model_Coaster', 'Model_Colt', 'Model_Copen', 'Model_Corolla 2.0 D', 'Model_Corolla Assista', 'Model_Corolla Axio', 'Model_Corolla Fielder', 'Model_Corolla GLI', 'Model_Corolla XE', 'Model_Corolla XLI', 'Model_Corona', 'Model_Corrolla Altis', 'Model_Cressida', 'Model_Cross Road', 'Model_Crown', 'Model_Cruze', 'Model_Cultus VX', 'Model_Cultus VXL', 'Model_Cultus VXR', 'Model_Cuore', 'Model_D Series', 'Model_Dayz', 'Model_Dayz Highway Star', 'Model_Demio', 'Model_Duet', 'Model_E Class', 'Model_EK Custom', 'Model_EK Space Custom', 'Model_Echo', 'Model_Ek Sport', 'Model_Ek Wagon', 'Model_Elantra', 'Model_Escudo', 'Model_Esse', 'Model_Estima', 'Model_Every', 'Model_Every Wagon', 'Model_Excel', 'Model_Exclusive', 'Model_FX', 'Model_Familia Van', 'Model_Figaro', 'Model_Fit', 'Model_Fj Cruiser', 'Model_Flair', 'Model_Flair Wagon', 'Model_Fortuner', 'Model_Freed', 'Model_Galant', 'Model_Gilgit', 'Model_Grace Hybrid', 'Model_Gran', 'Model_Gx Series', 'Model_Harrier', 'Model_Hiace', 'Model_Hijet', 'Model_Hilux', 'Model_Hustler', 'Model_I', 'Model_I Mivec', 'Model_ISIS', 'Model_IST', 'Model_Ignis', 'Model_Infinity', 'Model_Insight', 'Model_Is Series', 'Model_Jade Hybrid', 'Model_Jimny', 'Model_Jimny Sierra', 'Model_Joy', 'Model_Juke', 'Model_Kalam', 'Model_Kei', 'Model_Khyber', 'Model_Kix', 'Model_Kizashi', 'Model_L200', 'Model_L300', 'Model_Lancer', 'Model_Lancer Evolution', 'Model_Land Cruiser', 'Model_Liana', 'Model_Life', 'Model_Lite Ace', 'Model_Luce', 'Model_Lucida', 'Model_MR Wagon', 'Model_March', 'Model_Margalla', 'Model_Mark II', 'Model_Mark X', 'Model_Matiz', 'Model_Mega Carry Xtra', 'Model_Mehran VX', 'Model_Mehran VXR', 'Model_Minica', 'Model_Minicab Bravo', 'Model_Mira', 'Model_Mira Cocoa', 'Model_Mirage', 'Model_Moco', 'Model_Move', 'Model_Murrano', 'Model_N Box', 'Model_N One', 'Model_N Wgn', 'Model_Noah', 'Model_Note', 'Model_Optra', 'Model_Other', 'Model_Otti', 'Model_Pajero', 'Model_Pajero Mini', 'Model_Palette', 'Model_Palette Sw', 'Model_Passo', 'Model_Patrol', 'Model_Pickup', 'Model_Pino', 'Model_Pixis Epoch', 'Model_Platz', 'Model_Porte', 'Model_Potohar', 'Model_Prado', 'Model_Premio', 'Model_President', 'Model_Pride', 'Model_Prius', 'Model_Prius Alpha', 'Model_Probox', 'Model_Pulsar', 'Model_Qashqai', 'Model_RX Series', 'Model_RX8', 'Model_Racer', 'Model_Ractis', 'Model_Raum', 'Model_Rav4', 'Model_Ravi', 'Model_Rocky', 'Model_Roox', 'Model_Rush', 'Model_Rvr', 'Model_S Class', 'Model_S660', 'Model_Safari', 'Model_Santro', 'Model_Scrum', 'Model_Scrum Wagon', 'Model_Sera', 'Model_Shehzore', 'Model_Shogun', 'Model_Silverado', 'Model_Sirion', 'Model_Sirius', 'Model_Smart', 'Model_Solio', 'Model_Sonata', 'Model_Sonica', 'Model_Spacia', 'Model_Spark', 'Model_Spectra', 'Model_Spike', 'Model_Sportage', 'Model_Sprinter', 'Model_Starlet', 'Model_Stream', 'Model_Succeed', 'Model_Sunny', 'Model_Supra', 'Model_Surf', 'Model_Swift', 'Model_Sx4', 'Model_Sylphy', 'Model_Tanto', 'Model_Terios Kid', 'Model_Thats', 'Model_Tiida', 'Model_Toppo', 'Model_Town Ace', 'Model_Toyo Ace', 'Model_V2', 'Model_Vamos', 'Model_Van', 'Model_Vanette', 'Model_Verossa', 'Model_Vezel', 'Model_Vitara', 'Model_Vitz', 'Model_Vogue', 'Model_Wagon R', 'Model_Wagon R Stingray', 'Model_Wake', 'Model_Wingroad', 'Model_Wish', 'Model_X Trail', 'Model_X-PV', 'Model_Yaris', 'Model_Zest', 'Model_Zest Spark', 'Model_cars-other-23', 'Model_cars-other-37', 'Model_cars-other-5', 'Model_cars-other-7', 'Model_cars-suzuki-86', 'Model_iQ', 'Model_unknown',]
    fuel_columns =['Fuel_Diesel', 'Fuel_Hybrid', 'Fuel_LPG', 'Fuel_Petrol', 'Fuel_CNG']
    condition_columns = ['Condition_Used']

    damaged = 0

    brand = [0]*len(brands_columns)
    condition = [0]*len(condition_columns)
    fuel = [0]*len(fuel_columns)
    city = [0]*len(city_columns)
    model = [0]*len(models_columns)
    transaction = [0]*len(transaction_columns)

    brand[brands_columns.index('Brand_'+str(brand_name))] = 1
    model[models_columns.index('Model_'+str(model_name))] = 1
    city[city_columns.index('Registered City_'+str(city_name))] = 1
    fuel[fuel_columns.index('Fuel_'+str(fuel_name))] = 1
    condition[condition_columns.index('Condition_'+str(condition_name))] = 1
    transaction[transaction_columns.index('Transaction Type_'+str(transaction_name))] = 1

    if km_driven > 2000000:
        damaged = 1

    data = [km_driven, year]

    for b in brand:
        data.append(b)
    for c in condition:
        data.append(c)
    for f in fuel:
        data.append(f)
    for m in model:
        data.append(m)
    for c in city:
        data.append(c)
    for t in transaction:
        data.append(c)
    data.append(damaged)

    data = np.array(data).reshape(1, len(data)).astype('float64')
    y_pred = model_reg.predict(data)


    return round(y_pred[0], 1)


# values = {'km_driven': 85000,
# 'year' : 2015,
# 'brand_name' : 'Audi',
# 'model_name' : 'Other',
# 'condition' : 'Used',
# 'fuel_type' : 'Petrol',
# 'city_name' : 'Karachi',
# 'transaction_type' : 'Cash'}
#
# result = predict_price(values)
#
# print(result)
