from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)
# Create your views here.


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request, 'listings/listing.html',context)
# Create your views here.


def search(request):
    return render(request, 'listings/search.html')
