

def heart_rate_calculation():
    RestingHR = int (input('RestingHR:'))
    Age = int (input('Age:'))
    
    print("Intensity|  Rate")
    print("---------|------")
    
    for i in range(55,100,5):
        TargetHeartRate = ((220 - Age) - RestingHR) * i / 100 + RestingHR
        print('{}%      |{}bpm'.format(i,int(TargetHeartRate)))