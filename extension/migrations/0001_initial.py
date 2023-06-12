# Generated by Django 4.2.1 on 2023-06-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plataforma',
            fields=[
                ('id_plataforma', models.AutoField(primary_key=True, serialize=False, verbose_name='id plataforma')),
                ('nombrePLA', models.CharField(max_length=100, verbose_name='nombre plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False, verbose_name='id pregunta')),
                ('nombreP', models.CharField(max_length=250, verbose_name='nombre pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, verbose_name='id rol')),
                ('nombreR', models.CharField(max_length=30, verbose_name='nombre rol')),
            ],
        ),
        migrations.CreateModel(
            name='videojuego',
            fields=[
                ('id_videojuego', models.AutoField(primary_key=True, serialize=False, verbose_name='id videojuego')),
                ('nombreV', models.CharField(max_length=250, verbose_name='nombre videojuego')),
                ('descripcion', models.TextField(verbose_name='descripcion videojuego')),
                ('trailer', models.TextField(verbose_name='trailer videojuego')),
                ('foto', models.ImageField(upload_to='portada_videojuego')),
                ('link', models.TextField(verbose_name='link tienda')),
                ('plataforma_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='id de usuario')),
                ('nombreU', models.CharField(max_length=50, verbose_name='nombre usuario')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido usuario')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo usuario')),
                ('telefono', models.IntegerField(verbose_name='telefono usuario')),
                ('clave', models.CharField(max_length=20, verbose_name='clave usuario')),
                ('fotoU', models.ImageField(upload_to='Foto Perfil')),
                ('fechaU', models.DateField(verbose_name='Fecha nacimiento')),
                ('respuesta', models.CharField(max_length=250, verbose_name='respuesta usuario')),
                ('pregunta_id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.pregunta')),
                ('rol_id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.rol')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False, verbose_name='id comentario')),
                ('comentarios', models.TextField(verbose_name='comentario')),
                ('tituloC', models.CharField(max_length=200, verbose_name='titulo comentario')),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.usuario')),
                ('videojuego_id_videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.videojuego')),
            ],
        ),
    ]
