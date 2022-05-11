Getting Started
===============

This page details how to get started with FreeVirgil. 

Installation (Python)
---------------------
Requirements:

* Python3

Install by exectuting:
::

    pip install git+https://github.com/zacc23/freevirgil.git

or

::

    git clone https://github.com/zacc23/freevirgil.git
    cd freevirgil
    pip install .

Installation (C++)
------------------

Requirements:

* `CERN ROOT <https://root.cern/>`_

For getting N spins:
::

    git clone https://github.com/zacc23/OhMyGodWhatHappenedToVirgil.git
    cd OhMyGodWhatHappenedToVirgil
    c++ examples/getN.cpp -I. -Ofast -Wall -Wpedantic -o getN

For plotting:
::

    git clone https://github.com/zacc23/OhMyGodWhatHappenedToVirgil.git
    cd OhMyGodWhatHappenedToVirgil
    c++ examples/plot.cpp -Ofast -I. $(root-config --cflags --libs) -Wall -Wpedantic -o plot 

References
----------

**Gibbs Distribution**

Probability: :math:`P(\alpha) = e^{-E(\alpha)/kT}` with Boltzmann constant, :math:`k = 1.38064852 \times 10^{-23} J/K` and a temperature `T` in Kelvin. This gives the probability of observing :math:`\alpha`, a particular spin.

**Ising Hamiltonian**

Energy: :math:`\displaystyle\hat{H}' = \frac{\hat{H}}{k} = -\frac{J}{k}\sum_{<ij>} s_is_j + \tfrac{\mu}{k}\sum_i s_i`. This gives the energy where :math:`s_i = 1` if the :math:`i^{th}` spin is `up` and :math:`s_i = -1` if it is `down`.

Magnetization: :math:`M(\alpha) = N_{\text{up}}(\alpha) - N_{\text{down}}(\alpha)`. The sum of spins pointing up, minus those pointing down.

**Averages**

:math:`\left<M\right> = \sum_\alpha M(\alpha)P(\alpha)`. The average magnetization, which is found through the sum of each magnetism with its respective probability. 

:math:`\left<E\right> = \sum_\alpha E(\alpha)P(\alpha)`. The average energy, which is found through the sum of each energy with its respective probability.

Examples
--------

**Plot (Python)** 

.. literalinclude:: ../examples/plot.py

.. image:: ../examples/plot.png
  :width: 1000
  :alt: Quantities vs. Temperature

**Plot (C++)**

.. literalinclude:: ../freevirgil-cpp/examples/plot.cpp

.. image:: ../freevirgil-cpp/examples/plot.png
  :width: 1000
  :alt: Quantities vs. Temperature

Speed
-----

Tested by prefacing the execution command with `time` (with 10 sites)

**Python (plot.py)**
::

    0m02.72s real     0m02.61s user     0m00.08s system

**C++ (plot.cpp)**

* Default optimization

::

    0m00.71s real     0m00.58s user     0m00.13s system

* With g++ -Ofast flag

::

    0m00.54s real     0m00.43s user     0m00.12s system
