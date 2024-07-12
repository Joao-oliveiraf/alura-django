from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de usuário",
        max_length = 100,
        required = True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Joao123"
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        max_length = 70,
        required = True,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Nome de usuário",
        max_length = 100,
        required = True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Joao123"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Ex: joaodasilva@gmail.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    senha_2 = forms.CharField(
    label="Confirme sua senha",
    required=True,
    max_length=70,
    show_hidden_initial=True,
    widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha novamente'
            }
        )
    )