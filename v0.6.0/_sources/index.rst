.. title:: Home

.. raw:: html

    <img class="mx-auto d-block dark-light" src="./_static/ensaio-logo.svg" width="100">
    <h1 class="display-1 text-center">Ensaio</h1>
    <p class="text-center lead front-page-callout">
      Practice datasets to probe your code
    </p>
    <img class="front-page-banner" src="_static/banner.png" alt="A sampling of our datasets">

**Ensaio** (Portuguese for "rehearsal") is a Python package for downloading
open-access sample datasets for Geoscience.
It taps into the `Fatiando a Terra FAIR data collection
<https://github.com/fatiando-data>`__ that is designed for use in tutorials,
documentation, and teaching.

It uses `Pooch <https://www.fatiando.org/pooch>`__ to manage downloading and
caching the data on your computer.
This means that datasets are only downloaded if they can't be found on your
computer already.

.. grid:: 1 2 1 2
    :margin: 5 5 0 0
    :padding: 0 0 0 0
    :gutter: 4

    .. grid-item-card:: :octicon:`info` Getting started
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        New to Ensaio? Start here!

        .. button-ref:: using
            :ref-type: ref
            :click-parent:
            :color: primary
            :outline:
            :expand:

    .. grid-item-card:: :octicon:`paintbrush` Browse our datasets
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        Take a look at what's available

        .. button-ref:: gallery
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

    .. grid-item-card:: :octicon:`comment-discussion` Need help?
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        Ask on our community channels.

        .. button-link:: https://www.fatiando.org/contact
            :click-parent:
            :color: primary
            :outline:
            :expand:

            Join the conversation :octicon:`link-external`

    .. grid-item-card:: :octicon:`file-badge` Reference documentation
        :text-align: center
        :class-title: sd-fs-5
        :class-card: sd-p-3

        A list of modules and functions.

        .. button-ref:: api
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

----

.. seealso::

    Ensaio is a part of the
    `Fatiando a Terra <https://www.fatiando.org/>`_ project.


.. toctree::
    :caption: User Guide
    :hidden:
    :maxdepth: 1

    install.rst
    tutorial/using.rst
    tutorial/developers.rst
    gallery/index.rst

.. toctree::
    :caption: Reference
    :hidden:
    :maxdepth: 1

    api/index.rst
    compatibility.rst
    changes.rst
    versions.rst

.. toctree::
    :caption: Community
    :hidden:

    Join the community <https://www.fatiando.org/contact/>
    Code of Conduct <https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md>
    How to contribute <https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md>
    Source code on GitHub <https://github.com/fatiando/ensaio>
    Authors <https://github.com/fatiando/ensaio/blob/main/AUTHORS.md>
    Fatiando a Terra <https://www.fatiando.org>
