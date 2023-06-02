from django.core.mail import EmailMessage
from rest_framework.generics import get_object_or_404

from .serializers import MovieSerializer, SeatSerializer, ShowTimeSerializer, TicketSerializer
from .models import Movie, Seat, ShowTime
from rest_framework import viewsets, views, mixins
from rest_framework.response import Response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class MovieViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()


class ShowTimeView(views.APIView):
    def get(self, request):
        show_time_id = request.GET.get('id')
        movie_id = request.GET.get('movie')
        if show_time_id:
            show_time = ShowTime.objects.get(pk=show_time_id)
            serializer = ShowTimeSerializer(show_time)
        elif movie_id:
            show_times = ShowTime.objects.filter(movie=movie_id)
            serializer = ShowTimeSerializer(show_times, many=True)
        else:
            show_times = ShowTime.objects.all()
            serializer = ShowTimeSerializer(show_times, many=True)
        return Response(serializer.data)


# отправка билета на почту

def send_ticket_email(ticket_data):
    pdf_filename = 'ticket.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont('Helvetica', 14)
    c.drawString(100, 750, "Добро пожаловать на сеанс!")
    c.drawString(100, 700, f"Фильм: {ticket_data['movie_title']}")
    c.drawString(100, 680, f"Время: {ticket_data['showtime']}")
    c.drawString(100, 660, f"Место: Ряд {ticket_data['row']}, Место {ticket_data['number']}")
    c.save()

    # отправка письма с прикрепленным билетом
    subject = 'Ваш билет'
    message = 'Добро пожаловать на сеанс. Билет прикреплен к письму.'
    from_email = 'bakhmudov.bagatir@gmail.com'
    to_email = [ticket_data['email']]

    # прикрепление сгенерированного pdf-файла
    email = EmailMessage(subject, message, from_email, to_email)
    email.attach_file(pdf_filename, 'application/pdf')
    email.send()


class TicketOrderView(views.APIView):
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket_data = serializer.validated_data
            send_ticket_email(ticket_data)
            return Response({'message': 'Билет успешно заказан и отправлен на почту.'})
        else:
            return Response(serializer.errors, status=400)
