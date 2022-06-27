<img src="https://github.com/fatiando/ensaio/raw/main/doc/_static/readme-banner.png" alt="Ensaio">

<h2 align="center">Practice datasets to probe your code</h2>

<p align="center">
<a href="https://www.fatiando.org/ensaio"><strong>Documentation</strong> (latest)</a> •
<a href="https://www.fatiando.org/ensaio/dev"><strong>Documentation</strong> (main branch)</a> •
<a href="https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md"><strong>Contributing</strong></a> •
<a href="https://www.fatiando.org/contact/"><strong>Contact</strong></a>
</p>

<p align="center">
Part of the <a href="https://www.fatiando.org"><strong>Fatiando a Terra</strong></a> project
</p>

<p align="center">
<a href="https://pypi.python.org/pypi/ensaio"><img src="http://img.shields.io/pypi/v/ensaio.svg?style=flat-square" alt="Latest version on PyPI"></a>
<a href="https://github.com/conda-forge/ensaio-feedstock"><img src="https://img.shields.io/conda/vn/conda-forge/ensaio.svg?style=flat-square" alt="Latest version on conda-forge"></a>
<a href="https://codecov.io/gh/fatiando/ensaio"><img src="https://img.shields.io/codecov/c/github/fatiando/ensaio/main.svg?style=flat-square" alt="Test coverage status"></a>
<a href="https://pypi.python.org/pypi/ensaio"><img src="https://img.shields.io/pypi/pyversions/ensaio.svg?style=flat-square" alt="Compatible Python versions."></a>
<a href="https://doi.org/10.5281/zenodo.5784202"><img src="https://img.shields.io/badge/doi-10.5281%2Fzenodo.5784202-blue?style=flat-square" alt="DOI used to cite Ensaio"></a>
</p>

## About

**Ensaio** (Portuguese for "rehearsal") is a Python package for downloading
open-access sample datasets for Geoscience.
It taps into the
[Fatiando a Terra FAIR data collection](https://github.com/fatiando-data) that
is designed for use in tutorials, documentation, and teaching.

It uses [Pooch](https://www.fatiando.org/pooch) to manage downloading and
caching the data on your computer.
This means that datasets are only downloaded if they can't be found on your
computer already.

## Project goals

* Provide minimal code for downloading our sample data (basically just creates
  the relevant Pooch code).
* Only download and let the user load the data. This helps make tutorials and
  examples more easily extended to a user's own data.
* Be fully backwards compatible. We achieve this by separating **data**
  versions from **Ensaio** versions. Data fetching functions allow you to
  choose any data version that is older than the version of Ensaio that's
  installed. Major releases of Ensaio will be few and far between (if any).

## Project status

**Ensaio is ready for use but still changing.**
This means that we sometimes break backwards compatibility as we try to
improve the software based on user experience, new ideas, better design
decisions, etc. Please keep that in mind before you update to a newer
version.

**We welcome feedback and ideas!** This is a great time to bring new ideas on
how we can improve the project.
[Join the conversation](https://www.fatiando.org/contact) or submit
[issues on GitHub](https://github.com/fatiando/ensaio/issues).

## Getting involved

🗨️ **Contact us:** 
Find out more about how to reach us at 
[fatiando.org/contact](https://www.fatiando.org/contact/).

👩🏾‍💻 **Contributing to project development:** 
Please read our 
[Contributing Guide](https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md) 
to see how you can help and give feedback.

🧑🏾‍🤝‍🧑🏼 **Code of conduct:** 
This project is released with a 
[Code of Conduct](https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md). 
By participating in this project you agree to abide by its terms.

> **Imposter syndrome disclaimer:**
> We want your help. **No, really.** There may be a little voice inside your
> head that is telling you that you're not ready, that you aren't skilled
> enough to contribute. We assure you that the little voice in your head is
> wrong. Most importantly, **there are many valuable ways to contribute besides
> writing code**.
>
> *This disclaimer was adapted from the*
> [MetPy project](https://github.com/Unidata/MetPy).

## License

This is free software: you can redistribute it and/or modify it under the terms
of the **BSD 3-clause License**. A copy of this license is provided in
[`LICENSE.txt`](https://github.com/fatiando/ensaio/blob/main/LICENSE.txt).
