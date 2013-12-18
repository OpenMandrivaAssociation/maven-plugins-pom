%_javapackages_macros
%global short_name maven-plugins

Name:           %{short_name}-pom
Version:        23
Release:        7.0%{?dist}
Summary:        Maven Plugins POM
BuildArch:      noarch

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/
Source:         http://repo.maven.apache.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip

BuildRequires:  maven-local

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
%setup -q -n %{short_name}-%{version}
# Enforcer plugin is used to ban plexus-component-api.
%pom_remove_plugin :maven-enforcer-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE
