from django.shortcuts import render

def show_main(request):
    context = {
        'name': '"The Great Gasby"',
        'amount': 14,
        'price': 13,
        'description': '"The Great Gatsby" is a classic novel by F. Scott Fitzgerald set in the Roaring Twenties. \
                            It explores themes of wealth, love, and the American Dream through the story of \
                            the enigmatic Jay Gatsby and his obsession with the elusive Daisy Buchanan. \
                            This timeless tale of decadence and disillusionment continues to captivate readers with \
                            its elegant prose and complex characters.'
    }

    return render(request, "main.html", context)