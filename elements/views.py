from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView
from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from elements.forms import ContactForm
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
    authentication_classes = (TokenAuthentication, )

class ElementsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (IsAdminOrReadOnly, )


#def element_page(request):
#    element = Elements.objects.all()
#
#
#    context = {'element': element,}
#    return render(request, 'elements\element.html', context)

class ElementsListView(generic.ListView):
    model = Elements
    template_name = 'elements/element.html'
    paginate_by = 5

def index(request):
    # добавим сессии
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits':num_visits}
    return render(request, 'elements\index.html', context)


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