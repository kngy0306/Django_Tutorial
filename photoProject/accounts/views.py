from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
  '''サインアップページのビュー
  '''
  form_class = CustomUserCreationForm

  template_name = "signup.html"

  success_url = reverse_lazy('accounts:signup_success')


  def form_valid(self, form):
    '''CreateViewクラスのform_valid()をオーバーライド
    
    フォームのバリデーションを通過したときに呼ばれるフォームデータの登録を行う

    parameters:
      form(django.forms.Form):
        form_classに格納されているCustomUserCreationFormオブジェクト
    Return:
      HttpResponseRedirectオブジェクト:
        スーパークラスのform_valid()の返り値を返すことで、success_urlで設定されているURLにリダイレクトさせる
    '''
    # formオブジェクトのフィールド値をDBに保存
    user = form.save()
    self.object = user
    # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
    return super().form_valid(form)


class SignUpSuccessView(TemplateView):
  '''サインアップ完了ページのビュー
  '''
  template_name = "signup_success.html"
