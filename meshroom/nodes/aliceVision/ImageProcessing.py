__version__ = "1.1"

from meshroom.core import desc


class ImageProcessing(desc.CommandLineNode):
    commandLine = 'aliceVision_utils_imageProcessing {allParams}'
    size = desc.DynamicNodeSize('input')
    # parallelization = desc.Parallelization(blockSize=40)
    # commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file input, image filenames or regex(es) on the image file path.\nsupported regex: \'#\' matches a single digit, \'@\' one or more digits, \'?\' one character and \'*\' zero or more.',
            value='',
            uid=[0],
        ),
        desc.ListAttribute(
            elementDesc=desc.File(
                name="inputFolder",
                label="input Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="inputFolders",
            label="Images input Folders",
            description='Use images from specific folder(s).',
        ),
        desc.ListAttribute(
            elementDesc=desc.StringParam(
                name="metadataFolder",
                label="Metadata Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="metadataFolders",
            label="Metadata input Folders",
            description='Use images metadata from specific folder(s).',
            advanced=True,
        ),
        desc.ChoiceParam(
            name='extension',
            label='Output File Extension',
            description='Output Image File Extension.',
            value='',
            values=['', 'exr', 'jpg', 'tiff', 'png'],
            exclusive=True,
            uid=[0],
        ),
        desc.BoolParam(
            name='reconstructedViewsOnly',
            label='Only Reconstructed Views',
            description='Process Only Reconstructed Views',
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='exposureCompensation',
            label='Exposure Compensation',
            description='Exposure Compensation',
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name='scaleFactor',
            label='ScaleFactor',
            description='Scale Factor.',
            value=1.0,
            range=(0.0, 1.0, 0.01),
            uid=[0],
        ),
        desc.FloatParam(
            name='contrast',
            label='Contrast',
            description='Contrast.',
            value=1.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
        desc.IntParam(
            name='medianFilter',
            label='Median Filter',
            description='Median Filter.',
            value=0,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='fillHoles',
            label='Fill holes',
            description='Fill holes.',
            value=False,
            uid=[0],
        ),
        desc.GroupAttribute(name="sharpenFilter", label="Sharpen Filter", description="Sharpen Filtering Parameters.", joinChar=":", groupDesc=[
            desc.BoolParam(
                name='enabled',
                label='Enable',
                description='Use sharpen.',
                value=False,
                uid=[0],
            ),
            desc.IntParam(
                name='width',
                label='Width',
                description='Sharpen Width.',
                value=3,
                range=(1, 9, 2),
                uid=[0],
            ),
            desc.FloatParam(
                name='contrast',
                label='Contrast',
                description='Sharpen Contrast.',
                value=1.0,
                range=(0.0, 100.0, 0.1),
                uid=[0],
            ),
            desc.FloatParam(
                name='threshold',
                label='Threshold',
                description='Sharpen Threshold.',
                value=0.0,
                range=(0.0, 1.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.GroupAttribute(name="bilateralFilter", label="Bilateral Filter", description="Bilateral Filtering Parameters.", joinChar=":", groupDesc=[
            desc.BoolParam(
                name='bilateralFilterEnabled',
                label='Enable',
                description='Bilateral Filter.',
                value=False,
                uid=[0],
            ),
            desc.IntParam(
                name='bilateralFilterDistance',
                label='Distance',
                description='Diameter of each pixel neighborhood that is used during bilateral filtering.\nCould be very slow for large filters, so it is recommended to use 5.',
                value=0,
                range=(0, 9, 1),
                uid=[0],
            ),
            desc.FloatParam(
                name='bilateralFilterSigmaSpace',
                label='Sigma Coordinate Space',
                description='Bilateral Filter sigma in the coordinate space.',
                value=0.0,
                range=(0.0, 150.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name='bilateralFilterSigmaColor',
                label='Sigma Color Space',
                description='Bilateral Filter sigma in the color space.',
                value=0.0,
                range=(0.0, 150.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.GroupAttribute(name="claheFilter", label="Clahe Filter", description="Clahe Filtering Parameters.", joinChar=":", groupDesc=[
            desc.BoolParam(
                name='claheEnabled',
                label='Enable',
                description='Use Contrast Limited Adaptive Histogram Equalization (CLAHE) Filter.',
                value=False,
                uid=[0],
            ),
            desc.FloatParam(
                name='claheClipLimit',
                label='Clip Limit',
                description='Sets Threshold For Contrast Limiting.',
                value=4.0,
                range=(0.0, 8.0, 1.0),
                uid=[0],
            ),
            desc.IntParam(
                name='claheTileGridSize',
                label='Tile Grid Size',
                description='Sets Size Of Grid For Histogram Equalization. Input Image Will Be Divided Into Equally Sized Rectangular Tiles.',
                value=8,
                range=(4, 64, 4),
                uid=[0],
            ),
        ]),
        desc.GroupAttribute(name="noiseFilter", label="Noise Filter", description="Noise Filtering Parameters.", joinChar=":", groupDesc=[
            desc.BoolParam(
                name='noiseEnabled',
                label='Enable',
                description='Add Noise.',
                value=False,
                uid=[0],
            ),
            desc.ChoiceParam(
                name='noiseMethod',
                label='Method',
                description=" * method: There are several noise types to choose from:\n"
                            " * uniform: adds noise values uninformly distributed on range [A,B).\n"
                            " * gaussian: adds Gaussian (normal distribution) noise values with mean value A and standard deviation B.\n"
                            " * salt: changes to value A a portion of pixels given by B.\n",
                value='uniform',
                values=['uniform', 'gaussian', 'salt'],
                exclusive=True,
                uid=[0],
            ),
            desc.FloatParam(
                name='noiseA',
                label='A',
                description='Parameter that have a different interpretation depending on the method chosen.',
                value=0.0,
                range=(0.0, 1.0, 0.0001),
                uid=[0],
            ),
            desc.FloatParam(
                name='noiseB',
                label='B',
                description='Parameter that have a different interpretation depending on the method chosen.',
                value=1.0,
                range=(0.0, 1.0, 0.0001),
                uid=[0],
            ),
            desc.BoolParam(
                name='noiseMono',
                label='Mono',
                description='If is Checked, a single noise value will be applied to all channels otherwise a separate noise value will be computed for each channel.',
                value=True,
                uid=[0],
            ),
        ]),
        desc.ChoiceParam(
                name='outputFormat',
                label='Output Image Format',
                description='Allows you to choose the format of the output image.',
                value='rgba',
                values=['rgba', 'rgb', 'grayscale'],
                exclusive=True,
                advanced=True,
                uid=[0],
            ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='verbosity level (fatal, error, warning, info, debug, trace).',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        )
    ]

    outputs = [
        desc.File(
            name='outSfMData',
            label='Output sfmData',
            description='Output sfmData.',
            value=desc.Node.internalFolder + 'sfmData.abc',
            group='',  # do not export on the command line
            uid=[],
        ),
        desc.File(
            name='outputFolder',
            label='Output Images Folder',
            description='Output Images Folder.',
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]
