puppetboard-rpm
===============

Temporarly made the centosw/RH 6 rpms online at http://www.koewacht.net/repos/puppetboard/

Spec files to build all required packages to install puppetboard from rpm.  This is only for the rhel/centos verion six.  puppetboard depends on python 2.x, ans I haven't tested it on the latest fedora.

This is a first attemp to get all python-packages into an rpm.  Most specs are taken from the epel (6.5) or centos base (6.5) src.rpms, and updated to the 'requirements.txt' form the [puppetboard github page] (https://github.com/nedap/puppetboard).

Only the python-flacs is taken from the fc20 repos.  This spec file has support for both current versions of fedora and RHEL and deriviates.

Building the packaged is best done using a clean centos6.5 vagrant box.  There is a specific order and build requirements.  I still have some conflicting versions  ...

Nexts step are done on a vagrant box as the vagrant user (never build rpms as the root user)
The next steps will not work, because the sources are not available.  As soon as i have thos working properly, I will provide a repo for the rpms ans src.rpms.  In the meantime, you can find the links to the sources in the \*.spec file and put these files in ~/rpmbuild/SOURCES)

* wget http://fedora.cu.be/epel/6/i386/epel-release-6-8.noarch.rpm (or any other mirror)
* sudo yum localinstall epel-release-6-8.noarch.rpm

* yum install rpm-build
* cd rpmbuild/SPECS

copy all spec files in this directory

* rpmbuild -ba python-markupsafe.spec
* sudo yum localinstall ../RPMS/x86_64/python-markupsafe-0.18-1.el6.x86_64.rpm
* sudo yum install python-sphinx10
* rpmbuild -ba python-jinja2.spec
* sudo yum localinstall ../RPMS/noarch/python-jinja2-2.7-1.el6.noarch.rpm
* sudo yum install python-sphinx
* rpmbuild -ba python-werkzeug.spec
* sudo yum install python-itsdangerous (correct version is in base repo)
* rpmbuild -ba python-wtforms.spec
* sudo localinstall ../RPMS/noarch/python-wtforms-1.0.4-1.el6.noarch.rpm
* rpmbuild -ba python-flask-wtf.spec
* rpmbuild -ba python-flaks.spec

* rpmbuild -ba pythin-requiresPB.spec
  In the RedHat family, the python-require unbundled the packages, providing the same functionality with multiple python-packages. (python-urlgrab3 and pythont-chardet).  This packages just undoes this and iunstalls ecverything in the python-requests packages.  If we do not do so, we get a runtime error : (from .packages import charade as chardet - ImportError: No module named packages).

* rpmbuild -ba python-pypuppetdb
* rpmbuild -ba python-puppetdb

In the puppetdb rpm, all dependencies to other rpm and there specific version are hard Required:.  For a first attemp this can be OK.  This could change in the futere (I dont know if this is good practice)


Put all the build packages in a local repo, and yust issue :


    [root@book ~]# yum install python-puppetboard

This will pull in al the needed python packages.

