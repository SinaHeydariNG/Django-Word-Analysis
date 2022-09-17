from ast import operator
from django.shortcuts import render
import operator

# Create your views here.

def count(request):

    statement = request.GET.get('statement')
    wordstolist = statement.split()
    count = len(wordstolist)
    worddictionary = {}

    for word in wordstolist:
        if word in worddictionary:
            worddictionary[word] += 1
        elif word not in worddictionary:
            worddictionary[word] = 1      
    sortedwords = sorted(worddictionary.items() , key=operator.itemgetter(1) , reverse=True)            
    context = {
        "sortedwords" : sortedwords,
        "statement" :statement,
        "count" : count}
    return render(request , 'count/main.html' , context)