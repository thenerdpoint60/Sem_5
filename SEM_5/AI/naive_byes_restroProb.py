class NaiveBayes:
    def __init__(self,f,r):
        self.features=f
        self.response=r

    def predict(self,custcase):
        anskeys=list(self.response.keys())
        ansvalues=dict.fromkeys(anskeys,0)
        for key in anskeys:
            ansvalues[key]=self.response[key]
            for ikey,ival in custcase.items():
                ansvalues[key]=ansvalues[key]*self.features[ikey][ival][key]

        print(ansvalues)
        maxkey=""
        maxans=-1
        for ikey,ival in ansvalues.items():
            if ikey>maxans:
                maxans=ival
                maxkey=ikey
        return maxkey

response = {"Wait":0.4,"Leave":0.6}
features={"Reservation":{
                                "Yes":{"Wait":0.5,"Leave":0.66},
                                "No":{"Wait":0.5},"Leave":0.33}
              ,
              "Time>30":{
                          "Yes":{"Wait":0.25,"Leave":0.833},
                          "No":{"Wait":0.75,"Leave":0.1666}}
              }

nb=NaiveBayes(features,response)
resstatus=input("Manager asks customer,have you reserved table(Yes/No):")
timestatus = input("Customer asks manager,will it take more than 30 mins?(Yes/No):")
custcase={"Reservation":resstatus,"Time>30":timestatus}
print("Manager predicts predicts thgat customer will :",nb.predict(custcase))
