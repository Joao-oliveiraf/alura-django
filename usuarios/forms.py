from django import forms
from django.contrib.auth.models import User

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
    def clean_nome_cadastro(self): # clean no inicio referencia pro django que é uma validação
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Nome de usuário não pode conter espaços')
            elif User.objects.filter(username=nome).exists():
                raise forms.ValidationError('Nome de usuário em uso')
            else:
                return nome
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não conferem')
            else:
                return senha_2
