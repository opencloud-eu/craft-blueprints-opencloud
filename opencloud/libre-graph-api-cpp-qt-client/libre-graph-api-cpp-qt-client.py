import info
from Utils import CraftHash


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["1.0.6"]:
            self.targets[ver] = f"https://github.com/opencloud-eu/libre-graph-api-cpp-qt-client/archive/refs/tags/v{ver}.tar.gz"
            self.targetConfigurePath[ver] = "client"
            self.targetInstSrc[ver] = f"libre-graph-api-cpp-qt-client-{ver}"
        self.targetDigests["1.0.6"] = (["02a8f5efc079d022faf7bc6da6c0a646dfee96ca4d1bd505d8a6f2f1a0ef6ebc"], CraftHash.HashAlgorithm.SHA256)

        self.svnTargets["main"] = f"https://github.com/opencloud-eu/libre-graph-api-cpp-qt-client.git|main|"
        self.targetConfigurePath["main"] = "client"

        self.defaultTarget = "1.0.6"
        self.description = "Libre Graph Cloud Collaboration API - Qt bindings"

    def setDependencies(self):
        self.buildDependencies["craft/craft-blueprints-opencloud"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
