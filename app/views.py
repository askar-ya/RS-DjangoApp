from django.shortcuts import render



def main_page(request):
    return render(request, 'index.html')

def search_q(request):

    return render(request, 'TestSearch.html', )

