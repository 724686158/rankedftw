# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-13 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class RunSqlPostgreOnly(migrations.RunSQL):

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == "postgresql":
            super().database_forwards(app_label, schema_editor, from_state, to_state)


class Migration(migrations.Migration):

    replaces = [
        ('main', '0001_initial'),
        ('main', '0002_remove_auto_timestamps'),
        ('main', '0003_added_min_and_max_datetime_to_ranking'),
        ('main', '0004_add_clan_support'),
        ('main', '0005_add_new_cache_ladder_and_cache_ranking_relations'),
        ('main', '0006_create_cache_ladder_links'),
        ('main', '0007_duplicate_multi_linked_caches'),
        ('main', '0008_create_cache_ranking_links'),
        ('main', '0009_recalculate_rankings_with_changed_id_on_sources'),
        ('main', '0010_remove_relations_to_cache'),
        ('main', '0011_run_archive_and_delete')
    ]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(db_index=True, max_length=256)),
                ('bid', models.IntegerField(db_index=True)),
                ('type', models.IntegerField()),
                ('region', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(db_index=True)),
                ('updated', models.DateTimeField(db_index=True)),
                ('data', models.TextField(default=None, null=True)),
                ('retry_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cache',
            },
        ),
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.IntegerField()),
                ('bid', models.IntegerField()),
                ('strangeness', models.IntegerField(default=1)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(db_index=True)),
                ('mode', models.IntegerField(default=-1)),
                ('league', models.IntegerField(default=-1)),
                ('version', models.IntegerField(default=-1)),
                ('first_join', models.DateTimeField(null=True)),
                ('last_join', models.DateTimeField(null=True)),
                ('max_points', models.FloatField(null=True)),
                ('member_count', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'ladder',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.IntegerField()),
                ('bid', models.IntegerField()),
                ('realm', models.IntegerField()),
                ('name', models.CharField(db_index=True, max_length=12)),
                ('tag', models.CharField(db_index=True, max_length=6)),
                ('clan', models.CharField(db_index=True, max_length=32)),
                ('mode', models.IntegerField(null=True)),
                ('league', models.IntegerField(null=True)),
                ('race', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('data_time', models.DateTimeField(db_index=True)),
                ('min_data_time', models.DateTimeField()),
                ('max_data_time', models.DateTimeField()),
                ('status', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'ranking',
            },
        ),
        migrations.CreateModel(
            name='RankingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField()),
                ('data', models.BinaryField(default=None, null=True)),
                ('ranking', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ranking_data', to='main.Ranking')),
            ],
            options={
                'db_table': 'ranking_data',
            },
        ),
        migrations.CreateModel(
            name='RankingStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField()),
                ('data', models.TextField(default=None, null=True)),
                ('ranking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ranking')),
            ],
            options={
                'db_table': 'ranking_stats',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('year', models.IntegerField()),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('version', models.IntegerField()),
            ],
            options={
                'db_table': 'season',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.IntegerField()),
                ('mode', models.IntegerField()),
                ('version', models.IntegerField(null=True)),
                ('league', models.IntegerField()),
                ('race0', models.IntegerField(default=-1)),
                ('race1', models.IntegerField(default=-1)),
                ('race2', models.IntegerField(default=-1)),
                ('race3', models.IntegerField(default=-1)),
                ('member0', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Player')),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Player')),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Player')),
                ('member3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Player')),
                ('season', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Season')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.AddField(
            model_name='ranking',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Season'),
        ),
        migrations.AddField(
            model_name='player',
            name='season',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Season'),
        ),
        migrations.AddField(
            model_name='ladder',
            name='season',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Season'),
        ),
        migrations.AddField(
            model_name='cache',
            name='ladder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sources', to='main.Ladder'),
        ),
        migrations.AddField(
            model_name='cache',
            name='ranking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sources', to='main.Ranking'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('member0', 'member1', 'member2', 'member3', 'mode')]),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('bid', 'region', 'realm')]),
        ),
        migrations.AlterUniqueTogether(
            name='ladder',
            unique_together=set([('region', 'bid')]),
        ),
        migrations.AlterIndexTogether(
            name='cache',
            index_together=set([('region', 'id')]),
        ),
        RunSqlPostgreOnly("ALTER TABLE ranking_data ALTER COLUMN data SET STORAGE EXTERNAL;"),
        RunSqlPostgreOnly("CREATE INDEX player_name_upper_like ON player ((upper(name)) varchar_pattern_ops);"),
        RunSqlPostgreOnly("CREATE INDEX player_clan_upper_like ON player ((upper(clan)) varchar_pattern_ops);"),
        RunSqlPostgreOnly("CREATE INDEX player_tag_upper_like ON player ((upper(tag)) varchar_pattern_ops);"),
        # RunSqlPostgreOnly("DROP INDEX player_name_45435349_like;"),
        # RunSqlPostgreOnly("DROP INDEX player_clan_4f5b8669_like;"),
        # RunSqlPostgreOnly("DROP INDEX player_tag_09348bde_like;"),
        # Other unused indices have been dropped in prod as well.
    ]
