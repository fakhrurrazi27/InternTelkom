# Import Library
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pyts

# Confiigure CORS and Create FastAPI Object
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#model
model1 = pickle.load(open('model_baru_fix.p', 'rb'))
model2 = pickle.load(open('model_3.p', 'rb'))

#Encode Class
channel_class = pickle.load(open('channel_fix.p','rb'))
late_class = pickle.load(open('late_fix.p','rb'))
paket_class = pickle.load(open('paket(fix).p','rb'))

class Gladius(BaseModel):
    billing_2_amountTotal : str 
    billing_3_amountTotal :str 
    billing_4_amountTotal : str
    billing_5_amountTotal : str
    billing_6_amountTotal : str 
    billing_7_amountTotal : str
    billing_8_amountTotal : str
    billing_9_amountTotal : str
    billing_10_amountTotal : str
    billing_11_amountTotal : str
    billing_2_channel : str
    billing_3_channel : str
    billing_4_channel : str
    billing_5_channel : str
    billing_6_channel : str
    billing_7_channel : str
    billing_8_channel : str
    billing_9_channel : str
    billing_10_channel : str
    billing_11_channel : str
    billing_2_paymentDate : float
    billing_3_paymentDate : float
    billing_4_paymentDate : float
    billing_5_paymentDate : float
    billing_6_paymentDate : float
    billing_7_paymentDate : float
    billing_8_paymentDate : float
    billing_9_paymentDate : float
    billing_10_paymentDate : float
    billing_11_paymentDate : float
    gladius_paketradius : str
    usage : float

#function for encoding
def encode_channel(x):
    return channel_class.index(x)
def encode_late(x):
    return late_class.index(late(x))
def encode_paket(x):
    return paket_class.index(x)

#function for amount
def amount(x):
    return float(str(x).replace(".", "").replace(",", "."))

#function for feature
def paymentDate(x):
    return int(x)

def paymentDay(x):
    return int(str(paymentDate(x))[-2:])

#month late:
def late(x):
    if paymentDay(x) == 0:
        return 'UNPAID'
    elif (paymentDay(x) >= 1) & (paymentDay(x) < 21):
        return 'PAID'
    else:
        return 'LATE PAID'

@app.get('/predict')
def predict(data: Gladius):
    arr = [amount(data.billing_2_amountTotal),
       amount(data.billing_3_amountTotal),
       amount(data.billing_4_amountTotal),
       amount(data.billing_5_amountTotal),
       amount(data.billing_6_amountTotal),
       amount(data.billing_7_amountTotal),
       amount(data.billing_8_amountTotal),
       amount(data.billing_9_amountTotal),
       amount(data.billing_10_amountTotal),
       amount(data.billing_11_amountTotal),
       encode_channel(data.billing_2_channel),
       encode_channel(data.billing_3_channel),
       encode_channel(data.billing_4_channel),
       encode_channel(data.billing_5_channel),
       encode_channel(data.billing_6_channel),
       encode_channel(data.billing_7_channel),
       encode_channel(data.billing_8_channel),
       encode_channel(data.billing_9_channel),
       encode_channel(data.billing_10_channel),
       encode_channel(data.billing_11_channel),
       paymentDay(data.billing_2_paymentDate),
       paymentDay(data.billing_3_paymentDate),
       paymentDay(data.billing_4_paymentDate),
       paymentDay(data.billing_5_paymentDate),
       paymentDay(data.billing_6_paymentDate),
       paymentDay(data.billing_7_paymentDate),
       paymentDay(data.billing_8_paymentDate),
       paymentDay(data.billing_9_paymentDate),
       paymentDay(data.billing_10_paymentDate),
       paymentDay(data.billing_11_paymentDate),
       encode_late(data.billing_2_paymentDate),
       encode_late(data.billing_3_paymentDate),
       encode_late(data.billing_4_paymentDate),
       encode_late(data.billing_5_paymentDate),
       encode_late(data.billing_6_paymentDate),
       encode_late(data.billing_7_paymentDate),
       encode_late(data.billing_8_paymentDate),
       encode_late(data.billing_9_paymentDate),
       encode_late(data.billing_10_paymentDate),
       encode_late(data.billing_11_paymentDate),
       encode_paket(data.gladius_paketradius),
       data.usage
       ]
    print([arr])
    print(model2.n_features_in_)
    result1 = model1.predict_proba([arr])
    result2 = model2.predict_proba([arr])
# model 1 : [0 1 2] = ['LATE PAID', 'PAID', 'UNPAID']
#model 2 : [0 1 2] = ['LATE PAID', 'PAID', 'UNPAID']
    return {"Model 1" : {
                            "Bayar Tepat Waktu" : result1[0][1] *100,
                            "Telat Bayar" : result1[0][0] *100,
                            "Tidak Bayar" : result1[0][2] *100
                        },

            "Model 2" : {
                            "Bayar Tepat Waktu" : result2[0][1] *100,
                            "Telat Bayar" : result2[0][0] *100
                         }
            }