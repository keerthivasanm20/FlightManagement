from django.shortcuts import render,redirect
import pyrebase
config = {
  "apiKey": "AIzaSyB0o1nitaAVdZah346pksYqbMC41c9pqt0",
  "authDomain": "studentactivitymaintence.firebaseapp.com",
  "databaseURL": "https://studentactivitymaintence.firebaseio.com",
  "projectId": "studentactivitymaintence",
  "storageBucket": "studentactivitymaintence.appspot.com",
  "messagingSenderId": "64618605497",
  "appId": "1:64618605497:web:9cdd5d310a3b878e022468",
  "measurementId": "G-RB67K33HC5"
}
user=""
fkid={"Bangalore":['FKj01','FKJ02'],"Chennai":['FKJ06'],"Kolkata":['FKJO4']}
firebase=pyrebase.initialize_app(config)
auth1 = firebase.auth()
database=firebase.database()
# Create your views here.
def sample(request):
        
        return render(request,'index.html')
def logsample(request):
       return render(request,'index.html',{"k":"k"})
def signup(request):
  if request.method == "GET":    
            return render(request,'signup.html')
  else:
     #global email,password,user,session_id
     name = request.POST.get('name')
     email=request.POST.get('email')
     password=request.POST.get('pass')
     n=request.POST.get('admin')
     #creating  user with email and password 
    
     try:
         user=auth1.create_user_with_email_and_password(email,password)
     except:
          er="Weak identity"
          
          return render(request,'signup.html',{'er':er})
     
     #global user
     uid = user['localId']
    
     idtoken=request.session.get('uid',None)
     
     data={
          "name":name,"status":"1","admin":n,
     }
     print(idtoken)
     print(data)
     #pushing of data
     if n == "yes":
         r="admin"
     else: 
         r="user" 
     timestamps=database.child("users").child(r).child(uid).child("details").set(data,idtoken)
     print(timestamps)
     
     return render(request,'index.html')
def view(request):
    if request.method=="GET":
          return render(request,"View.html")
    else:
         fro=request.POST.get('from')
         to=request.POST.get('to')
         cap=request.POST.get('cap')
         date=request.POST.get('date')
         name={}
         a="a"
         #print(to)
         for i,j in fkid.items():
              if fro == i:
               #  print(j) 
                 for k in range(len(j)):    
                     #print(j[k])
                     name[k]=database.child("users").child("Flight_Detail_card").child(fro).child(j[k]).get().val()
         #print(name)
         count=0
         sa=str(to)
         same={}
         ra=0
         for i,j in name.items():
            if j is not None:
              k=j['To_where']
              da=j['Date']
              print(da)
              if k == to :
                same[ra]=j
                ra+=1               
            else:
                 a="ale" 
         #print(same) 
         m=1
        # print(same)
         return render(request,"View.html",{'n':same,'m':m,'to':to,"a":a,"cap":cap,"date":date})  
def Login(request):
    if request.method == "GET":
             return render(request,"login.html")
    else:
            

     #global email,password,user,session_id
          email =request.POST.get("email")
          password =request.POST.get("pass")
          global user
          try :

               user = auth1.sign_in_with_email_and_password(email,password)
               #print(])
          except :
               msg = "invalid"
               return render(request,'index.html',{"msg":msg})
            
          session_id=user['idToken']
          
         
          idtoken=user['idToken']
          a = auth1.get_account_info(idtoken)
          a = a['users']
          a=a[0]
          a = a['localId']
          print(a)
          
          wor=database.child("users").child("admin").child(a).child("details").get().val()
          
          if wor == None:
               print("user")
               k="user"
          else:
               print("admin")
               k="admin"
          return render(request,"index.html",{"k":k})
def logout(request):
       try:
            del request.session['uid']
       except KeyError:
            pass
       return render(request,"index.html")
def add(request):
  if request.method == "GET":
       return render(request,"create.html")

  else:

     import time
     from datetime import datetime, timezone
     import pytz
     
     tz = pytz.timezone('Asia/Kolkata')
     time_now=datetime.now(timezone.utc).astimezone(tz)
     millis=int(time.mktime(time_now.timetuple()))
     #console.log("time stamp :"+str(millis)) 
     name = request.POST.get('name')
     fro = request.POST.get('from')
     to = request.POST.get('to')
     rtrip = request.POST.get('rtrip')
     date = request.POST.get('date')
     rdate = request.POST.get('rdate')
     capacity = request.POST.get('cap'),
     cost=request.POST.get('cost')
     Fid=request.POST.get('Fid')
     data={

               'Flight_name':name,
                'From_where':fro,
                'To_where':to,
                'Round_Trip':rtrip,
                'Date':date,
                'Round_trip_date':rdate,
                'Capacity':capacity,
                'Travel_cost':cost,
                 
     }
     try:
         
          #pushing into the firebase 
          database.child("users").child("Flight_Detail_card").child(fro).child(Fid).set(data)
          name=database.child("users").child("Flight_Detail_card").child(fro).child(Fid).get().val()
          for key, value in name.items():
                    print(key, value)
             
          
          
          return render(request,"index.html",{'k':"admin"}) 
     except KeyError:
            mg="User Logged out please sign in again"
            return render(request,'create.html',{'msg':mg}) 

def book(request):
      if request.method == "POST":
            # fn=request.POST.get("Flightname")
            # fw=request.POST.get("From_where")
            # tw=request.POST.get("To_where")
            # dt=request.POST.get("dt")
            # tc=request.POST.get("Travel_cost")
            # quantity=request.POST.get("quantitiy")
            # print(quantity)
            # print(tc)
            # bill=1            
            # data={
            #     "fn":fn,"fw":fw,"tw":tw,"dt":dt,"tc":tc,"quantity":quantity,"bill":bill
            # }
             
          c=request.POST.get("dimple")
          print(c)
          c=c.split(',')
          d={}
          for i in range(len(c)):
               d[i]=c[i]
          
          print(d)
          data={}
          data["Flightname"]=d[0]
          data["From_where"]=d[1]
          data["To_where"]=d[2]
          data["Travel_cost"]=d[3]
          data["quantity"]=d[4]
          data["dt"]=d[5]
          data["bill"]=int(d[3])*int(d[4])

              
            
      try:      
            global user
            #print(user)
            idtoken=user['idToken']
            a = auth1.get_account_info(idtoken)
            a = a['users']
            a=a[0]
            a = a['localId']
            import time
            from datetime import datetime, timezone
            import pytz
     
            tz = pytz.timezone('Asia/Kolkata')
            time_now=datetime.now(timezone.utc).astimezone(tz)
            millis=int(time.mktime(time_now.timetuple()))
     
          
            
            database.child("users").child("bookings").child(a).child(millis).set(data,idtoken)
            return render(request,"book.html",{"data":data})
      except KeyError:
            mg="User Logged out please sign in again"
            return render(request,'index.html',{'msg':mg}) 
def deleadmin(request):
  
  if request.method == "POST":  
    dip=request.POST.get("date")
    
    print(dip)
    global user  
            #print(user)
    idtoken=user['idToken']
    a = auth1.get_account_info(idtoken)
    a = a['users']
    a=a[0]
    a = a['localId']
    category =["Chennai","Bangalore","Kolkata"]
    ans=[]
    for i in range(3):
      #print(fkid[category[i]][0])
      for j in range(len(fkid[category[i]])):  
           
         ans.append(database.child("users").child("Flight_Detail_card").child(category[i]).child(fkid[category[i]][j]).child("Date").get().val())
         #print(ans)                          
                           
         #print(ans[i])
         #print(dip)   
         print(fkid[category[i]][0])     
         if str(ans[i]) == str(dip):
                      database.child("users").child("Flight_Detail_card").child(category[i]).child(fkid[category[i]][j]).remove()
                      #return render(request,"index.html",{"k":"k"})
  
    return render(request,"index.html",{"k":"admin"})
  else:
        
            #print(user)
        
        return render(request,"deleteadmin.html",{"m":'m',"a2":"a2"})
 
def dele(request):
  global user  
  if request.method == "POST":  
    dip=request.POST.get("dip")
    dip=dip.split(',')
    print(dip)
    print(dip[0])
            #print(user)
    idtoken=user['idToken']
    a = auth1.get_account_info(idtoken)
    a = a['users']
    a=a[0]
    a = a['localId']
    timestamps=database.child("users").child("bookings").child(a).shallow().get(idtoken).val()
    lis_tim=[]
    if timestamps is  None :
             return render(request,"index.html",{"errrr":"errrr"})
    else:   
      for j  in  timestamps:
                         lis_tim.append(j)
                                             
      lis_tim.sort(reverse=True)
      wor=[]
      for l in range(len(lis_tim)):
                                   
                           
            wor.append(database.child("users").child("bookings").child(a).child(lis_tim[l]).child('Flightname').get(idtoken).val())
      for i in range(len(wor)):
            if wor[i] == dip[0]:
                      database.child("users").child("bookings").child(a).child(lis_tim[i]).remove()
                      return render(request,"index.html",{"k":"k"})
  
      return render(request,"index.html",{"k":"k"})
  else:
        
            #print(user)
        idtoken=user['idToken']
        a = auth1.get_account_info(idtoken)
        a = a['users']
        a=a[0]
        a = a['localId']

        
        timestamps=database.child("users").child("bookings").child(a).shallow().get(idtoken).val()
        lis_tim=[]
        for j  in  timestamps:
                         lis_tim.append(j)
                                             
        lis_tim.sort(reverse=True)
        i=0
        a2={}
        for l in lis_tim:
                                   
                    print(l)       
                    a2[i]=(database.child("users").child("bookings").child(a).child(l).get(idtoken).val())
                    print(a2)
                    i+=1 
        return render(request,"delete.html",{"m":'m',"a2":a2})
 