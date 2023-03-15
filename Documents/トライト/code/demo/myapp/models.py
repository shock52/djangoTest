from django.db import models
from unittest.util import _MAX_LENGTH


# 労働条件通知書テーブル


class ROUTSU_TBL(models.Model):
    # 1_労通ID(自動PK)
    ID = models.AutoField(primary_key=True, editable=False)
    # 2_公開/非公開フラグ
    OPEN_FRAG = models.BooleanField(default=1)
    # 3_有効期限
    DEADLINE_DATE = models.DateField(null=True)
    # 4_ステータス
    STATES = models.CharField(max_length=20, null=True)
    # 5_SFID
    SFID = models.CharField(max_length=10, null=True)
    # 6_法人用URL
    FCL_URL = models.CharField(max_length=20, null=True)
    # 7_法人採用担当者氏名
    FCL_PERSON = models.CharField(max_length=20, null=True)
    # 8_法人採用担当者連絡先
    FCL_PHONENUMBER = models.CharField(max_length=15, null=True)
    # 9_法人メールアドレス
    FCL_MAILADDRESS = models.CharField(max_length=50, null=True)
    # 10_法人送付日時
    FCL_SEND_DATE = models.DateTimeField(null=True)
    # 11_法人受領日時
    FCL_ACCEPT_DATE = models.DateTimeField(null=True)
    # 12_求職者用URL
    SK_URL = models.CharField(max_length=20, null=True)
    # 13_求職者氏名
    SK_NAME = models.CharField(max_length=30, null=True)
    # 14_求職者メールアドレス
    SK_MAILADDRESS = models.CharField(max_length=50, null=True)
    # 15_求職者送付日時
    SK_SEND_DATE = models.DateTimeField(auto_now_add=True)
    # 16_求職者受領日時
    SK_ACCEPT_DATE = models.CharField(max_length=255, null=True)
    # 17_求職者コメント
    SK_COMMENT = models.CharField(max_length=255, null=True)
    # 18_就業施設名
    FCL_NAME = models.CharField(max_length=50, null=True)
    # 19_勤務先郵便番号
    FCL_POSTALNUMBER = models.CharField(max_length=10, null=True)
    # 20_勤務先住所
    FCL_ADDRESS = models.CharField(max_length=100, null=True)
    # 21_入職日
    ENTERING_DAY = models.DateTimeField(null=True)
    # 22_勤務形態
    WORL_STYLE = models.CharField(max_length=50, null=True)
    # 23_期間の定め（有無）
    PERIOD_Y_OR_N = models.BooleanField(null=True)
    # 24_開始年月日
    START_DATE = models.DateTimeField(null=True)
    # 25_試用期間（有無）
    PROBATION_PERIOD_Y_OR_N = models.BooleanField(null=True)
    # 26_試用期間（月）
    PROBATION_PERIOD_MONTH = models.CharField(max_length=2, null=True)
    # 27_就業開始時間１
    WORK_START_TIME_1 = models.TimeField(null=True)
    # 28_就業終了時間１
    WORK_END_TIME_1 = models.TimeField(null=True)
    # 29_休憩時間１
    BREAK_TIME_1 = models.IntegerField(null=True)
    # 30_就業開始時間２
    WORK_START_TIME_2 = models.TimeField(null=True)
    # 31_就業終了時間２
    WORK_END_TIME_2 = models.TimeField(null=True)
    # 32_休憩時間２
    BREAK_TIME_2 = models.IntegerField(null=True)
    # 33_就業開始時間３
    WORK_START_TIME_3 = models.TimeField(null=True)
    # 34_就業終了時間３
    WORK_END_TIME_3 = models.TimeField(null=True)
    # 35_休憩時間３
    BREAK_TIME_3 = models.IntegerField(null=True)
    # 36_就業開始時間４
    WORK_START_TIME_4 = models.TimeField(null=True)
    # 37_就業終了時間４
    WORK_END_TIME_4 = models.TimeField(null=True)
    # 38_休憩時間４
    BREAK_TIME_4 = models.IntegerField(null=True)
    # 39_残業（有無）
    OVER_TIME = models.BooleanField(null=True)
    # 40_勤務日
    WORKING_DATE = models.CharField(max_length=20, null=True)
    # 41_仕事内容
    WORK_DESCRIPTION = models.CharField(max_length=255, null=True)
    # 42_基本給
    BASE_SALARY = models.IntegerField(null=True)
    # 43_その他手当１（名称）
    ALLOWANCE_NAME_1 = models.CharField(max_length=30, null=True)
    # 44_その他手当１（金額）
    ALLOWANCE_1 = models.IntegerField(null=True)
    # 45_その他手当１（補足）
    ALLOWANCE_SUPPLEMENT_1 = models.CharField(max_length=100, null=True)
    # 46_その他手当２（名称）
    ALLOWANCE_NAME_2 = models.CharField(max_length=30, null=True)
    # 47_その他手当２（金額）
    ALLOWANCE_2 = models.IntegerField(null=True)
    # 48_その他手当２（補足）
    ALLOWANCE_SUPPLEMENT_2 = models.CharField(max_length=100, null=True)
    # 49_その他手当３（名称）
    ALLOWANCE_NAME_3 = models.CharField(max_length=30, null=True)
    # 50_その他手当３（金額）
    ALLOWANCE_3 = models.IntegerField(null=True)
    # 51_その他手当３（補足）
    ALLOWANCE_SUPPLEMENT_3 = models.CharField(max_length=100, null=True)
    # 52_その他手当４（名称）
    ALLOWANCE_NAME_4 = models.CharField(max_length=30, null=True)
    # 53_その他手当４（金額）
    ALLOWANCE_4 = models.IntegerField(null=True)
    # 54_その他手当４（補足）
    ALLOWANCE_SUPPLEMENT_4 = models.CharField(max_length=100, null=True)
    # 55_その他手当５（名称）
    ALLOWANCE_NAME_5 = models.CharField(max_length=30, null=True)
    # 56_その他手当５（金額）
    ALLOWANCE_5 = models.IntegerField(null=True)
    # 57_その他手当５（補足）
    ALLOWANCE_SUPPLEMENT_5 = models.CharField(max_length=100, null=True)
    # 58_賞与（有無）
    BONUS = models.BooleanField(null=True)
    # 59_賞与（詳細）
    BONUS_DETAIL = models.CharField(max_length=255, null=True)
    # 60_昇給（有無）
    SALARY_RAISE_Y_OR_N = models.BooleanField(null=True)
    # 61_退職金（有無）
    RETIREMENT_ALLOWANCE_Y_OR_N = models.BooleanField(null=True)
    # 62_賃金締切日
    SALARY_CUT_OFF_DATE = models.CharField(max_length=20, null=True)
    # 63_賃金支払日
    SALARY_PAY_DATE = models.CharField(max_length=20, null=True)
    # 64_健康保険（有無）
    HEALTH_INSURANCE_Y_OR_N = models.BooleanField(null=True)
    # 65_厚生年金（有無）
    WALFARE_PENSION_Y_OR_N = models.BooleanField(null=True)
    # 66_労災保険（有無）
    COMPENSATION_INSURANCE_Y_OR_N = models.BooleanField(null=True)
    # 67_雇用保険（有無）
    EMPLOYEE_INSURANCE_Y_OR_N = models.BooleanField(null=True)
    # 68_休日
    HOLIDAY = models.CharField(max_length=255, null=True)
    # 69_受動喫煙防止措置
    PS_KBN = models.CharField(max_length=2, null=True)
    # 70_備考欄
    NOTES = models.CharField(max_length=255, null=True)
    # 71_受諾期限
    ACCEPT_DEADLINE_DATE = models.DateTimeField(null=True)
    # 72_労働条件通知書署名
    SIGNATURE = models.CharField(max_length=20, null=True)
    # 73_求職者郵便番号
    SK_POSTALNUMBER = models.CharField(max_length=10, null=True)
    # 74_求職者住所
    SK_ADDRESS = models.CharField(max_length=100, null=True)
    # 75_誓約書署名
    SEIYAKU_SIGNATURE = models.CharField(max_length=20, null=True)
    # 76_変更担当者
    UPD_USERNAME = models.CharField(max_length=20, null=True)
    # 77_変更日時
    UPD_DATE = models.DateTimeField(auto_now_add=True)
    # 78_更新カウンタ
    UPD_COUNT = models.IntegerField(null=True)
    # 79_登録担当者
    ADD_USERNAME = models.CharField(max_length=20)
    # 80_登録日時
    ADD_DATE = models.DateTimeField(auto_now_add=True)
    # 81_登録区分
    ENT_KBN = models.CharField(max_length=1, default=1, null=True)

    def __str__(self):
        return str(self.ID)


#求職者情報テーブル
class JOB_SEEKER_INFO(models.Model):
    # 1_求職者情報ID(自動PK)
    SEEKER_ID = models.AutoField(primary_key=True, editable=False)
    # 2_労通ID（外部キー）
    SK_ROUTSU_ID = models.ForeignKey('ROUTSU_TBL',to_field='ID',on_delete=models.CASCADE,null=True)
    # 3_経験年数
    YEARS_OF_EXPERIENCE = models.IntegerField(null=True)
    # 4_業種（業種マスタから取得）
    TYPE_OF_BUSINESS = models.CharField(max_length=2, null=True)
    # 5_職種（職種マスタから取得）
    OCCUPATION = models.CharField(max_length=2, null=True)
    # 6_保有資格（資格マスタから取得）
    HOLDING_QUALIFICATION = models.CharField(max_length=2, null=True)
    # 7_変更担当者
    UPD_USERNAME = models.CharField(max_length=20, null=True)
    # 8_変更日時
    UPD_DATE = models.DateTimeField(auto_now_add=True)
    # 9_更新カウンタ
    UPD_COUNT = models.IntegerField(null=True)
    # 10_登録担当者
    ADD_USERNAME = models.CharField(max_length=20)
    # 11_登録日時
    ADD_DATE = models.DateTimeField(auto_now_add=True)
    # 12_登録区分
    ENT_KBN = models.CharField(max_length=1, default=1, null=True)

    #管理画面に表示されるモデル内のレコードを判別するための、名前（文字列）を定義する
    def __str__(self):
        return str(self.PARE_DOC_ID)
