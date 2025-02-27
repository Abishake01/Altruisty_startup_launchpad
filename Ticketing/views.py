from django.shortcuts import render
from .models import Ticket

def ticketing(request):
    # Get the status filter from the request (if any)
    status_filter = request.GET.get('status', '')  # Default to an empty string if no status is selected

    # Filter tickets based on the status filter
    if status_filter:
        tickets = Ticket.objects.filter(status=status_filter)
    else:
        tickets = Ticket.objects.all()

    # Calculate ticket counts
    total_tickets = Ticket.objects.count()
    closed_tickets = Ticket.objects.filter(status='Closed').count()
    pending_tickets = Ticket.objects.filter(status='Pending').count()

    return render(request, 'Ticketing/ticketing.html', {
        'tickets': tickets,
        'total_tickets': total_tickets,
        'closed_tickets': closed_tickets,
        'pending_tickets': pending_tickets,
        'selected_status': status_filter,  # Pass the selected status to the template
    })
