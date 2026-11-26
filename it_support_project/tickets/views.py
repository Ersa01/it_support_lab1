import logging
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

logger = logging.getLogger(__name__)


def ticket_list_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info(f"Өтінім сақталды, ID: {ticket.id}")
            return redirect('ticket_list')
        else:
            logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()

    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {
        'form': form,
        'tickets': tickets,
    })
