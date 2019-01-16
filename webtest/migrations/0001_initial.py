# Generated by Django 2.1.1 on 2019-01-09 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webcase_models', models.CharField(max_length=250, verbose_name='所属模块')),
                ('webcasename', models.CharField(max_length=50, verbose_name='测试用例名称')),
                ('webcasedesc', models.CharField(max_length=50, verbose_name='步骤描述')),
                ('webteststep', models.CharField(max_length=200, verbose_name='测试步骤')),
                ('webcase_charger', models.CharField(max_length=200, verbose_name='负责人')),
                ('creat_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'web测试步骤',
                'verbose_name_plural': 'web测试步骤',
            },
        ),
        migrations.CreateModel(
            name='Webcase_keywords',
            fields=[
                ('keyword_id', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('library', models.CharField(max_length=50, verbose_name='库名')),
                ('keyword', models.CharField(max_length=200, verbose_name='关键字')),
                ('parameter', models.CharField(max_length=200, verbose_name='参数')),
                ('comment', models.CharField(max_length=200, verbose_name='参数2')),
            ],
        ),
        migrations.CreateModel(
            name='Webcasestep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webtestlocation', models.CharField(choices=[('id', 'id'), ('xpath', 'xpath'), ('css', 'css'), ('图片', '图片'), ('name', 'name'), ('link', 'link'), ('classname', 'classname'), ('tagname', 'tagname')], default='0', max_length=200, verbose_name='定位方式')),
                ('webfindmethod', models.CharField(blank=True, max_length=200, null=True, verbose_name='方法|操作')),
                ('webkwargesone', models.CharField(blank=True, max_length=200, verbose_name='参数1')),
                ('webkwargestwo', models.CharField(blank=True, max_length=200, verbose_name='参数2')),
                ('webkwargesthree', models.CharField(blank=True, max_length=200, verbose_name='参数3')),
                ('webkwargesfour', models.CharField(blank=True, max_length=200, verbose_name='参数4')),
                ('webassertdata', models.CharField(blank=True, max_length=200, verbose_name='验证数据')),
                ('webtestresult', models.CharField(blank=True, max_length=50, verbose_name='测试结果')),
                ('webcomments', models.CharField(blank=True, max_length=200, verbose_name='备注')),
                ('Webcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Webcasestep.webcasename+', to='webtest.Webcase')),
            ],
        ),
        migrations.CreateModel(
            name='webtest_task',
            fields=[
                ('task_id', models.AutoField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('task_modelname', models.CharField(max_length=100, verbose_name='模块名称')),
                ('task_casename', models.CharField(max_length=200, verbose_name='任务用例名称')),
                ('task_stepdesc', models.CharField(max_length=100, null=True, verbose_name='任务步骤描述')),
                ('task_status', models.CharField(default=True, max_length=200, verbose_name='状态')),
                ('task_retry', models.CharField(max_length=10, verbose_name='失败重跑次数')),
                ('task_result', models.CharField(max_length=20, verbose_name='测试结果')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('case_id', models.CharField(max_length=200, null=True, verbose_name='测试用例名称的ID')),
            ],
        ),
    ]
