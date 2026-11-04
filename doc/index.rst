.. title:: Home

Ensaio
======

.. div:: sd-fs-3

    Practice datasets to probe your code

.. figure:: _static/banner.png

**Ensaio** (Portuguese for "rehearsal") is a Python package for downloading
open-access sample datasets for Geoscience.
It taps into the `Fatiando a Terra FAIR data collection
<https://github.com/fatiando-data>`__ that is designed for use in tutorials,
documentation, and teaching.

It uses `Pooch <https://www.fatiando.org/pooch>`__ to manage downloading and
caching the data on your computer.
This means that datasets are only downloaded if they can't be found on your
computer already.

.. seealso::

    Ensaio is a part of the
    `Fatiando a Terra <https://www.fatiando.org/>`_ project.


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

Project status
--------------

**Ensaio is ready for use but still changing.** This means that we
sometimes break backwards compatibility as we try to improve the
software based on user experience, new ideas, better design decisions,
etc. Please keep that in mind before you update to a newer version.

**We welcome feedback and ideas!** This is a great time to bring new
ideas on how we can improve the project. `Join the
conversation <https://www.fatiando.org/contact>`__ or submit `issues on
GitHub <https://github.com/fatiando/ensaio/issues>`__.

Getting involved
----------------

🗨️ **Contact us:** Find out more about how to reach us at
`fatiando.org/contact <https://www.fatiando.org/contact/>`__.

👩🏾‍💻 **Contributing to project development:** Please read our
`Contributing
Guide <https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md>`__
to see how you can help and give feedback.

🤖 **Policy on AI usage:** Please read our `AI Usage
Policy <https://github.com/fatiando/community/blob/main/AI.md>`__.

🧑🏾‍🤝‍🧑🏼 **Code of conduct:** This project is released with a `Code of
Conduct <https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md>`__.
By participating in this project you agree to abide by its terms.

    **Imposter syndrome disclaimer:** We want your help. **No, really.** There
    may be a little voice inside your head that is telling you that you’re
    not ready, that you aren’t skilled enough to contribute. We assure you
    that the little voice in your head is wrong. Most importantly, **there are
    many valuable ways to contribute besides writing code** (giving feedback,
    teaching, writing documentation, and more).

    *This disclaimer was adapted from the* `MetPy
    project <https://github.com/Unidata/MetPy>`__.

License
-------

This is free software: you can redistribute it and/or modify it under
the terms of the **BSD 3-clause License**. A copy of this license is
provided in
`LICENSE.txt <https://github.com/fatiando/ensaio/blob/main/LICENSE.txt>`__.

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
    citing.rst
    compatibility.rst
    changes.rst
    versions.rst

.. toctree::
    :caption: Community
    :hidden:

    Join our community <https://www.fatiando.org/contact/>
    How to contribute <https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md>
    Code of Conduct <https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md>
    Authors <https://github.com/fatiando/ensaio/blob/main/AUTHORS.md>
    The Fatiando a Terra project <https://www.fatiando.org>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Code and packages

    GitHub <https://github.com/fatiando/ensaio>
    PyPI <https://pypi.python.org/pypi/ensaio>
    conda-forge <https://github.com/conda-forge/ensaio-feedstock>
    Zenodo <https://doi.org/10.5281/zenodo.5784202>
