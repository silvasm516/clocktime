from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import Template, Context
from django.template.context_processors import csrf
from django.template import Template
from django.template import loader
from django.template import RequestContext
# Create your views here.

def EmailHome(request):
    return render(request, 'Email.html')




# from Home page sign-in to date page or sign-up page
def Email_SignIn(request):
    from django.contrib.auth import authenticate, login
    import time
    import datetime 
    from datetime import date
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from django.template.context_processors import csrf
    from django.template import RequestContext
    from timo.models import Drivers		
    if request.method == 'POST':
        d = Drivers.objects.all()
        u = []
        email = request.POST.get('email')
        password = request.POST['email']
        request.session['password'] = password
        request.session.setdefault('password',email)

        for j in range(0, len(d)):
            o = d[j].Email
            u.append(o)
        i = []
        for t in u:
            e = t.lower() 
            i.append(e)   
            v = email.lower()
        
        if v in i:
            f = d.filter(Email = email)
            n = f[0].FirstName
            dte = ""
            request.session['em'] = v
            c = {
                'date': dte,
                'name': n
                }            
            temp = loader.get_template('Dato.html')
            return HttpResponse(temp.render(c, request))
        else:
            skunk = ""
            c = {
                'rat': skunk
                }
            
        temp = loader.get_template('SignUp.html')
        return HttpResponse(temp.render(c, request))




def Drivers_Register(request):
    
    if request.method == 'POST':
        from django.contrib.auth.models import User
        from timo.models import Drivers
        firstname = request.POST.get('firstName')
        email = request.POST.get('email')
        d = Drivers.objects.create(FirstName = firstname, Email = email)
        d.save()
        request.session['password'] = email
        request.session['firstname'] = firstname
    
    c = {    
    'name' : firstname
    }
    temp = loader.get_template('Dato.html')
    return HttpResponse(temp.render(c, request))


def Tod(request):
    #From Date Page
    from timo.models import Drivers
    from timo.models import Run
    from django.contrib.auth.models import User
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from django.template.context_processors import csrf
    from django.template import RequestContext
    import time
    import datetime 
    tody = request.POST.get('butval')
    email = request.POST.get('etval')
    
    request.session['password'] = email
    if tody == "today":
        from timo.models import Run
        allruns = Run.objects.all()
        driver = email
        person = allruns.filter(Email = driver)
        tdate = datetime.date.today().strftime("%j")
        valid = person.filter(Date = tdate)
        op = []
        op = valid
        runs = []
        druns = {}
        
##CREATES A LIST OF SORTED(LOW TO HIGH) RUN "ID's"        
        if list(valid) != []:
            ids = []
            for r in range(0, len(op)):
                ids.append(op[r].id)
                ids.sort()

##CREATES A LIST OF SORTED "RUNS"
            rs = []
            for i in ids:
                r = op.filter(id = i)
                rs.append(r)

##CREATES A LIST OF "ITEMS" CONSISTING OF IN, OUT, DURATION 
##TO BE APPLIED TO JINJA VARS

            items =[]
            for t in rs:
                items.append(t[0].In) 
                items.append(t[0].Out) 
                items.append(t[0].Duration)
            b = 0
              
            for k in items:
                if k is not "":
                    b = b + 1    
            
            w = b % 3
            
            if w == 0:

                c = {
                    'items': items
                    }


                i = {
                    'items': t[0].In
                    }
                    
                temp = loader.get_template('newRun.html')
                return HttpResponse(temp.render(c, request))
            
            else :
                items.remove(t[0].In)
                c = {
                    'item': t[0].In,  
                    'items': items
                    }


##                i = {
##                    'items': t[0].In
##                    }
                

                temp = loader.get_template('Out.html')
                return HttpResponse(temp.render(c, request))
       
                        
        else :
            rabbit = ""
            c = {"c" : rabbit}
            temp = loader.get_template('newRun.html')
            return HttpResponse(temp.render(c, request))
        

##b end        
    elif tody != "today":
##        email = request.POST.get('ezval') 
        request.session['password'] = email
        from timo.models import Run
        allruns = Run.objects.all()
##        driver = email
        driver = email
        person = allruns.filter(Email = driver)
##        tdate = datetime.date.today().strftime("%j")
        tdate = request.POST.get("butval")
        op = person.filter(Date = tdate)
        runs = []
        druns = {}
        
        
##CREATES A LIST OF SORTED(LOW TO HIGH) RUN "ID's"        
        if list(op) != []:
            ids = []
            for r in range(0, len(op)):
                ids.append(op[r].id)
                ids.sort()

##CREATES A LIST OF SORTED "RUNS"
            rs = []
            for i in ids:
                r = op.filter(id = i)
                rs.append(r)

##CREATES A LIST OF "ITEMS" CONSISTING OF IN, OUT, DURATION 
##TO BE APPLIED TO JINJA VARS

            items =[]
            for t in rs:
                items.append(t[0].In) 
                items.append(t[0].Out) 
                items.append(t[0].Duration)
            today = datetime.date.today()
            dx = datetime.datetime(today.year, 1, 1) + datetime.timedelta(int(tdate) - 1)
            rx =dx.strftime("%a %b %d") 
            c = {
            'md' : rx,
            'items' : items,
            'tag' : email
            }

                
                        
            temp = loader.get_template('Hist.html')
            return HttpResponse(temp.render(c, request))


        
        else:
            carp = 'go'
            c = {
                'rat': carp,
                'tag': email
                }

            temp = loader.get_template('Notice.html')
            return HttpResponse(temp.render(c, request)) 
            


          
def Trip(request):
    # From Save on In Page
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from django.template.context_processors import csrf
    from django.template import RequestContext
    import time
    import datetime
    if request.method == "POST":
        runin = request.POST.get('newRun')
        email = request.POST.get('etval')
        request.session['password'] = email
        
        from timo.models import Run
        ##start
        allruns = Run.objects.all()
        person = allruns.filter(Email = email)
        tdate = datetime.date.today().strftime("%j")
        valid = person.filter(Date = tdate)
        v = len(valid)
        op = valid
        ##end
        
        r = Run.objects.create(Date = datetime.date.today().strftime("%j"), Email = email, In = runin)
        r.save()
        
        ##start
##CREATES A LIST OF SORTED(LOW TO HIGH) RUN "ID's"        
        if list(valid) != []:
            ids = []
            for u in range(0, len(op)):
                ids.append(op[u].id)
                ids.sort()

##CREATES A LIST OF SORTED "RUNS"
            rs = []
            for i in ids:
                u = op.filter(id = i)
                rs.append(u)

##CREATES A LIST OF "ITEMS" CONSISTING OF IN, OUT, DURATION 
##TO BE APPLIED TO JINJA VARS

            items =[]
            for t in rs:
                items.append(t[0].In) 
                items.append(t[0].Out) 
                items.append(t[0].Duration)
                
            
            c = {
                'item':runin,
                'items': items
                }
            temp = loader.get_template('out.html')
            return HttpResponse(temp.render(c, request))
        item = runin
            
        i= {
            'item': item
            }
            
        temp = loader.get_template('out.html')
        return HttpResponse(temp.render(i, request))

def Complete(request):
    # From Save on Out Page
    from django.views.decorators.csrf import csrf_protect 
    from django.shortcuts import render
    from django.template import Template
    from django.template import loader
    from django.http import HttpResponse
    from django.template.context_processors import csrf
    from django.template import RequestContext
    import time
    import datetime
    if request.method == "POST":
        runout = request.POST.get('newRun')
        email = request.POST.get('emval')
        from timo.models import Run
        allruns = Run.objects.all()
        person = allruns.filter(Email = email)
        tdate = datetime.date.today().strftime("%j")
        valid = person.filter(Date = tdate)
        ids = []
        for r in range(0,len(valid)):
            ids.append(valid[r].id)
        b = max(ids)
##        e = valid[0].id
        j = Run.objects.get(id = b)
        j.Out = runout
        s = j.In
        j.save()
        #The Following Calculates Duration
        import time
        import datetime
        from timo.models import Run
        w = Run.objects.all()
        ip = w.filter(Date = datetime.date.today().strftime("%j"))
        op = ip.filter(Email = email)
        for r in range(0,len(op)):
            ids.append(op[r].id)
        b = max(ids)
        j = Run.objects.get(id = b)
        fu = j.In
        gu = j.Out
        n1 = time.strptime(fu,'%H:%M %p')
        n2 = time.strptime(gu,'%H:%M %p')
        h1 = n1.tm_hour* 60
        m1 = n1.tm_min
        h2 = n2.tm_hour* 60
        m2 = n2.tm_min
        time1 = h1 + m1
        time2 = h2 + m2
        diff = time2 - time1
        if h1 > h2:
            adj = 720 - time1
            diff = adj + time2
        #Hours
        f = int(diff/60)
        #Minutes
        m = diff - (60 * f)
        tyme = (str(f)+'hrs' + str(m) + 'min')
        dri = Run.objects.get(id = b)
        dri.Duration = str(tyme)
        dri.save()
    c = {'item' : s,
        'Out' : runout,
        'Duration' : tyme
        }
    
    temp = loader.get_template('out.html')
    return HttpResponse(temp.render(c, request)) 
    

    
def logout_view(request):
    from django.contrib.auth import logout 
    logout(request)
    # Redirect to a success page.
    temp = loader.get_template('Email.html') 
    a = ''
    c = {

         'frog': a

         }
    temp = loader.get_template('Email.html')
    return HttpResponse(temp.render(c, request))


def sessinvar(request):
    from timo.views import Tod
    email = request.POST.get('ezval')
    request.session['password'] = email
    Tod(request)
    c = {
        'request.session.password': email
        }
    temp = loader.get_template('Dato.html')
    return HttpResponse(temp.render(c, request))
