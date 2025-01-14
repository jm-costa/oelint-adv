import pytest

from .base import TestBaseClass


class TestClassOelintFileRequireIncludeRelPaths(TestBaseClass):

    @pytest.mark.parametrize('id', ['oelint.file.includerelpath'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'include ../oelint_adv_test.inc',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "../../bb.inc"
                                     include ${A}
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'require ../oelint_adv_test.inc',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "../../bb.inc"
                                     require ${A}
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'require a/../oelint_adv_test.inc',
                                 },
                             ],
                             )
    def test_bad(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)

    @pytest.mark.parametrize('id', ['oelint.file.includerelpath'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'require oelint_adv_test.inc',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'include oelint_adv_test.inc',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'require recipes-kernel/foo/oelint_adv_test.inc',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'include recipes-kernel/foo/oelint_adv_test.inc',
                                 },
                             ],
                             )
    def test_good(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)
