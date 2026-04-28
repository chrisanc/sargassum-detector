## **Sargassum detection in Mexican coast using CNN**
This project introduces an automated way to detect the sargassum plague in Mexican coasts, especifically in Chetumal so we are able
to take action on time and reduce the consequences of the plague when it's too late.

To do this, we'll be using the next tools:
* **Sentinel-2 in Copernicus Browser**: Using [Copernicus Browser](https://browser.dataspace.copernicus.eu/), we are able to keep track of
  sargassum from the mexican skies using filters and bands.
* **QGis (software)**: Used to manage and edit the images retrieved from the copernicus browser. Useful when we need to add layers of
  different kind of colors (color ramps).
* **Python**: Using Python libraries **(numpy, torch)** to train *Convolutional Neural Network* for image classification. The goal is to
  end up with a model able to detect sargassum with < 87% accuracy.

> [!NOTE]
> We're testing multiple indices for sargassum detection using bands and wave lengths.

*University of Colima (FIME) and ECOSUR*

*2026*
