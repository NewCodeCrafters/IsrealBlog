from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'blog/home_template.html')

# create a view called home_view which points to a template called home_template.html 
# welcome to Isreal Blog
# create url for the blog
# link the blog url to the main url

