from myapp.pdf import Pdf
from django.http import Http404
from google.cloud import bigquery as bq
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
import pandas as pd,string,random

#BigQuery接続
# client_bq = bq.Client(project="pj-routu")
# print('プロジェクト接続成功')
#result = client_bq.query(query="SELECT * FROM `pj-routu.test.TEST_TBL`")
# データフレームにする
#df = result.to_dataframe()


# ログイン画面表示
def login(request):
    template_name = "tryt/login.html"
    return render(request,template_name)

# ダッシュボード表示
def disp_dashboard(request):
    template_name = "tryt/dashboard.html","pagenation.html"

    # 以下、ページネーション。DB接続すれば動きます。
    #テーブルのレコード全件取得
    # all_data = ROUTSU_TBL.objects.all()
    #1ページに10件表示
    # paginator = Paginator(all_data, 3)
    #URLのパラメータから現在のページ番号を取得
    # p = request.GET.get('p')
    #指定のページのArticleを取得
    # datas = paginator.get_page(p)

    return render(request,template_name)
    # ↑に{'datas':datas}を書き足してdatasを渡す。

# 労通新規作成画面表示
def create_routsu(request):
    template_name = "tryt/routsu_new_create.html"
    if request.method == "POST":
        # routsu_info = models.ROUTSU_TBL.objects.create(SK_NAME=request.POST["sk_name"],FCL_NAME=request.POST["fcl_name"]) 
        # 第一引数には遷移したいページのview関数 第二引数には主キーを渡す。
        return redirect(edit_routsu)
    return render(request,template_name)

# ★労通情報入力画面表示
def edit_routsu(request):
    template_name = "tryt/routsu_edit.html"
    # try:
    #     routsu_info = models.ROUTSU_TBL.objects.get(pk=pk)#pkからDBの該当するデータを取得。
    # except models.Article.DoesNotExist:
    #     raise Http404
    # context = {"routsu_info": routsu_info}
    return render(request,template_name)

# 労通情報確認画面表示
def check_routsu(request):
    template_name = "tryt/routsu_check.html"
    return render(request,template_name)

# メールアドレス入力画面
def send_mail_routsu(request):
    template_name = "tryt/sendmail.html"
    return render(request,template_name)

# 労通最終確認画面
def lastcheck_routsu(request):
    template_name = "tryt/routsu_lastcheck.html"
    return render(request,template_name)

# 過去の労通表示画面
def past_routsu(request):
    template_name = "tryt/routsu_past.html"
    return render(request,template_name)

# 施設-利用規約確認
def facility_check_terms(request):
    template_name = "facility/facility_check_terms.html"
    return render(request,template_name)

# 施設-労通入力画面表示
def facility_edit_routsu(request,id):
    template_name = "facility/facility_routsu_edit.html"
    try:
        #hashidからDBの該当するデータを取得。
        query = 'SELECT * FROM `pj-routu.test.ROUTSU_TBL` WHERE FCL_PERSON = id'
        df = pd.read_gbq(query,'pj-routu')
        print(df)
    except query.DoesNotExist:
        raise Http404
    # if request.method == "POST":
        #URLはランダム20文字列で生成
        # c = string.ascii_lowercase + string.ascii_uppercase + string.digits
        # length = 30
        #cの中からランダムにチョイスする。それを20回繰り返す。
        #リストにつなげる
        # url = ''.join([random.choice(c) for i in range(length)])
    return render(request,template_name)

# 施設-労通情報確認画面表示
def facility_check_routsu(request):
    template_name = "facility/facility_routsu_check.html"
    #context = {"articles":models.ROUTSU_TBL.objects.all()}
    return render(request,template_name)

# 施設-労通情報確認後画面表示
def facility_after_check(request):
    template_name = "facility/facility_after_check.html"
    if request.method == "POST":
        pdf = Pdf()
        pdf.create_routsu_pdf()
        pdf.create_seiyakusyo_pdf()
    return render(request,template_name)

# 求職者-労通入力画面表示
def seeker_edit_routsu(request):
    template_name = "seeker/seeker_routsu_edit.html"
    return render(request,template_name)
