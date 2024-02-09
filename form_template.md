# 建立HTML表單
## 自HTML檔案中建立
自HTML中建立表單，不用配合web框架，下例示範建立上傳姓名、照片的表單

[REF](https://medium.com/bandai%E7%9A%84%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/%E6%89%8B%E6%8A%8A%E6%89%8B%E7%A8%8B%E5%BC%8F%E5%AF%A6%E4%BD%9C%E5%88%86%E4%BA%AB%E7%B3%BB%E5%88%97-django%E7%AF%84%E4%BE%8B-%E4%B8%8A%E5%82%B3%E5%80%8B%E4%BA%BA%E5%9C%96%E7%89%87-935d27c36326)

在models.py中建立資料庫邏輯
```python
from django.db import models# Create your models here.
class User(models.Model):    
    user_name = models.CharField(max_length=30)    
    user_image = models.ImageField(upload_to='image/')
    introduce = models.FileField(upload_to='introduce/')
    
    def __str__(self):
        return self.user_name
```
執行`python3 manage.py makemigration` & `python3 manage.py migrate`
接著設定`views.py`
```python
from django.shortcuts import render
from .models import User # 新增的程式碼
def add(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # add.html中的input name
        user_img = request.FILES.get('user_image')
        introduce = request.FILES.get('introduce')
        user = User(user_name=user_name, user_image=user_img, introduce=introduce)
        user.save()
        return render(request, 'upload_profile/add.html', locals())    # =====新增的程式碼=====#
    return render(request, 'upload_profile/add.html', locals())
```

html來可視化&蒐集表單內容
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- 網頁的標題 -->
    <title>添加使用者資料<</title> 
</head>
<body>
    <!-- 顯示在content的大標 -->
    <h1>添加使用者</h1>
    <form action="/upload_profile/add/" enctype="multipart/form-data" method="post">
        {% csrf_token %} # 防止跨站請求偽造
        <label for="user_name">名字:</label>
        <input type="text" name="user_name"><br><br>
        <label for="user_image">大頭貼:</label><br>
        <input type="file" name="user_image"><br><br>
        <label for="introduce">自我介紹:</label><br>
        <input type="file" name="introduce"><br><br>
        <input type="submit" value="提交">    </form>
</body>
</html>
```
```python
from django.shortcuts import render
from .models import User # 新增的程式碼# Create your views here.def add(request):
    # =====新增的程式碼=====#
    if request.method == "POST":
        user_name = request.POST.get('user_name')  # 對應剛剛add.html 中的input name
        user_img = request.FILES.get('user_image')
        introduce = request.FILES.get('introduce')
        user = User(user_name=user_name, user_image=user_img, introduce=introduce)
        user.save()
        return render(request, 'upload_profile/add.html', locals())    # =====新增的程式碼=====#
    return render(request, 'upload_profile/add.html', locals())
```


## 在form.py中建立表單、HTML中顯示
舉例自Django tutorial from MDN
在APP資料夾中建立`forms.py`
```python
from django import forms
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    ...

```
接著在APP資料夾中的`views.py`引入forms.py的內容，並將form的內容透過render傳送給html
```python
book_instance = get_object_or_404(BookInstance, pk = pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
        context = {'form': form, 'book_instance': book_instance}
        return render(request, 'catalog/book_renew_librarian.html', context)
```
在HTML當中取用顯示(appname/templates/appname/book_renew_librarian.html)
```HTML
<form action="" method="post">
        {% csrf_token %}
        <table>
            {{ form }}
            {{ form.as_ul }}
        </table>
    <input type="submit" value="Submit" />
</form>
```