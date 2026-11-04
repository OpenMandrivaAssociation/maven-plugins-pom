%global short_name maven-plugins

Name:           %{short_name}-pom
Version:        50
Release:        1
Summary:        Maven Plugins POM
BuildArch:      noarch
BuildSystem:	maven
BuildOption:	validate

License:        ASL 2.0
URL:            https://maven.apache.org/plugins/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
