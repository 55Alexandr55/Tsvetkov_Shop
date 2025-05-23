from django.views.generic import ListView, DetailView
from .models import Item, Category
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ReviewForm
from django.shortcuts import redirect



class CatalogView(ListView):
    '''
        главное представление каталога
        
        методы сортировки товаров - по категории, по интервалу цены
        
    '''
    model = Item
    # указываем расположение шаблона
    template_name = 'main/product/catalog.html'
    context_object_name = 'items'

    # собираем сортировки
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slugs = self.request.GET.getlist('category')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if category_slugs:
            queryset = queryset.filter(category__slug__in=category_slugs)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    # передаем контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_categories'] = self.request.GET.getlist('category')
        context['min_price'] = self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('max_price', '')
        return context





# страница товара
class ItemDetailView(DetailView):
    model = Item
    template_name = 'main/product/detail.html'
    context_object_name = 'item'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.object
        context['form'] = ReviewForm()
        context['reviews'] = item.reviews.order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = self.object
            review.save()
            return redirect(self.request.path_info)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


# Поиск товаров по запросу
def item_search(request):
    query = request.GET.get('q', '')
    items = Item.objects.filter(name__icontains=query) if query else []

    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')

    return render(request, 'main/product/search_results.html', {
        'products': items,
        'query': query,
        'categories': categories,
        'selected_categories': selected_categories,
    })


def item_autocomplete(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(name__icontains=query)[:10]
        data = list(items.values('id', 'name'))
    else:
        data = []
    return JsonResponse({'results': data})
