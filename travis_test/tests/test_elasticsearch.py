# -*- coding: utf-8 -*-

from pytest_dbfixtures import factories

es_proc = factories.elasticsearch_proc(port=9202, index_store_type='')
elasticsearch = factories.elasticsearch('es_proc')


def test_index_creation(elasticsearch):
    """Tests if index creation via elasticsearch fixture succeeds"""
    name = 'mytestindex'
    elasticsearch.indices.create(index=name)
    assert name in elasticsearch.indices.get_settings().keys()
