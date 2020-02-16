# Generated by Django 2.2.9 on 2020-02-16 08:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0013_faqpage_faqs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqpage',
            name='faqs',
            field=wagtail.core.fields.StreamField([('faqs', wagtail.core.blocks.StructBlock([('category', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('questions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', max_length='200', required=True)), ('content', wagtail.core.blocks.RichTextBlock())])))]))], blank=True, null=True),
        ),
    ]