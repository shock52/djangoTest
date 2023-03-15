from django.urls import path
from . import views,pdf

urlpatterns = [
    path("login/", views.login, name="login"),
    path("dashboard/", views.disp_dashboard, name="disp_dashboard"),
    path("create_new/", views.create_routsu, name="create_routsu"),
    path("edit_routsu/", views.edit_routsu, name="edit_routsu"),
    path("check_routsu/", views.check_routsu, name="format_routsu"),
    path("sendmail_to_facility/", views.send_mail_routsu, name="send_mail_routsu"),
    path("lastcheck/", views.lastcheck_routsu, name="lastcheck_routsu"),
    path("past_routsu/", views.past_routsu, name="past_routsu"),

    path("facility_check_terms/", views.facility_check_terms, name="facility_check_terms"),
    path("facility_edit_routsu/<slug:id>", views.facility_edit_routsu, name="facility_edit_routsu"),
    path("facility_check_routsu/", views.facility_check_routsu, name="facility_check_routsu"),
    path("facility_after_check/", views.facility_after_check, name="facility_after_check"),

    path("seeker_edit_routsu/", views.seeker_edit_routsu, name="seeker_edit_routsu"),

    #労通表示メソッド
    path("facility_after_check/pdf_disp/労働条件通知書.pdf",pdf.Pdf.create_routsu_pdf,name="create_routsu_pdf"),
    #誓約書表示メソッド
    path("facility_after_check/pdf_disp/誓約書.pdf",pdf.Pdf.create_seiyakusyo_pdf,name="create_seiyakusyo_pdf"),
  
]

