from django.http import HttpResponse
from django.shortcuts import render
import string

# 1. remove Punctuations
# 2. Capitalize First
# 3. newLineRemover 
# 4. SpaceRemover
# 5. CharCount

punctuation = string.punctuation
def index(request):
    '''to render any file we use render() in django'''
    return render(request,'index1.html')



def capfirst(text):
     text = text.capitalize()
     ans = ''
     # text = text.capitalize()
     ans  =  ''
     for i in range(len(text)):
         if (text[i-1] == ' ' or text[i-1] ==  '\n'):
             ans += text[i].upper()
         else:
             ans+=text[i]
     
     return ans

    

def removePunc(request):
    ''' to access form data in django we use the 'name' attribute to get its value'''
    text = request.GET.get('text','default')
    removePunc = request.GET.get('removepunc','off')
    print(text)
    print(removePunc)
    ans = ''
    for char in text:
        if char not in punctuation:
            ans +=char
    params = {'result':ans,'original_text':text,'option':'Remove Punctuation'}
    # return HttpResponse(f"remove punc {r} {punctuation} ")
    return render(request,'analyze.html',params)   

def newlineremover(request):
    pass

def spaceremover(request):
    pass

def analyzer(request):
    analyzed_text = ''
    purpose = []
    # print(analyzed_text)
    text = request.GET.get('text','default')
    original_text = text
    # 1 option value
    remove_punc = request.GET.get('removepunc','off')
    # 2 option value
    capitalize_first = request.GET.get('capitalizeFirst','off')
    # 3 option value
    newline_remover = request.GET.get('newLineRemover','off')
    # 4 option value
    space_remover  = request.GET.get('spaceRemover','off')
    # 5 option value
    char_count  = request.GET.get('charCount','off')
    analyzed_text = text
    
    if (remove_punc == 'on'):
        ''' to access form data in django we use the 'name' attribute to get its value'''
        print(text)
        print(removePunc)
        ans = ''
        for i in text:
            if i not in punctuation:
                ans +=i

        analyzed_text = ans
        purpose.append('Remove Punctuation')
        # params = {'result':ans,'original_text':text,'option':'Remove Punctuation'}
        # return HttpResponse(f"remove punc {r} {punctuation} ")
        # return render(request,'analyze.html',params)

    if (capitalize_first == 'on'):
        text = analyzed_text.capitalize()
        ans = ''
        # text = text.capitalize()
        ans  =  ''
        for i in range(len(text)):
            if (text[i-1] == ' ' or text[i-1] ==  '\n'):
                ans += text[i].upper()
            else:
                ans+=text[i]
        
        print(ans)
        analyzed_text = ans
        purpose.append("Capitalize First")

    if (newline_remover == 'on'):
        text = analyzed_text
        # lst = text.split()
        # ans = ' '.join(lst)
        # print(lst)
        res = ''
        for char in text:

            if char != '\n' or char != '\r':
                res+=char
        
        analyzed_text = res

        # ans = ''
        # res=[]
        # for i in lst:
        #     res.append(i.replace('\n',''))
        #     # res.append(i.replace('\r',''))
        
        # for char in lst:
        #     ans+=char
        # print(ans)
        # analyzed_text = ans
        purpose.append('New Line Remover')

    if (space_remover == 'on'):
        lst = analyzed_text.split()
        res = ' '.join(lst)
        analyzed_text = res
        purpose.append("Extra Space Remove")

    if (char_count == 'on'):
        counter = 0
        for char in analyzed_text:
            counter+=1
        
        analyzed_text += '\nnumber of character in a text is : ' + str(counter)
        if (capitalize_first == 'on'):
            analyzed_text = capfirst(analyzed_text)

        purpose.append('Char Count')
    
    if (remove_punc != 'on' and capitalize_first != 'on' and newline_remover != 'on' and space_remover != 'on' and char_count != 'on'):

        return HttpResponse('''<h1> Error (select atleast 1 operation) <a href="/">Return Home Page </a></h1>''')

    print(analyzed_text)
    print(purpose)
    params = {'original_text':original_text,'purpose':purpose,'analyzed_text' : analyzed_text}
    return render(request,'analyze1.html',params)



