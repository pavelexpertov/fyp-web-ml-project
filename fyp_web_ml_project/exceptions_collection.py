# Purpose of this module is to collect all exceptions from other modules
# without making the API interface knowing them.

from .json_form_utils import UnrecognisedTypeError
from .ml_ops import NotFoundMlClassError, NotFoundMlModelError, UntrainedMlModelError, DuplicateMlClassName
from .validator_utils import NotFourKeysError, MissingQueryKeyInJsonError, MissingSettingParameterJsonError
from .ml_class_formation import ClassSyntaxError
