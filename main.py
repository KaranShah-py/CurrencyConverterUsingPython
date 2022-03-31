# Modules imported
from tkinter import *
from tkinter.font import *
import json 
import requests

# Basic window
root = Tk()
root.title('Currency Calculator')
root.geometry('1200x600')
root.minsize(width=1200, height=600)
root.maxsize(width=1200, height=600)
root.config(bg='#242424')

country_options = [
    'India (INR)', 'UAE (AED)', 'Afghanistan (AFN)', 'Albania (ALL)', 'Armenia (AMD)', 'Angola (AOA)', 'Argentina (ARS)', 'Australia (AUD)', 'Aruba (AWG)', 
    'Barbados (BBD)', 'Bangladesh (BDT)', 'Bulgaria (BGN)', 'Burundi (BIF)', 'Bermuda (BMD)', 'Brunei Darussalam (BND)', 'Bolivia (BOB)', 
    'Bahrain (BRL)', 'Bahamas (BSD)', 'Bhutan (BTN)', 'Canada (CAD)', 'China (CNY)', 'Colombia (COP)', 'Costa Rica (CRC)', 'Cuba (CUP)', 'Cape Verde (CVE)', 'Czech Republic (CZK)',
    'Algeria (DZD)', 'Egypt (EGP)', 'Eritrea (ERN)', 'Ethiopia (ETB)', 'Austria (EUR)', 'Fiji (FJD)', 'Falkland Islands (FKP)', 'Great Britain (GBP)', 'Georgia (GEL)',
    'Ghana (GHS)', 'Gibraltar (GIP)', 'Gambia (GMD)', 'Guinea (GNF)', 'Guatemala (GTQ)', 'Guyana (GYD)', 'Hong Kong (HKD)', 'Honduras (HNL)', 'Croatia (HRK)', 
    'Haiti (HTG)', 'Hungary (HUF)', 'Indonesia (IDR)', 'Israel (ILS)', 'IMP', 'Iraq (IQD)', 'Iran (IRR)', 'Iceland (ISK)', 'Jamaica (JMD)', 'Jordan (JOD)', 
    'Japan (JPY)', 'Kenya (KES)', 'Kyrgyzstan (KGS)', 'Cambodia (KHR)', 'South Korea (KRW)', 'Kuwait (KWD)', 'Cayman Islands (KYD)', 'Kazakhstan(KZT)', 
    'Laos (LAK)', 'Lebanon (LBP)', 'Sri Lanka (LKR)', 'Liberia (LRD)', 'Lesotho (LSL)', 'Libya (LYD)', 'Morocco (MAD)', 'Moldova (MDL)', 'Madagascar (MGA)', 'Macedonia (MKD)', 
    'Myanmar Burma (MMK)', 'Mongolia (MNT)', 'Macao (MOP)', 'Mauritania (MRU)', 'Mauritius (MUR)', 'Maldives (MVR)', 'Malawi (MWK)', 'Mexico (MXN)', 'Malaysia (MYR)', 'Mozambique (MZN)', 
    'Namibia (NAD)', 'Nigeria (NGN)', 'Nicaragua (NIO)', 'Norway (NOK)', 'Nepal (NPR)', 'New Zealand (NZD)', 'Oman (OMR)', 'Panama (PAB)', 'Peru (PEN)', 'Papua New Guinea (PGK)', 
    'Philippines (PHP)', 'Pakistan (PKR)', 'Poland (PLN)', 'Paraguay (PYG)', 'Qatar (QAR)', 'Serbia (RSD)', 'Russia (RUB)', 'Rwanda (RWF)', 'Saudi Arabia (SAR)', 
    'Solomon Islands (SBD)', 'Seychelles (SCR)', 'Sudan (SDG)', 'Sweden (SEK)', 'Singapore (SGD)', 'Ascension Island (SHP)', 'Sierra Leone (SLL)', 'Somalia (SOS)', 'Suriname (SRD)', 
    'Sao Tome and Principe (STN)', 'Syria (SYP)', 'Swaziland (SZL)', 'Thailand (THB)', 'Tajikistan (TJS)', 'Turkmenistan (TMT)', 'Tunisia (TND)', 'Tonga (TOP)', 'Turkey (TRY)', 'Trinidad and Tobago (TTD)', 
    'Taiwan (TWD)', 'Tanzania (TZS)', 'Ukraine (UAH)', 'Uganda (UGX)', 'United States of America (USD)', 'Uruguay (UYU)', 'Uzbekistan (UZS)', 'Vietnam (VND)', 
    'Samoa (WST)', 'Central African Republic (XAF)', 'Anguilla (XCD)', 'New Caledonia (XPF)', 'South Africa (ZAR)', 'Zambia (ZMW)'
]

global selected_fr_country
selected_fr_country = StringVar()
selected_fr_country.set(country_options[0]) 

global selected_to_country
selected_to_country = StringVar()
selected_to_country.set(country_options[1])

# Funtions
def convertion():
    if entry_box1.get() == '':
        entry_box1.insert(0, 1)    
    variable1 = currency_name(selected_fr_country.get())
    variable2 = currency_name(selected_to_country.get())
    ulr = 'https://v6.exchangerate-api.com/v6/ADD_YOUR_API_KEY_HERE/latest/' + variable1
    r = requests.get(ulr)
    data = json.loads(r.content)
    result = data['conversion_rates'][variable2]
    if entry_box1.get() == 1:
        entry_box2.config(state=NORMAL)
        entry_box2.insert(0,result)
    else:
        variable3 = int(entry_box1.get()) * result
        entry_box2.config(state=NORMAL)
        entry_box2.insert(0,variable3)

def currency_name(var):
    i = 0
    for i in range(0, len(var)):
        if var[i] == '(':
            j = i+1
        elif var[i] == ')':
            k = i
        else:
            pass
    new_var = var[j:k]
    return new_var


def clear():
    entry_box1.delete(0,END)
    entry_box2.delete(0,END)
    entry_box2.config(state='readonly')

# Defining widgets
title_label = Label(root, text='CURRENCY CONVERTER', font=('Helvetica', 30, BOLD, ITALIC), bg='#363636', fg='Black', borderwidth=0, relief=GROOVE)

ent__amount = Label(root, text='ENTER AMOUNT', font=('Helvetica', 20, BOLD, ITALIC), bg='#363636', fg='Black', borderwidth=0, relief=GROOVE, padx=10)
entry_box1 = Entry(root, bg='#363636', fg='White', width=10, borderwidth=0, relief=GROOVE, font=('Helvetic', 20, ITALIC), justify=CENTER)

fr_co_label = Label(root, text='FROM COUNTRY', font=('Helvetica', 20, BOLD, ITALIC), bg='#363636', fg='Black', borderwidth=0, relief=GROOVE, padx=10)
to_co_label = Label(root, text='TO COUNTRY', font=('Helvetica', 20, BOLD, ITALIC), bg='#363636', fg='Black', borderwidth=0, relief=GROOVE, padx=32)

fr_co_opts = OptionMenu(root, selected_fr_country, *country_options)
to_co_opts = OptionMenu(root, selected_to_country, *country_options)

con_button = Button(root, text='CONVERT', font=('Helvetica', 20, BOLD), bg='#363636', fg='Black', activebackground='#3D3D3D', activeforeground='White', borderwidth=0, relief=GROOVE, padx=20, pady=20, command=convertion)
cle_button = Button(root, text=' CLEAR ', font=('Helvetica', 20, BOLD), bg='#363636', fg='Black', activebackground='#3D3D3D', activeforeground='White', borderwidth=0, relief=GROOVE, padx=20, pady=20, command=clear)

cur__amount = Label(root, text='CURRENT RATE', font=('Helvetica', 20, BOLD, ITALIC), bg='#363636', fg='Black', borderwidth=0, relief=GROOVE, padx=10)
entry_box2 = Entry(root, bg='#363636', fg='White', width=10, borderwidth=0, relief=GROOVE, font=('Helvetic', 20, ITALIC), justify=CENTER, state="readonly", readonlybackground='#363636')

# Putting them on the screen
title_label.place(x=400, y=20)

ent__amount.place(x=400, y=100)
entry_box1.place(x=700, y=100)

fr_co_label.place(x=400, y=150)
fr_co_opts.place(x=700, y=152)

to_co_label.place(x=400, y=200)
to_co_opts.place(x=700, y=202)

cur__amount.place(x=400, y=250)
entry_box2.place(x=700, y=252)

con_button.place(x=50, y=450)
cle_button.place(x=1000, y=450)


# mainloop
root.mainloop()
