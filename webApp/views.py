# importing libraries
from django.shortcuts import render
from django.views.generic import TemplateView
from summarizer.bert import Summarizer
# importing form from form.py
from webApp.forms import HomeForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "accounts/login.html"
    # Create a get function to render html with the form
    def get(self, request):
        # Creating an instance of the form created in form.py
        form = HomeForm()
        # Rendering the html template with the django form
        return render(request,self.template_name, {'form':form})#, {'text': textarea})

    def post(self,request):
        # Creating an instance of the form and getting a post request from it
        form = HomeForm(request.POST)
        # Checking if the form has vali details in it
        if form.is_valid():
            # getting the text from the text area of the form which requested the post method
            text = form.cleaned_data['post']
            # getting number of sentence
            num1 = form.cleaned_data['num1']
            # getting minimum number of words in each sentence
            num2 = form.cleaned_data['num2']
        # Text entered in text area is placed in data variable
        data = text
        # removing the Byte Order Mark
        data = data.replace("\ufeff","")
        # Creating an instance of model
        model = Summarizer()
        # Getting the summarized text
        result = model(data, num_sentences=int(num1), min_length=int(num2))
        # Removing / and " in our text
        new = ''
        for i in result:
            if i != "\\" and i != '"':
                new += i
        print(new)
        args = {'form':form, 'text':new}
        # args dictionary is rendered with the html so that text in args can be used in html
        return render(request,self.template_name, args)#, {'text': textarea})
