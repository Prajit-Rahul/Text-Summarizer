from django import forms
# Creating a Class to create django forms
class HomeForm(forms.Form):
    # Creating a text box for user to place the text
    post = forms.CharField(widget=forms.Textarea,label='')
    # Creating a integer field for user to specify number of sentence he need in the summarized text
    num1 = forms.IntegerField(label='number of sentence')
    # Creating a integer field for user to specify minimum number of words in each sentence
    num2 = forms.IntegerField(label='min length of sentence')
