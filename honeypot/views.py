from django.shortcuts import render
from .models import HoneypotAttempt
from django.core.mail import send_mail

def fake_admin_view(request):
    """Fake admin login page that logs intruders and mimics failed login behavior."""
    error_message = None
    username = ""  # Preserve entered username

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # Log the attempt in the database
        ip = get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")
        HoneypotAttempt.objects.create(ip_address=ip, user_agent=user_agent)

        # Send an email alert
        send_mail(
            "🚨 Security Alert: Unauthorized Admin Access",
            f"An unauthorized admin login attempt was detected from IP: {ip}\nUser-Agent: {user_agent}\nUsername: {username}\nPassword: {password}",
            "admin@yourdomain.com",
            ["security@yourdomain.com"],
            fail_silently=True,
        )

        # Fake error message like real Django admin
        error_message = "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."

    return render(request, "fake_admin.html", {"error_message": error_message, "username": username})

def get_client_ip(request):
    """Extract the client's IP address."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
