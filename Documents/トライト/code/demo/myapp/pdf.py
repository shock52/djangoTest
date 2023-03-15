from . import models
import datetime
import os
import uuid
from xhtml2pdf import pisa
from django.http import Http404, HttpResponse
from django.template.loader import get_template


# wkhtmltopdfのインストールパスを指定
wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# os.path.dirnameでファイル名（パス）を取得
root = os.path.dirname(__file__)
# rootにはadd.pyのパスが格納
if root == '':
    root = '.'
FMT_HTML_ROUTSU = 'myapp/templates/format_comp_routsu.html'  # 読み込むフォーマットHTML
FMT_HTML_SEIYAKUSYO = 'myapp/templates/format_seiyakusyo.html'  # 読み込むフォーマットHTML
STR_FILENAME_ROUTSU = '労働条件通知書'
STR_FILENAME_SEIYAKUSYO = '誓約書'
PDF_SAVE_DIR = os.path.join(os.getcwd(), 'PDF')


class Pdf():
    # 労通PDF化メソッド
    def create_routsu_pdf(self):
        routsu_data = models.ROUTSU_TBL.objects.get(pk='1')  # DBの該当するデータを取得。
        # 挿入するデータ
        context = {'SK_NAME': routsu_data.SK_NAME,
                   'FCL_NAME': routsu_data.FCL_NAME,
                   }
        # ファイルタイプ、PDFであること指定。
        response = HttpResponse(content_type='application/pdf')
        # フォーマットとするHTMLを指定
        format = get_template(FMT_HTML_ROUTSU)
        # フォーマットHTMLにcontext（挿入データ）を渡す
        has_value_format = format.render(context)

        # 以下、システムに生成するPDFの名前生成
        d = datetime.datetime.now()
        str_char = d.strftime('%Y.%m.%d.%H.%M.%S') + str(uuid.uuid4())
        pdf_file_path = f'{STR_FILENAME_ROUTSU}{str_char}.pdf'

        # PDF生成。(保存先パス,出力名)
        output_file_path = os.path.join(PDF_SAVE_DIR, pdf_file_path)
        with open(output_file_path, "w+b") as file:
            # destはPDF生成結果の保存先。responseとすることで画面に渡す。
            pisa_status = pisa.CreatePDF(has_value_format, dest=response)
            pisa_status = pisa.CreatePDF(has_value_format, dest=file)

        if pisa_status.err:
            return HttpResponse(has_value_format)

        delete_pdf(pdf_file_path)

        return response

    # 誓約書PDF化メソッド
    def create_seiyakusyo_pdf(self):
        response = HttpResponse(content_type='application/pdf')
        format = get_template(FMT_HTML_SEIYAKUSYO)
        has_value_format = format.render()

        d = datetime.datetime.now()
        str_char = d.strftime('%Y.%m.%d.%H.%M.%S') + str(uuid.uuid4())
        pdf_file_path = f'{STR_FILENAME_SEIYAKUSYO}{str_char}.pdf'

        output_file_path = os.path.join(PDF_SAVE_DIR, pdf_file_path)
        with open(output_file_path, "w+b") as file:
            pisa_status = pisa.CreatePDF(has_value_format, dest=response)
            pisa_status = pisa.CreatePDF(has_value_format, dest=file)

        if pisa_status.err:
            return HttpResponse(has_value_format)

        delete_pdf(pdf_file_path)

        return response

# ファイル削除処理


def delete_pdf(pdf_file_path):
    delete_file_path = os.path.join(PDF_SAVE_DIR, pdf_file_path)
    if os.path.isfile(delete_file_path):
        os.remove(delete_file_path)
