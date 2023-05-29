# Generated by Django 4.2.1 on 2023-05-29 03:09

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
                ('id_plataforma', models.IntegerField(primary_key=True, serialize=False, verbose_name='id plataforma')),
                ('nombrePLA', models.CharField(max_length=20, verbose_name='nombre plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False, verbose_name='id pregunta')),
                ('nombreP', models.CharField(max_length=20, verbose_name='nombre pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, verbose_name='id rol')),
                ('nombreR', models.CharField(max_length=20, verbose_name='nombre rol')),
            ],
        ),
        migrations.CreateModel(
            name='tienda',
            fields=[
                ('id_tienda', models.AutoField(primary_key=True, serialize=False, verbose_name='id tienda')),
                ('nombreT', models.CharField(max_length=30, verbose_name='nombre tienda')),
                ('link', models.CharField(max_length=500, verbose_name='link tienda')),
                ('foto', models.ImageField(upload_to='foto tienda')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='id de usuario')),
                ('nombreU', models.CharField(max_length=30, verbose_name='nombre usuario')),
                ('apellido', models.CharField(max_length=30, verbose_name='apellido usuario')),
                ('rut', models.IntegerField(verbose_name='rut usario')),
                ('correo', models.CharField(max_length=40, verbose_name='correo usuario')),
                ('telefono', models.IntegerField(verbose_name='telefono usuario')),
                ('clave', models.CharField(max_length=20, verbose_name='clave usuario')),
                ('respuesta', models.CharField(max_length=20, verbose_name='respuesta usuario')),
                ('pregunta_id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.pregunta')),
                ('rol_id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.rol')),
            ],
        ),
        migrations.CreateModel(
            name='videojuego',
            fields=[
                ('id_videojuego', models.AutoField(primary_key=True, serialize=False, verbose_name='id videojuego')),
                ('nombreV', models.CharField(max_length=40, verbose_name='nombre videojuego')),
                ('descripcion', models.CharField(max_length=500, verbose_name='descripcion videojuego')),
                ('fecha_lanz', models.DateField(verbose_name='fecha lanzamiento')),
                ('trailer', models.CharField(max_length=500, verbose_name='trailer videojuego')),
                ('foto', models.ImageField(upload_to='portada videojuego')),
            ],
        ),
        migrations.CreateModel(
            name='vid_tienda',
            fields=[
                ('id_vi_tien', models.AutoField(primary_key=True, serialize=False, verbose_name='id vid_tien')),
                ('tienda_id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.tienda')),
                ('videojuego_id_videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.videojuego')),
            ],
        ),
        migrations.CreateModel(
            name='valoracion',
            fields=[
                ('id_valoracion', models.AutoField(primary_key=True, serialize=False, verbose_name='id valoracion')),
                ('puntaje', models.IntegerField(verbose_name='puntaje de valoracion')),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.usuario')),
                ('videojuego_id_videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.videojuego')),
            ],
        ),
        migrations.CreateModel(
            name='plat_video',
            fields=[
                ('id_pv', models.AutoField(primary_key=True, serialize=False, verbose_name='id plataforma videojuego')),
                ('plataforma_id_platafomra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.plataforma')),
                ('videojuego_id_videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.videojuego')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False, verbose_name='id comentario')),
                ('fecha_comentario', models.DateField(verbose_name='fecha de comentario')),
                ('comentarios', models.CharField(max_length=500, verbose_name='comentario')),
                ('tituloC', models.CharField(max_length=30, verbose_name='')),
                ('usuario_id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.usuario')),
                ('videojuego_id_videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extension.videojuego')),
            ],
        ),
    ]
