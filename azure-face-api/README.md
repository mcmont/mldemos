# Azure Face API demo
**Dr. Chris Empson, Infinity Works Ltd.**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

Twitter: [@monty_mcmont](https://twitter.com/monty_mcmont)

## Overview
This demo visualises the feature information returned by Microsoft Azure's Face API.

The application will download the image and display it in a window. When the window appears press any key to query the Azure Face API. (You may need to click on the window to focus it first.) The facial features will be overlaid on top of the image.

## Running the demo
You will need python3 and the pillow image processing library installed to run this demo.

```pip3 install pillow```

You will also need an Azure account, and you'll need a Microsoft Cognitive Services API key. The key should be added to your environment as a variable called `AZURE_COGNITIVE_SERVICES_API_KEY`:

```export AZURE_COGNITIVE_SERVICES_API_KEY=your-api-key```

This demo requires an image URL as an argument, for example:

```python3 demo.py http://example.com/image.jpg```

## References, useful links and whatnot
[Azure Face API documentation](https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236)
