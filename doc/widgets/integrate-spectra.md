Integrate Spectra
=================

Integrate spectra in various ways.

**Inputs**

- Data: input dataset

**Outputs**

- Integrated Data: data with integrals appended
- Preprocessor: preprocessing method

The **Integrate Spectra** widget allows you to add integrals to your data by selecting regions of interest and integrating them with several methods.

![](images/Integrate-Spectra-stamped.png)

1. Add integral:
   - Integral from 0
   - Integral from baseline
   - Peak from 0
   - Peak from baseline
   - Closest value
   - X-value of maximum from 0
   - X-value of maximum from baseline
   - Standard deviation
   - Absolute integral from baseline
   - Integral ratio of two regions
2. Toggle preview.
3. Preview plot with its editor menu like in the [Spectra](spectra.md) widget.
4. Show a subsample of the spectra (implemented for performance).
5. Output integrals as meta attributes. Otherwise only integrals will be output. Commit to send the changes to the output.

Integrate Methods
-------

- **Integral from 0:** The sum of the area under the curve above (+) and below (-) zero. Calculated using the [trapezoidal method](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html).
- **Integral from baseline:** The sum of the area under the curve above (+) and below (-) a straight line between the integral endpoints. Calculated using the trapezoidal method.
- **Integral from separate baseline:** The sum of the area under the curve above (+) and below (-) a baseline defined by a straight line between a separate region. Calculated using the trapezoidal method.
- **Peak from 0:** The highest curve point above zero.
- **Peak from baseline:** The highest curve point from a baseline defined by a straight line between the integral endpoints.
- **Closest value:** The closest 'x' value to the defined region.
- **X-value of maximum from 0:** The 'x' value of the maximum peak from zero.
- **X-value of maximum from baseline:** The 'x' value of the maximum peak from a baseline defined by a straight line between the integral endpoints.
- **Standard deviation:** The standard deviation of the dataset within the given limits. Calculated using the NumPy's [standard deviation](https://numpy.org/doc/2.1/reference/generated/numpy.std.html) setting *ddof=1* to output the standard deviation of a sample dataset.
- **Absolute integral from baseline:** The sum of the area under the curve above (+) and below (+) a straight line between the integral endpoints. Calculated using the trapezoidal method and absolute value curve distance from the baseline.
- **Integral ratio of two regions:** Two 'Integral from baseline' integrals may be defined. The output is the ratio of the numerator integral divided by the denominator integral.

Example
-------

This is a simple example on how to use the **Integrate Spectra** widget. The widget provides many options for integrating spectral areas and the results are appended as additional columns to the data.

We are using the *liver spectroscopy* data set from the **Datasets** widget. In **Integrate Spectra** we have selected *integral from 0* and set the lower and upper limit with the red lines. We could also do it by setting the *Low limit* and *High limit* values on the left.

To observe the integrated area, we need to press the triangular play button next to the method. To output the data, we need to press *Commit*.

Finally, we can observe the additional column with the integral values of the area in a **Data Table**.

![](images/Integrate-Spectra-Example.png)
