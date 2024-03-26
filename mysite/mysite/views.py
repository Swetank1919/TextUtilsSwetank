from django.http import  HttpResponse 
from django.shortcuts import render
def index(request):
   
    return render(request,'index.html')
   
def about(request):
    return HttpResponse('about sweta')
def htao(request):
   

   
   
 
    check=(request.GET.get('removePunc','off'))
    sp=(request.GET.get('spacehta','off'))
    

    djtext=(request.GET.get('text','default'))

    bda=request.GET.get('upperkr','off')
    hta=request.GET.get('linehta','off')
    if check=='on':
        puncuations='''/.,'"*|({[~+=-&^%$#'''
        stirng=''
        for char in djtext:
            if char not in puncuations:
                stirng+=char 
        params={'purpose':'hta do bkr cheejo ko','unch':stirng}
        djtext=stirng
        #return render(request,'bda.html',params)
    if bda=='on':
        stirng=''
        for char in djtext:
            stirng+=char.upper()
        params={'purpose':'issebda kardo','unch':stirng}
        djtext=stirng
        #return render(request,'bda.html',params) 
    if hta=='on':
        string=''
        for char in djtext:
            if char=='\n':
                djtext.remove(char)
        params={'purpose':'line remove karna','unch':string}
        #return render(request,'bda.html',params) 
        djtext=stirng
    if sp=='on':
        stirng=''
        for index , char in  enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                stirng+=char
        params={'purpose':'space remove karna','unch':stirng}
        djtext=stirng
        #return render(request,'bda.html',params)
    if(check!='on' and hta!='on' and sp!='on' and bda!='on' ):
         
        return HttpResponse('saale off hogya')
    return render(request,'bda.html',params)
            



        
        
        
            

        
        
   
    

   
    print(bda)
    print(check)
    print(djtext)
    print(hta)
    
    
   
    
   
   
    return render(request,'remove.html')

   
    return HttpResponse('dekhlo text')
    
    
