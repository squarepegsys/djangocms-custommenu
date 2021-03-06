# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-04 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_custommenu', '0008_auto_20180220_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMenu',
            fields=[
                ('menu_type', models.CharField(choices=[(b'show_menu', 'Show menu'), (b'show_menu_below_id', 'Show menu below page'), (b'show_sub_menu', 'Show sub menu')], default=b'show_menu', help_text='Check documentation here http://docs.django-cms.org/en/release-3.4.x/reference/navigation.html', max_length=255, verbose_name='Menu type')),
                ('template', models.CharField(choices=[(b'default', 'Default'), (b'zoom-masonry', 'Zoom masonry'), (b'dropdown-image', 'Dropdown image'), (b'footer-menu-item', 'Footer menu item')], default=b'default', max_length=255, verbose_name='Template')),
                ('start_level', models.PositiveSmallIntegerField(default=0, help_text='From which level the navigation should be rendered.', verbose_name='Start level')),
                ('end_level', models.PositiveSmallIntegerField(default=100, help_text='At which level the navigation tree should stop.', verbose_name='End level')),
                ('extra_inactive', models.PositiveSmallIntegerField(default=0, help_text='How many levels of navigation should be displayed if a node is not a direct ancestor or descendant of the current active node.', verbose_name='Extra inactive')),
                ('extra_active', models.PositiveSmallIntegerField(default=100, help_text='How many levels of descendants of the currently active node should be displayed.', verbose_name='Extra active')),
                ('levels', models.PositiveSmallIntegerField(default=100, help_text='At which level the navigation tree should stop.', verbose_name='Levels')),
                ('root_level', models.PositiveSmallIntegerField(blank=True, help_text='At what level, if any, the menu should have its root.', null=True, verbose_name='Root level')),
                ('nephews', models.PositiveSmallIntegerField(default=100, help_text='How many levels of nephews (children of siblings) are shown.', verbose_name='Nephews')),
                ('classes', models.CharField(blank=True, help_text='Comma separated list of classes to add to the element.', max_length=255)),
                ('configuration', models.TextField(blank=True, help_text='Custom configuration.')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_custommenu_custommenu', serialize=False, to='cms.CMSPlugin')),
                ('root_page', models.ForeignKey(blank=True, help_text='Menu tree starts from this page. Warning: selected page MUST have its ID set in advanced settings.', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='Root page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
