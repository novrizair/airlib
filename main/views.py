from django.shortcuts import render
# from .models import Books

def show_main(request):
    books = [
        {'name': '"Bird Box"', 'amount': 4, 'price': 20,'description': 'a contemporary horror novel by Josh.'},
        {'name': '"The Great Gasby"', 'amount': 14, 'price': 13,'description': 'a classic novel by F. Scott Fitzgerald.'},
    ]
    
    context = {
        'books': books,
    }

    # context ={'name': '"The Great Gasby"',
    #         'amount': 14,
    #         'price': 13,
    #         'description': '"The Great Gatsby" is a classic novel by F. Scott Fitzgerald set in the Roaring Twenties. \
    #                         It explores themes of wealth, love, and the American Dream through the story of \
    #                         the enigmatic Jay Gatsby and his obsession with the elusive Daisy Buchanan. \
    #                         This timeless tale of decadence and disillusionment continues to captivate readers with \
    #                         its elegant prose and complex characters.'
    #         }
    
    # Books.objects.get_or_create(name='"The Great Gasby"', amount=14, price=13, description='The Great Gatsby is a classic novel by F. Scott Fitzgerald set in the Roaring Twenties.\
    #                                 It explores themes of wealth, love, and the American Dream through the story of \
    #                                 the enigmatic Jay Gatsby and his obsession with the elusive Daisy Buchanan. \
    #                                 This timeless tale of decadence and disillusionment continues to captivate readers with \
    #                                 its elegant prose and complex characters.') 
        # {'name': '"Bird Box"',
        # 'amount': 4,
        # 'price': 20,
        # 'description': '"Bird Box" is a contemporary horror novel by Josh Malerman. In a world plagued by \
        #                 mysterious creatures that drive people to madness and violence when seen, \
        #                 the story follows a mother, Malorie, and her two children as they navigate \
        #                 a treacherous river blindfolded to reach a rumored safe haven.'
        # }]

    return render(request, "main.html", context)