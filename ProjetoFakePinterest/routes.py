from flask import render_template, request, redirect, flash, url_for
from ProjetoFakePinterest.forms import FormCriarConta, FormLogin, FormFoto
from ProjetoFakePinterest import app, database, bcrypt
from ProjetoFakePinterest.models import Usuario, Foto
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlparse
import secrets
import os
from PIL import Image
from werkzeug.utils import secure_filename


# ---------------- HOME / LOGIN ---------------- #
@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(
            email=form_login.email.data.lower()
        ).first()

        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)

            flash(f"Login feito com sucesso: {form_login.email.data}", 'alert-success')

            # 🔒 Segurança no redirect
            par_next = request.args.get('next')
            if par_next and urlparse(par_next).netloc == "":
                return redirect(par_next)

            return redirect(url_for('feed'))
        else:
            form_login.senha.errors.append('E-mail ou senha inválidos')
    return render_template('homepage.html', form_login=form_login)


# ---------------- CRIAR CONTA ---------------- #
@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criar_conta = FormCriarConta()

    if form_criar_conta.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(
            form_criar_conta.senha.data
        ).decode("utf-8")

        usuario = Usuario(
            username=form_criar_conta.username.data,
            email=form_criar_conta.email.data.lower(),
            senha=senha_cript
        )

        database.session.add(usuario)
        database.session.commit()

        login_user(usuario, remember=True)

        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=form_criar_conta)


# ---------------- PERFIL ---------------- #
@app.route('/perfil/<id_usuario>', methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    usuario = Usuario.query.get_or_404(int(id_usuario))

    # 🔒 Só o próprio usuário pode postar foto
    if usuario.id == current_user.id:
        form_foto = FormFoto()

        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data

            # Nome seguro
            nome_original = secure_filename(arquivo.filename)
            extensao = os.path.splitext(nome_original)[1]

            # Nome único
            nome_unico = secrets.token_hex(8) + extensao

            caminho = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                app.config["UPLOAD_FOLDER"],
                nome_unico
            )

            # Salvar imagem
            arquivo.save(caminho)

            # 🔧 Redimensionar imagem
            try:
                img = Image.open(caminho)
                img.thumbnail((500, 500))
                img.save(caminho)
            except Exception:
                pass  # evita quebrar caso dê erro na imagem

            # Salvar no banco
            foto = Foto(imagem=nome_unico, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()

            flash("Foto enviada com sucesso!", "alert-success")

        return render_template(
            'perfil.html',
            usuario=usuario,
            form=form_foto
        )

    # 👀 Visualizando perfil de outro usuário
    return render_template(
        'perfil.html',
        usuario=usuario,
        form=None
    )


# ---------------- LOGOUT ---------------- #
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da sua conta.", "alert-info")
    return redirect(url_for("homepage"))


# ---------------- FEED ---------------- #
@app.route("/feed", methods=["GET"])
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao).all()
    return render_template("feed.html", fotos=fotos)