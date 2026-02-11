import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["main"] = "https://github.com/dragotin/openvfs.git|main"
        self.targetInstSrc["main"] = "openVfsFuse"
        self.defaultTarget = "main"

    def setDependencies(self):
        self.buildDependencies["libs/nlohmann-json"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
