# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import VecReg

def test_VecReg_inputs():
    input_map = dict(affine_mat=dict(argstr='-t %s',
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-i %s',
    mandatory=True,
    ),
    interpolation=dict(argstr='--interp=%s',
    ),
    mask=dict(argstr='-m %s',
    ),
    out_file=dict(argstr='-o %s',
    genfile=True,
    hash_files=False,
    ),
    output_type=dict(),
    ref_mask=dict(argstr='--refmask=%s',
    ),
    ref_vol=dict(argstr='-r %s',
    mandatory=True,
    ),
    rotation_mat=dict(argstr='--rotmat=%s',
    ),
    rotation_warp=dict(argstr='--rotwarp=%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    warp_field=dict(argstr='-w %s',
    ),
    )
    inputs = VecReg.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_VecReg_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = VecReg.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

