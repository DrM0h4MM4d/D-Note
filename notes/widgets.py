from django.forms import Textarea


class DivTextarea(Textarea):
    template_name = 'custom_widget/div.html'
