from django import forms


class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(
        label="令和何年？", min_value=1, help_text="例: 1 → 2019年"
    )


class BMIForm(forms.Form):
    height = forms.FloatField(
        label="身長(cm)",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "例：170"}),
    )
    weight = forms.FloatField(
        label="体重(kg)",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "例：60"}),
    )


class WarikanForm(forms.Form):
    total = forms.IntegerField(
        label="合計金額（円）",
        min_value=1,
        widget=forms.NumberInput(attrs={"placeholder": "例：12000"}),
    )
    people = forms.IntegerField(
        label="人数",
        min_value=1,
        widget=forms.NumberInput(attrs={"placeholder": "例：4"}),
    )


class ChokinForm(forms.Form):
    monthly_saving = forms.IntegerField(label="毎月の貯金額（円）", min_value=0)
    years = forms.IntegerField(label="貯金年数（年）", min_value=1)


class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="1つ目の数字")
    operator = forms.ChoiceField(
        label="演算の種類",
        choices=[
            ("+", "足し算（＋）"),
            ("-", "引き算（−）"),
            ("*", "掛け算（×）"),
            ("/", "割り算（÷）"),
        ],
    )
    num2 = forms.FloatField(label="2つ目の数字")
