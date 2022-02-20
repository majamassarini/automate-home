%global pypi_name         automate-home

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1%{?dist}
Summary:        A python3 library to automate (home) devices

License:        MIT

Url:            https://github.com/majamassarini/automate-home
Source0:        https://github.com/majamassarini/automate-home/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Yet another home automation (iot) project because
a **smart light is more than just on or off**.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides    python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{python3} -m unittest

%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitelib}/automate_home-%{version}.dist-info/
%{python3_sitelib}/automate_home

%changelog
%autochangelog