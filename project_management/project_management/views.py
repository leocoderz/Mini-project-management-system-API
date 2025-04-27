from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>🚀 Welcome to Project Management API</h1>
        <p>Use the following endpoints:</p>
        <ul>
            <li><a href="/swagger/">Swagger API Docs</a></li>
            <li><a href="/admin/">Django Admin Panel</a></li>
            <li><a href="/api/register/">Register New User</a></li>
            <li><a href="/api/token/">Login (JWT Token)</a></li>
            <li><a href="/api/projects/">Projects API</a></li>
            <li><a href="/api/tasks/">Tasks API</a></li>
        </ul>
        <p>Happy Building! 🚀</p>
    """)
