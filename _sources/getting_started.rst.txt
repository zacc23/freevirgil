Getting Started
===============

This page details how to get started with FreeVirgil. 

Installation
------------
Requirements:

* **Python3**

Install by exectuting:
::

    pip install git+https://github.com/zacc23/freevirgil.git

or

::

    git clone https://github.com/zacc23/freevirgil.git
    cd freevirgil
    pip install .

References
----------

**Gibbs Distribution**

:math:`P(\alpha) = e^{-E(\alpha)/kT}` with Boltzmann constant, :math:`k = 1.38064852 \times 10^{-23} J/K` and a temperature `T` in Kelvin. This gives the probability of observing :math:`\alpha`, a particular spin.

**Ising Hamiltonian**

Energy: :math:`\displaystyle\hat{H}' = \frac{\hat{H}}{k} = -\frac{J}{k}\sum_{<ij>} s_is_j + \tfrac{\mu}{k}\sum_i s_i`. This gives the energy where :math:`s_i = 1` if the :math:`i^{th}` spin is `up` and :math:`s_i = -1` if it is `down`.

Magnetization: :math:`M(\alpha) = N_{\text{up}}(\alpha) - N_{\text{down}}(\alpha)`. The sum of spins pointing up, minus those pointing down.

**Averages**

:math:`\left<M\right> = \sum_\alpha M(\alpha)P(\alpha)`. The average magnetization, which is found through the sum of each magnetism with its respective probability. 

:math:`\left<E\right> = \sum_\alpha E(\alpha)P(\alpha)`. The average energy, which is found through the sum of each energy with its respective probability.

Examples
--------

**Plot** 

.. literalinclude:: ../examples/plot.py

.. image:: ../examples/plot.png
  :width: 400
  :alt: Quantities vs. Temperature
