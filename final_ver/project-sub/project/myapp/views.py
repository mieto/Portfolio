# 各モジュールとライブラリ
from django.shortcuts import render, redirect
from .forms import UploadFileForm, HelpForm
import csv
from .models import Information, Help
import tempfile
import os
import datetime
import locale
from  django.http import HttpResponse

# 関数ベースビュー
# フロントページの描画
def front_page(request):
    template_name = 'myapp/front.html'
    ctx = {'data':template_name}
    return render(request, template_name, ctx)


# CSVファイルのアップロード用の関数
# ロケールを設定
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            # 一時的なファイルの生成
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)

            # csvをデータベースに保存
            with open(temp_file.name, 'r', encoding='cp932', errors='ignore') as csvfile:
                csvreader = csv.DictReader(csvfile)
                next(csvreader)
                for row in csvreader:
                    date_str = row['date']  # カンマを削除

                    # 日付のフォーマットを変更
                    date_format = "%Y-%m-%d"
                    date_obj = datetime.datetime.strptime(date_str, date_format).date()

                    Information.objects.create(
                        date=date_obj,
                        time_slot_a=row['time_a'],
                        time_slot_b=row['time_b'],
                        time_slot_c=row['time_c'],
                        time_slot_d=row['time_d'],
                    )
                      # 既存のデータと比較して重複挿入を防止
                    existing_data = Information.objects.filter(date=date_obj)
                    if not existing_data:
                        Information.objects.create(
                            date=date_obj,
                            time_slot_a=row['time_a'],
                            time_slot_b=row['time_b'],
                            time_slot_c=row['time_c'],
                            time_slot_d=row['time_d'],
                        )

            # 一時的に作成したファイルを削除
            os.remove(temp_file.name)
            return redirect('success_page')
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})

# 成功した時に現れるページ
def success_page(request):
    informations = Information.objects.all()
   
    return render(request, 'myapp/success.html',{'informations': informations})

# 計算するページ
def calculate_page(request):
    if request.method == 'POST':
        hourly_rate = float(request.POST.get('hourly_rate', 0))
        if hourly_rate <= 0:
            return HttpResponse('時給は正の値で入力してください')
        
        # 出勤情報を取得する
        total_work_hours = 0
        informations = Information.objects.all()
        for info in informations:
            total_work_hours += (info.time_slot_a == '〇') + (info.time_slot_b == '〇') + (info.time_slot_c == '〇') + (info.time_slot_d == '〇')
        
        # 実際に計算する
        total_salary = total_work_hours * hourly_rate
        return render(request, 'myapp/calculate.html', {'total_salary': total_salary})
 
    return render(request,'myapp/calculate.html')

# データが溜まるため削除する関数
def delete_data(request):
    if request.method == 'POST':
        Information.objects.all().delete()
        return redirect('upload_file')
    else:
        return render(request, 'myapp/delete.html')
    

# ヘルプの内容を実際にadminサイトに送るための関数
def post_help_page(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            # データベースに保存
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            detail = form.cleaned_data['detail']

            Help.objects.create(name=name, mail=mail, detail=detail)
            return redirect('front_page')
    else:
        form = HelpForm()
    return render(request, 'myapp/help_form.html', {'form':form})

