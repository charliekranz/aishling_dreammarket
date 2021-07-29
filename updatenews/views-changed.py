from django.views import generic
from .models import Post

# Updates and Comments view

# def updatenews(request):
#    """ A view to return the updates and comments page """
#
#    return render(request, 'updatenews/updatenews.html')

def PostList(request, post_id):
    """ A view to show individual Post details """

    post = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'about/about.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
