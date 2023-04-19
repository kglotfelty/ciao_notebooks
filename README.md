# CIAO Notebooks

This is a collection of [CIAO](http://cxc.cfa.harvard.edu/ciao) notebooks
that I've written.

These are not offical products of the CXC, Chandra, or any of the other
various affiliations you might want to consider.  All opinions are my own.

Use at your own risk.  Most won't work with current version of CIAO without
modifications, but should give you some ideas about what is possible.

- `DitherEffectOnSpatialResolution.ipynb` (now part of the CIAO documentation).  Discusses how spacecraft dither limits subpixel resolution.
- `E_Model_Example.ipynb` and example of a reconstruction using my [`emodel` script](https://github.com/kglotfelty/ellipse_model)
- `Expansion.ipynb` shows how to manipulate WCS and reproject datasets to simulate expansion of an extended source.
- `FAP_Example.ipynb` uses Frank Primini's next generation aperature photometry
- `Future_Arf_6676.ipynb` shows how to modify `ardlib` parameters to generate an ARF for a future observation (off axis in this case).
- `PSF_Contamination.ipynb` shows how to identify and begin to quantify amount of PSF contamination in radial profile bins.
- `PrettyPictureProcessingSteps.ipynb` creating fluxed tricolor images
- `SourceInChipGap.ipynb` (now part of the CIAO docs), analysis of a source in chip gap
- `WhyEarlyData.ipynb` presents an argument for processing early data
- `bias_repair_bad_idea.ipynb` many interesting analysis techniques are shown to understand why pixels were not longer considered bad after bias "repair"
- `dmimgadapt_expmap_separately.ipynb` why  you should not smooth fluxed images (smooth counts and exposure separately)
- `reproject_aspect_and_merge.ipynb` an example of reproject_aspect to improve alignment between observations.
- `Deblend Experiment.ipynb` shows how to randomly assign individual events from overlapping sources to a specific source. 
- `commanded_dither_parameters.ipynb` how to estimate dither parameters from Chandra engineering data.

