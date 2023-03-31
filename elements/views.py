from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView, UpdateView, DeleteView, CreateView, ListView
from rest_framework import generics, viewsets

from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from elements.forms import ContactForm, ElementsForm
from elements.models import Elements
from elements.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from elements.serializers import ElementsSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ElementsAPIList(generics.ListCreateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class ElementsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class ElementsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ElementsListView(generic.ListView):
    model = Elements
    template_name = 'elements/element.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class SearchResult(ListView):
    """Поиск по элементу"""
    model = Elements
    template_name = 'elements/search_result.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        q = query.title().strip()
        object_list = Elements.objects.filter(name__istartswith=q)
        return object_list


def index(request):
    # добавим сессии
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits}
    return render(request, 'elements/index.html', context)


class ElementsDetailView(generic.DetailView):
    model = Elements
    template_name = 'elements/elements_list.html'
    pk_url_kwarg = 'elements_pk'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'elements/contact.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')






class ElementsUpdate(UpdateView):
    model = Elements
    form_class = ElementsForm
    pk_url_kwarg = 'elements_pk'
    success_url = reverse_lazy('element_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['configuration'] = configuration.objects.all()
        return context


class ElementsDelete(DeleteView):
    model = Elements
    fields = '__all__'
    success_url = reverse_lazy('element_page')


class ElementCreate(CreateView):
    model = Elements
    fields = '__all__'
    success_url = reverse_lazy('element_page')
