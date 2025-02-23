from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Contact
from django.http import HttpResponse
from django.urls import reverse
from django.http import QueryDict

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

@require_http_methods(['GET'])
def get_contacts(request):
    contacts = Contact.objects.all()
    if request.headers.get('HX-Request'):
        return render(request, 'partials/contactListPartial.html', {'contacts': contacts})

    return render(request, 'index.html', {'contacts': contacts})

@require_http_methods(['GET'])
def create_contact_modal(request, contact_id=None):
    if contact_id:
        # Edit existing contact
        contact = get_object_or_404(Contact, id=contact_id)
        action = "Edit Contact"
        submit_button_text = "Save Changes"
        url = reverse('edit_contact', args=[contact.id])
    else:
        # Add new contact
        contact = None
        action = "Add Contact"
        submit_button_text = "Add"
        url = reverse('create_contact')

    return render(request, "createContactModal.html", {
        "contact": contact,
        "action": action,
        "submit_button_text": submit_button_text,
        "url": url
    })


@require_http_methods(["POST"])
def create_contact(request):
    name = request.POST.get("name")
    address = request.POST.get("address")
    phone = request.POST.get("phone")

    # Create the new contact
    new_contact = Contact.objects.create(name=name, address=address, phoneNumber=phone)

    # Return only the new contact row instead of the full list
    return render(request, "partials/contactRowPartial.html", {"contact": new_contact})

@require_http_methods(['PUT'])
def edit_contact(request, contact_id):
        put = QueryDict(request.body)
        rowToEdit = get_object_or_404(Contact, id=contact_id)
        rowToEdit.name = put.get("name")
        rowToEdit.address = put.get("address")
        rowToEdit.phoneNumber = put.get("phone")
        rowToEdit.save()

        return render(request, "partials/contactRowPartial.html", {"contact": rowToEdit})


def delete_contact(request, contact_id):
    if request.method == "DELETE":
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()

    return HttpResponse(status=200)


