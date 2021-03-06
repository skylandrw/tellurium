

Stochastic simulation
---------------------

Stochastic simulations can be run by changing the current integrator
type to 'gillespie' or by using the ``r.gillespie`` function.

.. code-block:: python

    import tellurium as te
    import numpy as np
    
    r = te.loada('S1 -> S2; k1*S1; k1 = 0.1; S1 = 40')
    r.integrator = 'gillespie'
    r.integrator.seed = 1234
    
    results = []
    for k in range(1, 50):
        r.reset()
        s = r.simulate(0, 40)
        results.append(s)
        r.plot(s, show=False, alpha=0.7)
    te.show()



.. image:: _notebooks/core/tellurium_stochastic_files/tellurium_stochastic_2_0.png


Seed
^^^^

Setting the identical seed for all repeats results in identical traces
in each simulation.

.. code-block:: python

    results = []
    for k in range(1, 20):
        r.reset()
        r.setSeed(123456)
        s = r.simulate(0, 40)
        results.append(s)
        r.plot(s, show=False, loc=None, color='black', alpha=0.7)
    te.show()



.. image:: _notebooks/core/tellurium_stochastic_files/tellurium_stochastic_4_0.png


Combining Simulations
^^^^^^^^^^^^^^^^^^^^^

You can combine two timecourse simulations and change e.g. parameter
values in between each simulation. The ``gillespie`` method simulates up
to the given end time ``10``, after which you can make arbitrary changes
to the model, then simulate again.

When using the ``r.plot`` function, you can pass the parameter
``labels``, which controls the names that will be used in the figure
legend, and ``tag``, which ensures that traces with the same tag will
be drawn with the same color (each species within each trace will be
plotted in its own color, but these colors will match trace to trace).

.. code-block:: python

        import tellurium as te

        r = te.loada('S1 -> S2; k1*S1; k1 = 0.02; S1 = 100')
        r.setSeed(1234)
        for k in range(1, 20):
            r.resetToOrigin()
            res1 = r.gillespie(0, 10)
            r.plot(res1, show=False) # plot first half of data
            
            # change in parameter after the first half of the simulation
            # We could have also used an Event in the antimony model,
            # which are described further in the Antimony Reference section
            r.k1 = r.k1*20
            res2 = r.gillespie (10, 20)
            
            r.plot(res2, show=False) # plot second half of data

        te.show()



.. image:: _notebooks/core/tellurium_stochastic_files/tellurium_stochastic_6_0.png

