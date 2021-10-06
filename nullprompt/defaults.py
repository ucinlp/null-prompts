# NOTE(rloganiv): New functionality is routinely added to some trainers, which
# consequently adds new parameters. If these parameters do not have defaults
# this can break old yaml configs. To avoid this issue, we define defaults
# here.
#
# TODO(rloganiv): In the future it would be nice to restructure the code to use
# something like gin and more modular dataclasses for configuration.
# Unfortunately this would require a lot of refactoring, so for now we'll use
# this simpler but more brittle solution.
DEFAULT_CONFIG = {
    'checklist': None,
    'ckpt_dir': 'ckpt/',
    'label_map': None,
    'initial_trigger': [],
    'label_field': 'label',
    'add_padding': False,
    'preprocessor': None,
    'decoding_strategy': None,
    'linear': False,
    'skip_train': False,
    'skip_eval': False,
    'skip_test': False,
    'randomize_labels': False,
    'randomize_mask': False,
    'reduction_factor': 16,
    'disable_dropout': False,
    'clip': 1.0,
    'limit': None,
    'seed': 1234,
    'l1decay': 0.0,
    'theta': 1e32,
    'force_overwrite': False,
    'quiet': False,
    'tmp': True
}
