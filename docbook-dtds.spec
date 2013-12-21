Name: docbook-dtds
Version: 1.0
Release: 63.0%{?dist}

Summary: SGML and XML document type definitions for DocBook

License: Copyright only
URL: http://www.oasis-open.org/docbook/

Requires:	docbook-dtd-mathml20
Requires:	docbook-dtd30-sgml
Requires:	docbook-dtd31-sgml
Requires:	docbook-dtd41-sgml
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-sgml
Requires:	docbook-dtd42-xml
Requires:	docbook-dtd43-xml
Requires:	docbook-dtd44-xml
Requires:	docbook-dtd45-xml
Requires:	docbook-dtds
Requires:	docbook-style-dsssl
Requires:	docbook-style-dsssl-doc
Requires:	docbook-style-xsl
Requires:	docbook-style-xsl-ns
Requires:	docbook-to-man
Requires:	docbook-utils
Requires:	docbook-utils-pdf
Requires:	docbook2x

Requires:	sgml-common
Requires:	xml-common

BuildArch:	noarch

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.


%prep

%build

%install

%files
