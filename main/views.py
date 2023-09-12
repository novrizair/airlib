from django.shortcuts import render

def show_main(request):
    books = [
        {'name': '"Bird Box"', 'amount': 4, 'price': 20,'description': 'a contemporary horror novel by Josh.'},
        {'name': '"The Great Gasby"', 'amount': 14, 'price': 13,'description': 'a classic novel by F. Scott Fitzgerald.'},
    ]
    
    context = {'books': books,
               'nama': 'Novrizal Airsyahputra',
               'kelas': 'PBP-A',
               'aplikasi': 'airlib'
               }

    return render(request, "main.html", context)