# Contributing

I work hard to provide a high-quality and useful framework, and we greatly value feedback and contributions from our community. Whether it's a new feature, correction, or additional documentation, we welcome your pull requests. Please submit any [issues](https://github.com/osiro/dugite/issues) or [pull requests](https://github.com/osiro/dugite/pulls) through GitHub.

This document contains guidelines for contributing code and filing issues.

## Contributing Code

This list below are guidelines to use when submitting pull requests. These are the same set of guidelines that the core contributors use when submitting changes, and we ask the same of all community contributions as well:

- Dugite is released under the MIT license. Any code you submit will be released under that license.
- All new features must include documentation before they can be merged.

## Feature Development

Any significant feature development for Dugite should have a corresponding github issue for discussion. This gives several benefits:
- Helps avoid wasted work by discussing the proposed changes before significant dev work is started.
- Gives a single place to capture discussion about the rationale for a feature.

This applies to:
- Any feature that proposes modifying the project
- Any new CLI commands

If you'd like to implement a significant feature for Dugite, please file an issue to start the design discussion.

## Development Environment Setup

First, create a virtual environment for Dugite:

```bash
python -m venv .env
source venv/bin/activate
```

Keep in mind that Dugite is designed to work with AWS Lambda, so you should ensure your virtual environment is created with python3.12, python3.11, python3.10 or python3.9, which are the versions of python currently supported by AWS Lambda.

Next, you'll need to install Dugite. The easiest way to configure this is to use:

$ pip install -e .

Run this command in the root directory of the Dugite repo.

Next, you have a few options. There are various requirements files depending on what you'd like to do.

For example, if you'd like to work on Dugite, either fixing bugs or adding new features, install requirements-dev.txt:

```bash
pip install -r requirements-dev.txt
```

## Code Analysis

Dugite uses flake8 for checking pep8 as well as common lint checks. This also helps to cut down on the noise for pull request reviews because many issues are caught locally during development.
