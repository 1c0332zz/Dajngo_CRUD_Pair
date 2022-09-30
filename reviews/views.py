from django.shortcuts import render, redirect
from reviews.models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)


def detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)
    return redirect("/reviews")
