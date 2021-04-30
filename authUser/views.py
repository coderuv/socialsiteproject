from django.shortcuts import render,redirect
from .models import Contact,user_post,userconnection,followcount
# Create your views here.
from django.http import HttpResponse


def login(request):
            if request.method == 'POST':

                mob = request.POST.get('mobile')
                psw = request.POST.get('psw')
                print(mob,psw)
                dbData = Contact.objects.all()
                print(dbData)
                flag = "0"
                for item in dbData:
                    print(item.mobile)
                    if mob == item.mobile:
                        print("right number")
                        if psw == item.password:
                            print("right password")
                            request.session['user'] = mob
                            #return render(request,'userhome.html')
                            return redirect('userhome')
                        else:
                            print("wrong password")
                            flag = "1"
                            #return HttpResponse("wrong password")

                            #return render(request,'login.html')
                    else:
                        print("wrong number")
                        flag = "1"
                        #return HttpResponse("wrong number")
                        #return render(request,'login.html')
            #return render(request,'login.html',{'message':'wrong id & pass'})
            return render(request,'login.html')

def signup(request):
        if request.method == 'POST':
            print("This is post")
            name = request.POST['name']
            mobile = request.POST['mobile']
            email = request.POST['email']
            password = request.POST['psw']
            print(name,mobile,email,password)
            ins = Contact(name=name,email=email,mobile=mobile,password=password)
            count=0
            insFollow = followcount(followId=mobile,noOfFollow=count)


            dbData = Contact.objects.all()
            print(dbData)
            for item in dbData:
                print(item.mobile)
                if mobile == item.mobile:
                    print("Duplicate entry mobile number should be unique")
                    return HttpResponse("Duplicate entry mobile number should be unique")
                else:
                    ins.save()
                    insFollow.save()
                    print("data saved")
                    #return HttpResponse("data saved")


        return render(request,'signup.html');

def userhomefun(request):
         username = request.session['user']
         print(username)
         print("hii iam user home")
         e = followcount.objects.get(followId=username)
         ConUserdata = userconnection.objects.all()
         #ConUserdata = .objects.get(userId=username)
    #return HttpResponse("hello world");

         return render(request,'userhome.html',{'username':username,'conUser':ConUserdata,'followedpeople':e.noOfFollow})



def createpostfun(request):
          #return HttpResponse("post");
          if request.method == 'POST':
              print("This is  create post")
              description = request.POST['desc']
              visibility = request.POST['visibility']
              #imgname = request.POST['file_img']
              imgname = request.FILES['file_img']
              username = request.session['user']
             # print(description,visibility)
              document = user_post(filedata=imgname,description=description,visibility=visibility,userid=username)
              #document = userpost.objects.create(filedata=imgname)
              document.save()
              return HttpResponse("your file saved")
          return render(request,'Create_post.html')




def search_fun(request):

          if request.method == 'POST':
              searchdata = request.POST['search_argument']
              dbData = Contact.objects.all()
              username = request.session['user']
              flag="data"
              connectionData = userconnection.objects.all()
              for item in dbData:
                 # print(item.mobile)
                  if searchdata == item.mobile or searchdata == item.name or searchdata == item.email:
                     #return HttpResponse("user found");
                    # return redirect('showuser',{'obj':dbData})
                    print(item.mobile)

                    for itemCon in connectionData:
                        print(itemCon.userConnectionId)
                        print(itemCon.userId)
                        if itemCon.userId == username and item.mobile == itemCon.userConnectionId:
                            flag="following"

                        else:
                            flag="Add Connection"


                    return render(request,'showuser.html',{'obj':item.mobile,'userid':username,'status':flag})
                  else:
                      #return HttpResponse("user not found");
                      print("user not found")
              #entry = Contact.objects.get(mobile=searchdata)
             # print(entry)
             # if entry=='null':
                 # return HttpResponse("user not found");
              #else:
                   #return HttpResponse("user found");
              #return HttpResponse("hello world");
          return render(request,'searchform.html')



def showuser_fun(request):

            print("show user called");
            return render(request,'showuser.html')





def alluser_fun(request):

                     dbData = Contact.objects.all()
                     #userid = {
                              #"userId": dbData
                            #}

                    # userid2 = {
                            #  "userId2": dbData
                            #}

                     return render(request,'alluser.html',{'db1':dbData,'db2':dbData,'flags':'1'})
                     #return userid




def follow_fun(request):

                            ID = request.GET['id']
                            username = request.session['user']
                            insF = userconnection(userConnectionId=ID,userId=username)
                            e = followcount.objects.get(followId=username)
                            e.noOfFollow = e.noOfFollow + 1
                            e.save()
                            insF.save()
                            return HttpResponse("you follows this person from now!!");
                     #return userid
