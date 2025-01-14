import pytest

from .base import TestBaseClass


class TestClassOelintVarsOverrideAppend(TestBaseClass):

    @pytest.mark.parametrize('id', ['oelint.vars.overrideappend'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:class-target:append = " a"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:class-target:prepend = "a"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:qemux86-64:prepend = "a"
                                     ''',
                                 },
                             ],
                             )
    def test_bad(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)

    @pytest.mark.parametrize('id', ['oelint.vars.overrideappend'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'FILES:${PN}-ptest:append:class-target = " a"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'ALTERNATIVE:${PN}:append = " xxd"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     B:class-target = ""
                                     B:class-target:append = " a"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     B:class-target:qemux86-64 = ""
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     FILES:${PN} = "a"
                                     ''',
                                 },
                             ],
                             )
    def test_good(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)
