# Generated by Django 2.1.7 on 2020-10-14 11:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_sign_up', models.CharField(blank=True, max_length=500)),
                ('listener_sign_up', models.CharField(blank=True, max_length=500)),
                ('creator_update', models.CharField(blank=True, max_length=500)),
                ('listener_update', models.CharField(blank=True, max_length=500)),
                ('creator_upload', models.CharField(blank=True, max_length=500)),
                ('creator_upload_update', models.CharField(blank=True, max_length=500)),
                ('creator_activity', models.CharField(blank=True, max_length=500)),
                ('listener_activity', models.CharField(blank=True, max_length=500)),
                ('playlist', models.CharField(blank=True, max_length=500)),
                ('playlist_update', models.CharField(blank=True, max_length=500)),
                ('follow_activity', models.CharField(blank=True, max_length=500)),
                ('favorite_activity', models.CharField(blank=True, max_length=500)),
                ('friend_activity', models.CharField(blank=True, max_length=500)),
                ('creator_auth', models.CharField(blank=True, max_length=500)),
                ('listener_auth', models.CharField(blank=True, max_length=500)),
                ('approved', models.CharField(blank=True, max_length=500)),
                ('reveiws', models.CharField(blank=True, max_length=500)),
                ('upadate', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('cover', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('artist_name', models.CharField(blank=True, max_length=150)),
                ('features', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('creator_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creator_name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('username', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('town', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reveiwed_by_admin', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CreatorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_upload', models.CharField(blank=True, max_length=500)),
                ('my_upload_update', models.CharField(blank=True, max_length=500)),
                ('my_followers', models.CharField(blank=True, max_length=500)),
                ('my_followers_update', models.CharField(blank=True, max_length=500)),
                ('playlist_featured', models.CharField(blank=True, max_length=500)),
                ('playlist_featured_update', models.CharField(blank=True, max_length=500)),
                ('my_favorites', models.CharField(blank=True, max_length=500)),
                ('my_favorites_update', models.CharField(blank=True, max_length=500)),
                ('milestone_stats', models.CharField(blank=True, max_length=500)),
                ('creator_auth', models.CharField(blank=True, max_length=500)),
                ('creator_update', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
                ('album_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Creator')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('listener_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('display_name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reveiwed_by_admin', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ListenerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_playlists', models.CharField(blank=True, max_length=500)),
                ('my_playlists_update', models.CharField(blank=True, max_length=500)),
                ('my_followers', models.CharField(blank=True, max_length=500)),
                ('my_followers_update', models.CharField(blank=True, max_length=500)),
                ('my_favorites', models.CharField(blank=True, max_length=500)),
                ('my_favorites_update', models.CharField(blank=True, max_length=500)),
                ('followed', models.CharField(blank=True, max_length=500)),
                ('followed_update', models.CharField(blank=True, max_length=500)),
                ('my_friends', models.CharField(blank=True, max_length=500)),
                ('my_friends_update', models.CharField(blank=True, max_length=500)),
                ('milestone_stats', models.CharField(blank=True, max_length=500)),
                ('listener_auth', models.CharField(blank=True, max_length=500)),
                ('listener_update', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Creator')),
                ('listener_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Listener')),
            ],
        ),
        migrations.CreateModel(
            name='MyGenericModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theFile', models.FileField(blank=True, default='aa', upload_to='media/files/')),
                ('firebase_id_token', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('publisher_id', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('cover', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('podcast_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('duration', models.CharField(blank=True, max_length=50)),
                ('cover', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('artist_name', models.CharField(blank=True, max_length=150)),
                ('features', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=75, unique=True)),
                ('property_value', models.CharField(blank=True, max_length=254, null=True)),
                ('property_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('property_group', models.CharField(choices=[('APP_CONF', 'App Setting'), ('GENERAL_CONF', 'General Setting'), ('PROHIBITED_USER_NAME', 'Prohibited User Name'), ('PROHIBITED_USER_EMAIL', 'Prohibited User Email'), ('OTHERS', 'Other')], default='APPSETTING', max_length=75)),
            ],
            options={
                'verbose_name': 'Site Config',
                'verbose_name_plural': 'Site Configs',
                'db_table': 'dev_site_config',
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_streamed', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='StreamDetail',
            fields=[
                ('stream_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stream_location', models.CharField(blank=True, max_length=150)),
                ('count', models.CharField(blank=True, max_length=50)),
                ('listener_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Listener')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('duration', models.CharField(blank=True, max_length=50)),
                ('cover', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('artist_name', models.CharField(blank=True, max_length=150)),
                ('features', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('upload_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file_url', models.CharField(blank=True, max_length=150)),
                ('reveiwed_by_admin', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='track_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Upload'),
        ),
        migrations.AddField(
            model_name='track',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Creator'),
        ),
        migrations.AddField(
            model_name='stream',
            name='stream_detailed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.StreamDetail'),
        ),
        migrations.AddField(
            model_name='stream',
            name='upload_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Upload'),
        ),
        migrations.AlterIndexTogether(
            name='siteconfig',
            index_together={('property_group',)},
        ),
        migrations.AddField(
            model_name='podcast',
            name='podcast_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Upload'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Creator'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='bl.Upload'),
        ),
        migrations.AddField(
            model_name='friend',
            name='friend_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Listener'),
        ),
        migrations.AddField(
            model_name='follow',
            name='listener_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Listener'),
        ),
        migrations.AddField(
            model_name='follow',
            name='playlist_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Playlist'),
        ),
        migrations.AddField(
            model_name='follow',
            name='podcast_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Podcast'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='listener_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Listener'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='playlist_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Playlist'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='podcast_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Podcast'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='track_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Track'),
        ),
        migrations.AddField(
            model_name='creatorlog',
            name='listener_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Listener'),
        ),
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.ManyToManyField(to='bl.Track'),
        ),
        migrations.AddField(
            model_name='album',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl.Creator'),
        ),
        migrations.AddField(
            model_name='adminlog',
            name='creator_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Creator'),
        ),
        migrations.AddField(
            model_name='adminlog',
            name='listener_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bl.Listener'),
        ),
    ]