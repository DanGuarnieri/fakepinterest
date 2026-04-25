from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ProjetoFakePinterest.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao = PasswordField("Confirmação da Senha", validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')
    
    def validate_email(self, email):
        email_normalizado = email.data.lower()
        usuario = Usuario.query.filter_by(email=email_normalizado).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')
            


    
class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
    def validate_email(self, email):
        email_normalizado = email.data.lower()
        usuario = Usuario.query.filter_by(email=email_normalizado).first()
        if not usuario:
            raise ValidationError('Usuário não cadastrado. Crie uma conta para continuar.')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['png','jpg', 'jpeg'])])
    
    botao_submit_editarperfil  = SubmitField('Confirmar Edição')
   
    def validate_email(self, email):
        #verificar se o cara mudou de email
        if current_user.email != email.data.lower():
            email_normalizado = email.data.lower()
            usuario = Usuario.query.filter_by(email=email_normalizado).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este E-mail. Cadastre-se com outro e-mail.')
            

class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_submit = SubmitField('Enviar')
    