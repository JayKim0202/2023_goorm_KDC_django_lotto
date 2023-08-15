from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    lottos = GuessNumbers.objects.all()  # DB에 저장된 GuessNumbers 객체 모두를 가져온다.

    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    # {} : context-dict
    return render(request, "lotto/default.html", {"lottos": lottos})


def post(request):
    """ request.POST -> dict
        - dict의 key == input tage의 name 값
        - dict의 value == input tag의 value 값 (== USER의 입력값)"""

    # POST 요청이 들어온 경우
    if request.method:
        # print(request.POST)  # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # print(request.method)   # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST)  # filled form
        # print(type(form))   # <cqalss 'lotto.forms.PostForm'>
        # print(form)
        if form.is_valid():
            # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            # 최종 DB 저장은 아래 generate 함수 내부의 .save5()로 처리
            lotto = form.save(commit=False)
            # print(type(lotto))  # class 'lotto.models.GuessNumbers'>
            # print(lotto)
            lotto.generate()
            return redirect('index')  # urls.py의 name='index'에 해당
        else:
            form = PostForm()   # empty form
            return render(request, "lotto/form.html", {"form": form})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1")


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(id=lottokey)

    return render(request, 'lotto/detail.html', {"lotto": lotto})
