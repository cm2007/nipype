# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.registration.specialized import FiducialRegistration

def test_FiducialRegistration_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fixedLandmarks=dict(argstr='--fixedLandmarks %s...',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    movingLandmarks=dict(argstr='--movingLandmarks %s...',
    ),
    outputMessage=dict(argstr='--outputMessage %s',
    ),
    rms=dict(argstr='--rms %f',
    ),
    saveTransform=dict(argstr='--saveTransform %s',
    hash_files=False,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    transformType=dict(argstr='--transformType %s',
    ),
    )
    inputs = FiducialRegistration.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_FiducialRegistration_outputs():
    output_map = dict(saveTransform=dict(),
    )
    outputs = FiducialRegistration.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

