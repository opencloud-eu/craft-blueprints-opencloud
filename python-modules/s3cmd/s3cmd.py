# -*- coding: utf-8 -*-
import info
import utils
from CraftCore import CraftCore
from Package.PipPackageBase import PipPackageBase


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = ""
        self.description = "Official s3cmd repo -- Command line tool for managing S3 compatible storage services (including Amazon S3 and CloudFront)."
        self.defaultTarget = "master"

    def setDependencies(self):
        if not CraftCore.compiler.compiler.isMSVC:
            self.buildDependencies["python-modules/setuptools"] = None
        self.runtimeDependencies["python-modules/python-dateutil"] = None
        self.runtimeDependencies["python-modules/python-magic"] = None


class Package(PipPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def install(self):
        if not super().install():
            return False
        return self.createMacOSPipShims(["s3cmd"])

    def postInstall(self):
        if CraftCore.compiler.platform.isWindows:
            if not utils.createShim(
                    self.installDir() / f"bin/s3cmd{CraftCore.compiler.platform.executableSuffix}",
                    f"python3{CraftCore.compiler.platform.executableSuffix}",
                    args= [f"{self.installPrefix()}/bin/Scripts/s3cmd"],
                    useAbsolutePath=False,
            ):
                return False
        return super().postInstall()
