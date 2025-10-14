from django.shortcuts import render
from .forms import AirportRouteForm, SearchForm, ShortestRouteForm
from .models import AirportRoute

# Home page
def index(request):
    return render(request, 'index.html')


# Add a new Airport Route
def add_route(request):
    form = AirportRouteForm(request.POST) #Checks if the form was submitted
    message = ""

    if request.method == 'POST' and form.is_valid():
        form.save()  # Save new route
        message = "Airport Route added successfully!"
        form = AirportRouteForm()  # Reset the form

    return render(request, 'add_route.html', {'form': form, 'message': message})


# Find Nth Left or Right Node
def find_nth_node(request):
    result = None  #placeholder to store the Nth node found
    form = SearchForm(request.GET)  # use GET for search

    if form.is_valid():
        direction = form.cleaned_data['direction']
        n = form.cleaned_data['n']

        # Filter routes by direction
        routes = AirportRoute.objects.filter(position=direction).order_by('id')

        # Pick Nth node (1-based index)
        if routes.count() >= n:
            result = routes[n - 1]
        else:
            result = "No such node found!"

    return render(request, 'find_nth_node.html', {'form': form, 'result': result})


# Find the Longest Node by Duration
def longest_node(request):
    longest = AirportRoute.objects.order_by('-duration').first()  # Max duration
    return render(request, 'longest_node.html', {'longest': longest})


# Find the Shortest Node Between Two Airports
def shortest_node(request):
    result = None
    form = ShortestRouteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        src = form.cleaned_data['source'].upper()
        dest = form.cleaned_data['destination'].upper()

        # Find routes for source or destination, order by duration
        routes = AirportRoute.objects.filter(
            airport_code__in=[src, dest]
        ).order_by('duration')

        if routes.exists():
            result = routes.first()  # Pick shortest

    return render(request, 'shortest_node.html', {'form': form, 'result': result})
