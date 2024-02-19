# CI

## cloud.terraform_ops Collection

GitHub Actions are used to run the Continuous Integration for redhat-cop/cloud.terraform_ops collection. The workflows used for the CI can be found [here](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/.github/workflows). These workflows include jobs to run the sanity tests, linters and changelog check. The following table lists the Python and Ansible versions against which these jobs are run.

| Jobs | Description | Python Versions | Ansible Versions |
| ------ |-------| ------ | -----------|
| Changelog |Checks for the presence of Changelog fragments | 3.9 | devel |
| Linters | Runs `ansible-lint`, `black` and `flake8`| 3.9 and 3.11 for ansible-lint | devel |
| Sanity | Runs Ansible sanity checks | 3.9, 3.10, 3.11, 3.12 | 2.14 (not on 3.12), 2.15 (not on 3.12), 2.16 (not on 3.9), stable (not on 3.9), devel (not on 3.9) |
| Integration | Executes the integration test suites | 3.11 | milestone |
