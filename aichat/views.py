from django.shortcuts import render

# Create your views here.
def index(request):
    session_id = request.session.session_key
    if session_id:
        # 使用 session_id
        print(f"Session ID: {session_id}")
    else:
        # session 尚未启动
        print("Session has not been started yet.")
    return render(request, 'aichat/index.html')




    