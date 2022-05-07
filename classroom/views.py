from re import T
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher




# functionbased view
#def home_view(request):
    #   return render(request,'classroom/home.html')
#same thing below

#classbased view
class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    model =  Teacher

#returns 1 instance
class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')



class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #success url?
    #its url not template
    success_url = reverse_lazy('classroom:thank_you')

    #wht to do with the form
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

