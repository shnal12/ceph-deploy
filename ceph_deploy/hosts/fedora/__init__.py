import mon
from ceph_deploy.hosts.centos import pkg
from install import install, mirror_install
from uninstall import uninstall

# Allow to set some information about this distro
#

distro = None
release = None
codename = None
