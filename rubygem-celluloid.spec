%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from celluloid-0.15.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name celluloid

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.15.2
Release: 4%{?dist}
Summary: Actor-based concurrent object framework for Ruby
Group: Development/Languages
License: MIT
URL: https://github.com/celluloid/celluloid
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(timers) >= 1.1.0
Requires: %{?scl_prefix}rubygem(timers) < 1.2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ror}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(timers)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Celluloid enables people to build concurrent programs out of concurrent
objects just as easily as they build sequential programs out of sequential
objects.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite

%check
pushd .%{gem_instdir}

# Disable code coverrage.
sed -i '/overalls/ s/^/#/' spec/spec_helper.rb

# Get rid of Bundler.
sed -i '/bundler/ s/^/#/' spec/spec_helper.rb

# Test suite expect log directory to exist.
mkdir log

%{?scl:scl enable %{scl} - << \EOF}
rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
# License file is going to be included in next version, keep README.md in main
# package until that.
# https://github.com/celluloid/celluloid/commit/e66bff2cfa8a6a7ab8efd03ef3f70f3008ecb3d6
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
# Needed by lib/rspec.
%{gem_instdir}/spec/support

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%exclude %{gem_instdir}/spec/support

%changelog
* Thu Nov 27 2014 Josef Stribny <jstribny@redhat.com> - 0.15.2-4
- Fix typo in requires

* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 0.15.2-3
- Add SCL macros

* Mon Sep 01 2014 Vít Ondruch <vondruch@redhat.com> - 0.15.2-2
- spec/support is needed by runtime.

* Thu Aug 28 2014 Vít Ondruch <vondruch@redhat.com> - 0.15.2-1
- Initial package
