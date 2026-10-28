# -*- coding: utf-8 -*-
import info
from Package.PipPackageBase import PipPackageBase


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = ""
        self.description = "Extensions to the standard Python datetime module"
        self.defaultTarget = "master"

    def setDependencies(self):
        self.runtimeDependencies["python-modules/six"] = None
        self.runtimeDependencies["python-modules/tzdata"] = None
        self.buildDependencies["python-modules/setuptools-scm"] = None


class Package(PipPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
