# Generated by Django 2.0.5 on 2018-10-31 17:57

from django.conf import settings
import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("taggit", "0002_auto_20150616_2121"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name="ConfigurationClass",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="ConfigurationParameter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("raw_value", models.TextField()),
                (
                    "string_value",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("integer_value", models.IntegerField(blank=True, null=True)),
                ("float_value", models.FloatField(blank=True, null=True)),
                ("boolean_value", models.NullBooleanField()),
                (
                    "configuration_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parameters",
                        related_query_name="parameter",
                        to="core.ConfigurationClass",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Environment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Fact",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="FactRule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "operator",
                    models.CharField(
                        choices=[
                            ("=", "="),
                            ("!=", "!="),
                            ("~", "~"),
                            ("!~", "!~"),
                            (">", ">"),
                            (">=", ">="),
                            ("<", "<"),
                            ("<=", "<="),
                        ],
                        default="=",
                        max_length=3,
                    ),
                ),
                ("value", models.CharField(max_length=255)),
                (
                    "fact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rules",
                        related_query_name="rule",
                        to="core.Fact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MasterZone",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("ca_cert", models.FileField(null=True, upload_to="")),
                ("signed_cert", models.FileField(null=True, upload_to="")),
                ("private_key", models.FileField(null=True, upload_to="")),
            ],
            options={"permissions": (("has_access", "Has access to MasterZone"),)},
        ),
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("certname", models.CharField(max_length=255)),
                (
                    "master_zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nodes",
                        related_query_name="node",
                        to="core.MasterZone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Parameter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("value_type", models.CharField(default="String", max_length=255)),
                ("value_default", models.TextField(default="")),
                ("values", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PuppetClass",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "environment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        related_query_name="class",
                        to="core.Environment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("request_path", models.CharField(max_length=256)),
                ("request_method", models.CharField(max_length=10)),
                ("response_code", models.CharField(max_length=3)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        related_query_name="log",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UUIDTaggedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.UUIDField(db_index=True, verbose_name="Object id"),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="core_uuidtaggeditem_tagged_items",
                        to="contenttypes.ContentType",
                        verbose_name="Content type",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="core_uuidtaggeditem_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"verbose_name": "Tag", "verbose_name_plural": "Tags"},
        ),
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.Group",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="Rule",
            fields=[
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.Group",
                    ),
                ),
                (
                    "match_type",
                    models.CharField(
                        choices=[("ALL", "All rules"), ("ANY", "Any rules")],
                        default="ALL",
                        max_length=3,
                    ),
                ),
                ("nodes", models.ManyToManyField(to="core.Node")),
            ],
        ),
        migrations.CreateModel(
            name="Variable",
            fields=[
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.Group",
                    ),
                ),
                ("data", django.contrib.postgres.fields.hstore.HStoreField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name="parameter",
            name="puppet_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="parameters",
                related_query_name="parameter",
                to="core.PuppetClass",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="environment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                related_query_name="group",
                to="core.Environment",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="master_zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                related_query_name="group",
                to="core.MasterZone",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="matching_nodes",
            field=models.ManyToManyField(to="core.Node"),
        ),
        migrations.AddField(
            model_name="group",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="core.UUIDTaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="fact",
            name="master_zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facts",
                related_query_name="fact",
                to="core.MasterZone",
            ),
        ),
        migrations.AddField(
            model_name="environment",
            name="master_zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="environments",
                related_query_name="environment",
                to="core.MasterZone",
            ),
        ),
        migrations.AddField(
            model_name="configurationparameter",
            name="parameter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="classifications",
                related_query_name="classification",
                to="core.Parameter",
            ),
        ),
        migrations.AddField(
            model_name="configurationclass",
            name="puppet_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                related_query_name="group",
                to="core.PuppetClass",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="node", unique_together={("certname", "master_zone")}
        ),
        migrations.AddField(
            model_name="factrule",
            name="rule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="facts",
                related_query_name="fact",
                to="core.Rule",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="fact", unique_together={("name", "master_zone")}
        ),
        migrations.AddField(
            model_name="configurationclass",
            name="configuration",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="classes",
                related_query_name="class",
                to="core.Configuration",
            ),
        ),
    ]