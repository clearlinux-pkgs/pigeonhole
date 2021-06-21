#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x18A348AEED409DA1 (dovecot-ce@dovecot.org)
#
Name     : pigeonhole
Version  : 2.3.pigeonhole.0.5.15
Release  : 5
URL      : https://pigeonhole.dovecot.org/releases/2.3/dovecot-2.3-pigeonhole-0.5.15.tar.gz
Source0  : https://pigeonhole.dovecot.org/releases/2.3/dovecot-2.3-pigeonhole-0.5.15.tar.gz
Source1  : https://pigeonhole.dovecot.org/releases/2.3/dovecot-2.3-pigeonhole-0.5.15.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: pigeonhole-bin = %{version}-%{release}
Requires: pigeonhole-lib = %{version}-%{release}
Requires: pigeonhole-libexec = %{version}-%{release}
Requires: pigeonhole-license = %{version}-%{release}
Requires: pigeonhole-man = %{version}-%{release}
BuildRequires : cyrus-sasl-dev
BuildRequires : dovecot-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : valgrind
Patch1: build.patch

%description
Pigeonhole for Dovecot v2.4
Introduction
============
This package is part of the Pigeonhole project (http://pigeonhole.dovecot.org).
It adds support for the Sieve language (RFC 5228) and the ManageSieve protocol
(RFC 5804) to the Dovecot Secure IMAP Server. In the literal sense, a pigeonhole
is a a hole or recess inside a dovecot for pigeons to nest in. It is, however,
also the name for one of a series of small, open compartments in a cabinet used
for filing or sorting mail. As a verb, it describes the act of putting an item
into one of those pigeonholes. The name `Pigeonhole' therefore well describes an
important part of the functionality that this project adds to Dovecot: sorting
and filing e-mail messages.

%package bin
Summary: bin components for the pigeonhole package.
Group: Binaries
Requires: pigeonhole-libexec = %{version}-%{release}
Requires: pigeonhole-license = %{version}-%{release}

%description bin
bin components for the pigeonhole package.


%package dev
Summary: dev components for the pigeonhole package.
Group: Development
Requires: pigeonhole-lib = %{version}-%{release}
Requires: pigeonhole-bin = %{version}-%{release}
Provides: pigeonhole-devel = %{version}-%{release}
Requires: pigeonhole = %{version}-%{release}

%description dev
dev components for the pigeonhole package.


%package doc
Summary: doc components for the pigeonhole package.
Group: Documentation
Requires: pigeonhole-man = %{version}-%{release}

%description doc
doc components for the pigeonhole package.


%package lib
Summary: lib components for the pigeonhole package.
Group: Libraries
Requires: pigeonhole-libexec = %{version}-%{release}
Requires: pigeonhole-license = %{version}-%{release}

%description lib
lib components for the pigeonhole package.


%package libexec
Summary: libexec components for the pigeonhole package.
Group: Default
Requires: pigeonhole-license = %{version}-%{release}

%description libexec
libexec components for the pigeonhole package.


%package license
Summary: license components for the pigeonhole package.
Group: Default

%description license
license components for the pigeonhole package.


%package man
Summary: man components for the pigeonhole package.
Group: Default

%description man
man components for the pigeonhole package.


%prep
%setup -q -n dovecot-2.3-pigeonhole-0.5.15
cd %{_builddir}/dovecot-2.3-pigeonhole-0.5.15
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624294588
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-dovecot=/usr/lib64/dovecot \
--with-ldap=yes \
--with-moduledir=/usr/lib64/dovecot
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1624294588
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pigeonhole
cp %{_builddir}/dovecot-2.3-pigeonhole-0.5.15/COPYING %{buildroot}/usr/share/package-licenses/pigeonhole/e54ccad100241cf089ed3934f148d2ac2db470fd
cp %{_builddir}/dovecot-2.3-pigeonhole-0.5.15/COPYING.LGPL %{buildroot}/usr/share/package-licenses/pigeonhole/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sieve-dump
/usr/bin/sieve-filter
/usr/bin/sieve-test
/usr/bin/sievec

%files dev
%defattr(-,root,root,-)
/usr/include/dovecot/sieve/edit-mail.h
/usr/include/dovecot/sieve/mail-raw.h
/usr/include/dovecot/sieve/pigeonhole-config.h
/usr/include/dovecot/sieve/pigeonhole-version.h
/usr/include/dovecot/sieve/rfc2822.h
/usr/include/dovecot/sieve/sieve-actions.h
/usr/include/dovecot/sieve/sieve-address-parts.h
/usr/include/dovecot/sieve/sieve-address-source.h
/usr/include/dovecot/sieve/sieve-address.h
/usr/include/dovecot/sieve/sieve-ast.h
/usr/include/dovecot/sieve/sieve-binary-dumper.h
/usr/include/dovecot/sieve/sieve-binary-private.h
/usr/include/dovecot/sieve/sieve-binary.h
/usr/include/dovecot/sieve/sieve-code-dumper.h
/usr/include/dovecot/sieve/sieve-code.h
/usr/include/dovecot/sieve/sieve-commands.h
/usr/include/dovecot/sieve/sieve-common.h
/usr/include/dovecot/sieve/sieve-comparators.h
/usr/include/dovecot/sieve/sieve-config.h
/usr/include/dovecot/sieve/sieve-dump.h
/usr/include/dovecot/sieve/sieve-error-private.h
/usr/include/dovecot/sieve/sieve-error.h
/usr/include/dovecot/sieve/sieve-execute.h
/usr/include/dovecot/sieve/sieve-ext-copy.h
/usr/include/dovecot/sieve/sieve-ext-enotify.h
/usr/include/dovecot/sieve/sieve-ext-environment.h
/usr/include/dovecot/sieve/sieve-ext-imap4flags.h
/usr/include/dovecot/sieve/sieve-ext-mailbox.h
/usr/include/dovecot/sieve/sieve-ext-variables.h
/usr/include/dovecot/sieve/sieve-extensions.h
/usr/include/dovecot/sieve/sieve-generator.h
/usr/include/dovecot/sieve/sieve-interpreter.h
/usr/include/dovecot/sieve/sieve-lexer.h
/usr/include/dovecot/sieve/sieve-limits.h
/usr/include/dovecot/sieve/sieve-match-types.h
/usr/include/dovecot/sieve/sieve-match.h
/usr/include/dovecot/sieve/sieve-message.h
/usr/include/dovecot/sieve/sieve-objects.h
/usr/include/dovecot/sieve/sieve-parser.h
/usr/include/dovecot/sieve/sieve-plugins.h
/usr/include/dovecot/sieve/sieve-result.h
/usr/include/dovecot/sieve/sieve-runtime-trace.h
/usr/include/dovecot/sieve/sieve-runtime.h
/usr/include/dovecot/sieve/sieve-script-private.h
/usr/include/dovecot/sieve/sieve-script.h
/usr/include/dovecot/sieve/sieve-settings.h
/usr/include/dovecot/sieve/sieve-smtp.h
/usr/include/dovecot/sieve/sieve-storage-private.h
/usr/include/dovecot/sieve/sieve-storage.h
/usr/include/dovecot/sieve/sieve-stringlist.h
/usr/include/dovecot/sieve/sieve-types.h
/usr/include/dovecot/sieve/sieve-validator.h
/usr/include/dovecot/sieve/sieve.h
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/dovecot/example-config/conf.d/20-managesieve.conf
/usr/share/doc/dovecot/example-config/conf.d/90-sieve-extprograms.conf
/usr/share/doc/dovecot/example-config/conf.d/90-sieve.conf
/usr/share/doc/dovecot/example-config/sieve-ldap.conf
/usr/share/doc/dovecot/sieve/extensions/duplicate.txt
/usr/share/doc/dovecot/sieve/extensions/editheader.txt
/usr/share/doc/dovecot/sieve/extensions/include.txt
/usr/share/doc/dovecot/sieve/extensions/spamtest-virustest.txt
/usr/share/doc/dovecot/sieve/extensions/vacation.txt
/usr/share/doc/dovecot/sieve/extensions/vnd.dovecot.environment.txt
/usr/share/doc/dovecot/sieve/extensions/vnd.dovecot.report.txt
/usr/share/doc/dovecot/sieve/locations/dict.txt
/usr/share/doc/dovecot/sieve/locations/file.txt
/usr/share/doc/dovecot/sieve/locations/ldap.txt
/usr/share/doc/dovecot/sieve/plugins/imap_filter_sieve.txt
/usr/share/doc/dovecot/sieve/plugins/imapsieve.txt
/usr/share/doc/dovecot/sieve/plugins/sieve_extprograms.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/dovecot/doveadm/lib10_doveadm_sieve_plugin.so
/usr/lib64/dovecot/lib90_sieve_plugin.so
/usr/lib64/dovecot/lib95_imap_filter_sieve_plugin.so
/usr/lib64/dovecot/lib95_imap_sieve_plugin.so
/usr/lib64/dovecot/libdovecot-sieve.so
/usr/lib64/dovecot/libdovecot-sieve.so.0
/usr/lib64/dovecot/libdovecot-sieve.so.0.0.0
/usr/lib64/dovecot/settings/libmanagesieve_login_settings.so
/usr/lib64/dovecot/settings/libmanagesieve_settings.so
/usr/lib64/dovecot/settings/libpigeonhole_settings.so
/usr/lib64/dovecot/sieve/lib90_sieve_extprograms_plugin.so
/usr/lib64/dovecot/sieve/lib90_sieve_imapsieve_plugin.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dovecot/managesieve
/usr/libexec/dovecot/managesieve-login

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pigeonhole/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/pigeonhole/e54ccad100241cf089ed3934f148d2ac2db470fd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/doveadm-sieve.1
/usr/share/man/man1/sieve-dump.1
/usr/share/man/man1/sieve-filter.1
/usr/share/man/man1/sieve-test.1
/usr/share/man/man1/sievec.1
/usr/share/man/man1/sieved.1
/usr/share/man/man7/pigeonhole.7
