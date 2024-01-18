from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def anylyze(reuqest):
    # get the data from textarea
    djtext= reuqest.POST.get("text","defualt")
    # get checkboc option value 
    removepunc= reuqest.POST.get("removepunc","off")
    uppercase= reuqest.POST.get("uppercase","off")
    newline= reuqest.POST.get("newline","off")
    spaceremover= reuqest.POST.get("spaceremover","off")
    charcount= reuqest.POST.get("charcount","off")
    #Function to Remove Punctuation Marks
    if removepunc=='on':
        anylyze=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                anylyze=anylyze+char
            param ={"puropse":"remove punctuation ","remove_text":anylyze}
            djtext=anylyze
    # Convert to Upper Case
    if uppercase =='on':
        anylyze=""
        for char in djtext:
            anylyze=anylyze+char.upper()
        param ={"puropse":"Upper Case ","remove_text":anylyze}
        djtext=anylyze
        
    # New Line Characters 
    if newline =='on':
        anylyze=""
        for char in djtext:
            if char!="\n" and char !="\r":
                anylyze=anylyze+char
        param ={"puropse":"New Line  ","remove_text":anylyze}
        djtext=anylyze

    # space removing code
    if spaceremover=="on":
        anylyze=""
        for index,char in enumerate(djtext):
            if djtext[index]=="" and djtext[index+1]=="":
                pass 
            else :
                anylyze=anylyze+char
        param ={"puropse":"New Line  ","remove_text":anylyze}
        djtext=anylyze

        #word count code not working 
    # if charcount=="on":
    #     count_dict = {}
    #     for char in djtext:
    #         if char in count_dict:
    #             count_dict[char] += 1
    #         else:
    #             count_dict[char] = 1
    #         co=len(count_dict)
    #         param ={"puropse":"New Line  ","remove_text":anylyze , "count ":co}
    #     return render (reuqest,"anylyze.html",param)  
    return render (reuqest,"anylyze.html",param)
    


