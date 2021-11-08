from .models import Category


def menu_links(context):
    categories = Category.objects.all()
    return {'categories': categories}
