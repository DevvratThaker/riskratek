# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:22:55 2021

@author: GI0231
"""


from flask import Flask, request, render_template
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        KGI_District_WOE=request.form['KGI_District_WOE']
        if(KGI_District_WOE=='Cluster4'):
            Cluster4 = 1
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0
            
                      
            
        elif(KGI_District_WOE=='Cluster6'):
            Cluster4 = 0
            Cluster6 = 1
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0 
            
        elif(KGI_District_WOE=='Cluster1'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 1
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0 
            
        elif(KGI_District_WOE=='Cluster7'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 1
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0
            
        elif(KGI_District_WOE=='Cluster8'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 1
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0
            
        elif(KGI_District_WOE=='Cluster5'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 1
            Cluster2 = 0
            Cluster3 = 0 
            
        elif(KGI_District_WOE=='Cluster2'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 1
            Cluster3 = 0
            
        elif(KGI_District_WOE=='Cluster3'):
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 1 
            
        else:
            Cluster4 = 0
            Cluster6 = 0
            Cluster1 = 0
            Cluster7 = 0
            Cluster8 = 0
            Cluster5 = 0
            Cluster2 = 0
            Cluster3 = 0 
            
        Banca_Non_Banca_Rev = request.form["Banca_Non_Banca_Rev"]
        if (Banca_Non_Banca_Rev=='Digital'):
            Digital = 1
            BancaOEM = 0
            NonBancaOEMDigital = 0
            OEM = 0

        elif(Banca_Non_Banca_Rev=='BancaOEM'):
            Digital = 0
            BancaOEM = 1
            NonBancaOEMDigital = 0
            OEM = 0
            
        elif(Banca_Non_Banca_Rev=='NonBancaOEMDigital'):
            Digital = 0
            BancaOEM = 0
            NonBancaOEMDigital = 1
            OEM = 0
            
        elif(Banca_Non_Banca_Rev=='OEM'):
            Digital = 0
            BancaOEM = 0
            NonBancaOEMDigital = 0
            OEM = 1
            
        else:
            Digital = 0
            BancaOEM = 0
            NonBancaOEMDigital = 0
            OEM = 0
            
        New_Renewal_Rollover1 = request.form["New_Renewal_Rollover1"]
        if(New_Renewal_Rollover1=='FreshRol'):
            FreshRol = 1
            Renewal = 0
            FreshNew = 0
        elif(New_Renewal_Rollover1=='Renewal'):
            FreshRol = 0
            Renewal = 1
            FreshNew = 0
        elif(New_Renewal_Rollover1=='Freshnew'):
            FreshRol = 0
            Renewal = 0
            FreshNew = 1
        
        else:
            FreshRol = 0
            Renewal = 0
            FreshNew = 0
            
        NCB1 = request.form["NCB1"]
        if(NCB1==twenty):
            twenty = 1
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==zero):
            twenty = 0
            zero = 1
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==twentyfive):
            twenty = 0
            zero = 0
            twentyfive = 1
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==fifty):
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 1
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==thirtyfive):
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 1
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==fortyfive):
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 1
            New = 0
            Greaterthen55 = 0
            
        elif(NCB1==New):
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 1
            Greaterthen55 = 0
            
        elif(NCB1==Greaterthen55):
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 1
            
        else:
            twenty = 0
            zero = 0
            twentyfive = 0
            fifty = 0
            thirtyfive = 0
            fortyfive = 0
            New = 0
            Greaterthen55 = 0
            
        Break_In_Band = request.form["Break_In_Band"]
        if(Break_In_Band=='NoBreakIn'):
            NoBreakIn = 1
            BreakIn90pdays = 0
            BreakIn90mdays = 0
            NoPIP = 0
        elif(Break_In_Band=='BreakIn90pdays'):
            NoBreakIn = 0
            BreakIn90pdays = 1
            BreakIn90mdays = 0
            NoPIP = 0
        elif(Break_In_Band=='BreakIn90mdays'):
            NoBreakIn = 0
            BreakIn90pdays = 0
            BreakIn90mdays = 1
            NoPIP = 0
        elif(Break_In_Band=='NoPIP'):
            NoBreakIn = 0
            BreakIn90pdays = 0
            BreakIn90mdays = 0
            NoPIP = 1
        else:
            NoBreakIn = 0
            BreakIn90pdays = 0
            BreakIn90mdays = 0
            NoPIP = 0
            
        Credit_Score_Band = request.form["Credit_Score_Band"]
        if(Credit_Score_Band=='NoCreditScore'):
            NoCreditScore = 1
            CSLessthen700 = 0
            CSGreaterthen700 = 0
        elif(Credit_Score_Band=='CSLessthen700'):
            NoCreditScore = 0
            CSLessthen700 = 1
            CSGreaterthen700 = 0
        elif(Credit_Score_Band=='CSGreaterthen700'):
            NoCreditScore = 0
            CSLessthen700 = 0
            CSGreaterthen700 = 1
        else:
            NoCreditScore = 0
            CSLessthen700 = 0
            CSGreaterthen700 = 0
            
        VA_Group = request.form["VA_Group"]
        if(VA_Group=='VA1to2pt99'):
            VA1to2pt99 = 1
            VA5to6pt99 = 0
            VA3to4pt99 = 0
            VA7to9pt99 = 0
            VA0to0pt99 = 0
            VAGreaterthen10 = 0
        elif(VA_Group=='VA5to6pt99'):
            VA1to2pt99 = 0
            VA5to6pt99 = 1
            VA3to4pt99 = 0
            VA7to9pt99 = 0
            VA0to0pt99 = 0
            VAGreaterthen10 = 0
        elif(VA_Group=='VA3to4pt99'):
            VA1to2pt99 = 0
            VA5to6pt99 = 0
            VA3to4pt99 = 1
            VA7to9pt99 = 0
            VA0to0pt99 = 0
            VAGreaterthen10 = 0
        elif(VA_Group=='VA7to9pt99'):
            VA1to2pt99 = 0
            VA5to6pt99 = 0
            VA3to4pt99 = 0
            VA7to9pt99 = 1
            VA0to0pt99 = 0
            VAGreaterthen10 = 0
        elif(VA_Group=='VA0to0pt99'):
            VA1to2pt99 = 0
            VA5to6pt99 = 0
            VA3to4pt99 = 0
            VA7to9pt99 = 0
            VA0to0pt99 = 1
            VAGreaterthen10 = 0
        elif(VA_Group=='VAGreaterthen10'):
            VA1to2pt99 = 0
            VA5to6pt99 = 0
            VA3to4pt99 = 0
            VA7to9pt99 = 0
            VA0to0pt99 = 0
            VAGreaterthen10 = 1
        else:
            VA1to2pt99 = 0
            VA5to6pt99 = 0
            VA3to4pt99 = 0
            VA7to9pt99 = 0
            VA0to0pt99 = 0
            VAGreaterthen10 = 0
    
        FuelType = request.form["FuelType"]
        if(FuelType=='Petrol'):
            Petrol = 1
            Diesel = 0
            Others = 0
            CNG = 0
        elif(FuelType=='Diesel'):
            Petrol = 0
            Diesel = 1
            Others = 0
            CNG = 0
        elif(FuelType=='Others'):
            Petrol = 0
            Diesel = 0
            Others = 1
            CNG = 0
        elif(FuelType=='CNG'):
            Petrol = 0
            Diesel = 0
            Others = 0
            CNG = 1
        else:
            Petrol = 0
            Diesel = 0
            Others = 0
            CNG = 0
            
        AddOn_Description = request.form["AddOn_Description"]
        if(AddOn_Description=='NilDepwithotherAddOn'):
            NilDepwithotherAddOn = 1
            TariffPackage = 0
            OtherAddOnwithoutNilDep = 0
            Standalone = 0
        elif(AddOn_Description=='TariffPackage'):
            NilDepwithotherAddOn = 0
            TariffPackage = 1
            OtherAddOnwithoutNilDep = 0
            Standalone = 0
        elif(AddOn_Description=='OtherAddOnwithoutNilDep'):
            NilDepwithotherAddOn = 0
            TariffPackage = 0
            OtherAddOnwithoutNilDep = 1
            Standalone = 0
        elif(AddOn_Description=='Standalone'):
            NilDepwithotherAddOn = 0
            TariffPackage = 0
            OtherAddOnwithoutNilDep = 0
            Standalone = 1
        else:
            NilDepwithotherAddOn = 0
            TariffPackage = 0
            OtherAddOnwithoutNilDep = 0
            Standalone = 0
            
        Tier = request.form["Tier"]
        if(Tier=='Tier2'):
            Tier2 = 1
            Tier3 = 0
            Tier1 = 0
        elif(Tier=='Tier3'):
            Tier2 = 0
            Tier3 = 1
            Tier1 = 0    
        elif(Tier=='Tier1'):
            Tier2 = 0
            Tier3 = 0
            Tier1 = 1
        else:
            Tier2 = 0
            Tier3 = 0
            Tier1 = 0
            
        Segment = request.form["Segment"]
        if(Segment=='SUV'):
            SUV = 1
            MidSizeCars = 0
            CompactCars = 0
            HighEndCars = 0
        elif(Segment=='MidSizeCars'):
            SUV = 0
            MidSizeCars = 1
            CompactCars = 0
            HighEndCars = 0 
        elif(Segment=='CompactCars'):
            SUV = 0
            MidSizeCars = 0
            CompactCars = 1
            HighEndCars = 0
        elif(Segment=='HighEndCars'):
            SUV = 0
            MidSizeCars = 0
            CompactCars = 0
            HighEndCars = 1
        else:
            SUV = 0
            MidSizeCars = 0
            CompactCars = 0
            HighEndCars = 0
            
        VehicleMake = request.form["VehicleMake"]
        if(VehicleMake=='HONDA'):
            HONDA = 1
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='HYUNDAI'):
            HONDA = 0
            HYUNDAI = 1
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='MARUTI'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 1
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='RENAULT'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 1
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='OthersHE'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 1
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='FORD'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 1
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='MAHINDRAMAHINDRA'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 1
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='Others'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 1
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='TOYOTAMOTORS'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 1
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        elif(VehicleMake=='TATAMOTORS'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 1
            VOLKSWAGEN = 0
        elif(VehicleMake=='VOLKSWAGEN'):
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 1
        else:
            HONDA = 0
            HYUNDAI = 0
            MARUTI = 0
            RENAULT = 0
            OthersHE = 0
            FORD = 0
            MAHINDRAMAHINDRA = 0
            Others = 0
            TOYOTAMOTORS = 0
            TATAMOTORS = 0
            VOLKSWAGEN = 0
        
        prediction = model.predict([[
            Cluster4,
            Cluster6,
            Cluster1,
            Cluster7,
            Cluster8,
            Cluster5,
            Cluster2,
            Cluster3,
            Digital,
            BancaOEM,
            NonBancaOEMDigital,
            OEM,
            FreshRol,
            Renewal,
            FreshNew,
            twenty,
            zero,
            twentyfive,
            fifty,
            thirtyfive,
            fortyfive,
            New,
            Greaterthen55,
            NoBreakIn,
            BreakIn90pdays,
            BreakIn90mdays,
            NoPIP,
            NoCreditScore,
            CSLessthen700,
            CSGreaterthen700,
            VA1to2pt99,
            VA5to6pt99,
            VA3to4pt99,
            VA7to9pt99,
            VA0to0pt99,
            VAGreaterthen10,
            Petrol,
            Diesel,
            Others,
            CNG,
            NilDepwithotherAddOn,
            TariffPackage,
            OtherAddOnwithoutNilDep,
            Standalone,
            Tier2,
            Tier3,
            Tier1,
            SUV,
            MidSizeCars,
            CompactCars,
            HighEndCars,
            HONDA,
            HYUNDAI,
            MARUTI,
            RENAULT,
            OthersHE,
            FORD,
            MAHINDRAMAHINDRA,
            Others,
            TOYOTAMOTORS,
            TATAMOTORS,
            VOLKSWAGEN
        ]])
            
        output=round(prediction[0],2)
        return render_template('home.html',prediction_text="Your rate is. {}".format(output))
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)


        
        
        

            
        
            
        

        

            

            
        
            


    
            
        
    

        
            
        
            

            

            
            
        




            
            
        
        
            
        
            
        
            
            

        
