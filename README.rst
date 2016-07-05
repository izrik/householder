householder
===========

A versioned packaging system for python

    Then said he unto them, Therefore every scribe which is instructed unto the kingdom of heaven is like unto a man that is an **householder**, which bringeth forth out of his treasure things **new** and **old**.

    --*Matthew 13:52*

====

``householder`` is a packaging system that lets you import a specific version of a module. In addition, multiple versions of the same module can be loaded simultaneously.

Simply tweak the way you import modules::

.. code-block:: python
    :linenos:
    import householder
    requests1 = householder.import('requests', version='1.0')
    requests2 = householder.import('requests', version='2.0')

    requests1.get('http://google.com')
    requests2.get('http://google.com')



quote break::

    import householder
    requests1 = householder.import('requests', version='1.0')
    requests2 = householder.import('requests', version='2.0')

    requests1.get('http://google.com')
    requests2.get('http://google.com')
