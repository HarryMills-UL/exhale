# -*- coding: utf8 -*-
########################################################################################
# This file is part of exhale.  Copyright (c) 2017-2019, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################
"""
Tests for the ``c_maths`` project.
"""

from __future__ import unicode_literals
import os

from testing.base import ExhaleTestCase
from testing.decorators import confoverrides, no_run
from testing.hierarchies import                                       \
    class_hierarchy, compare_class_hierarchy, compare_file_hierarchy, \
    directory, file, file_hierarchy, function, parameters


class CMathsTests(ExhaleTestCase):
    """
    Primary test class for project ``c_maths``.
    """

    test_project = "c_maths"
    """.. testproject:: c_maths"""

    @confoverrides(exhale_args={"containmentFolder": "./alt_api"})
    def test_alt_out(self):
        """
        Test ``"./alt_api"`` rather than default ``"./api"`` as ``"containmentFolder"``.
        """
        self.checkRequiredConfigs()

    def test_hierarchies(self):
        """Verify the class and file hierarchies."""
        # verify the file hierarchy and file declaration relationships
        file_hierarchy_dict = {
            directory("include"): {
                file("c_maths.h"): {
                    function("int", "cm_add"): parameters("int", "int"),
                    function("int", "cm_sub"): parameters("int", "int")
                }
            }
        }
        compare_file_hierarchy(self, file_hierarchy(file_hierarchy_dict))
        compare_class_hierarchy(self, class_hierarchy({}))


@no_run
class CMathsTestsNoRun(ExhaleTestCase):
    """
    Secondary test case for project ``c_maths``.

    A :func:`testing.decorators.no_run` decorated test class.
    """

    test_project = "c_maths"
    """.. testproject:: c_maths"""

    def test_classwide_no_run(self):
        """
        Verify that the default ``"./api"`` folder is indeed **not** generated.
        """
        exhale_args = self.app.config.exhale_args
        containmentFolder = exhale_args["containmentFolder"]
        self.assertEqual(containmentFolder, "./api")

        # check that nothing has been generated
        containmentFolder = self.getAbsContainmentFolder()
        self.assertFalse(
            os.path.exists(containmentFolder),
            "Folder [{containmentFolder}] should not exist!".format(
                containmentFolder=containmentFolder
            )
        )
