# SPDX-License-Identifier: BSD-2-Clause
# Copyright Sphinx Confluence Builder Contributors (AUTHORS)

from tests.lib.parse import parse
from tests.lib.testcase import ConfluenceTestCase
from tests.lib.testcase import setup_builder
from tests.lib.testcase import setup_editor


class TestConfluenceRstTargets(ConfluenceTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.dataset = cls.datasets / 'rst' / 'targets'

    @setup_builder('confluence')
    def test_storage_rst_targets_defaults(self):
        out_dir = self.build(self.dataset)

        with parse('index', out_dir) as data:
            # sanity check anchor creation
            anchor_tag = data.find('ac:structured-macro')
            self.assertIsNotNone(anchor_tag)
            self.assertTrue(anchor_tag.has_attr('ac:name'))
            self.assertEqual(anchor_tag['ac:name'], 'anchor')

            anchor_param = anchor_tag.find('ac:parameter', recursive=False)
            self.assertIsNotNone(anchor_param)
            self.assertEqual(anchor_param.text, 'inline-target')

            # before and after text
            before_data = anchor_tag.previous_sibling.strip()
            self.assertEqual(before_data, 'An')

            trailing_data = anchor_tag.next_sibling .strip()
            self.assertEqual(trailing_data, 'inline target example.')

    @setup_builder('confluence')
    @setup_editor('v2')
    def test_storage_rst_targets_v2(self):
        out_dir = self.build(self.dataset)

        with parse('index', out_dir) as data:
            # sanity check anchor creation
            anchor_tag = data.find('ac:structured-macro')
            self.assertIsNotNone(anchor_tag)
            self.assertTrue(anchor_tag.has_attr('ac:name'))
            self.assertEqual(anchor_tag['ac:name'], 'anchor')

            anchor_param = anchor_tag.find('ac:parameter', recursive=False)
            self.assertIsNotNone(anchor_param)
            self.assertEqual(anchor_param.text, 'inline-target')

            # before text
            before_data = anchor_tag.previous_sibling.strip()
            self.assertEqual(before_data, 'An')
