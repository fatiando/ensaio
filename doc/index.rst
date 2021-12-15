.. title:: Home

.. raw:: html

    <h1 class="display-2 text-center">
      Ensaio
    </h1>

.. raw:: html

    <p class="lead centered front-page-callout">
        Practice datasets to probe your code
    </p>


Ensaio (Portuguese for "rehearsal") is a Python package for downloading
open-access sample datasets for Geoscience.
It taps into the curated collection from `fatiando/data
<https://github.com/fatiando/data>`__ that is designed for use in tutorials,
documentation, and teaching.

Our code uses `Pooch <https://www.fatiando.org/pooch>`__ to manage downloading
and caching the data on your computer.
This means that datasets are only downloaded if they can't be found on your
computer already.

.. panels::
    :header: text-center text-large
    :card: border-1 m-1 text-center

    **Getting started**
    ^^^^^^^^^^^^^^^^^^^

    New to Ensaio? Start here!

    .. link-button:: install
        :type: ref
        :text: Installing
        :classes: btn-outline-primary btn-block stretched-link

    ---

    **Browse our datasets**
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Take a look at what's available

    .. link-button:: gallery_v1
        :type: ref
        :text: Gallery
        :classes: btn-outline-primary btn-block stretched-link

    ---

    **Need help?**
    ^^^^^^^^^^^^^^

    Get in touch with the Fatiando team

    .. link-button:: https://www.fatiando.org/contact
        :type: url
        :text: Join our Slack
        :classes: btn-outline-primary btn-block stretched-link

    ---

    **Reference documentation**
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    A list of modules and functions

    .. link-button:: api
        :type: ref
        :text: API reference
        :classes: btn-outline-primary btn-block stretched-link

.. seealso::

    Ensaio is a part of the
    `Fatiando a Terra <https://www.fatiando.org/>`_ project.


----


Table of contents
-----------------

.. toctree::
    :caption: User Guide
    :maxdepth: 1

    install.rst
    gallery/v1/index.rst

.. toctree::
    :caption: Reference
    :maxdepth: 1

    api/index.rst
    compatibility.rst
    changes.rst
    versions.rst

.. toctree::
    :caption: Community

    Join the community <https://www.fatiando.org/contact/>
    Code of Conduct <https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md>
    How to contribute <https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md>
    Source code on GitHub <https://github.com/fatiando/ensaio>
    Authors <https://github.com/fatiando/ensaio/blob/main/AUTHORS.md>
    Fatiando a Terra <https://www.fatiando.org>
