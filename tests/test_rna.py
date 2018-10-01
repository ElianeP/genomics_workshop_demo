from genomics_demo.rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')

<<<<<<< HEAD
def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'


=======
def test_mutated_sequence_works():
    #assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == True
    assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == print('The fish is mutated')
    assert RNA('GGGGGGGGGGUGGGGUUGGG')._check_if_mutated == print('The fish is not mutated')


def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'

def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'

>>>>>>> 8ae8dde00c0f7e6165e8232e75863c3faf433371
def test_motifs_works():
    assert RNA('GAUGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA').type_rna() == 'polyA tail mRNA'
    assert RNA('AUCAUCAUCAUCGAGAGUA').type_rna() == 'clover leaf loop tRNA'
    assert RNA('UCAUCAAGUGC').type_rna() == 'microRNA'
    assert RNA('AUCAUCAUCAUCGAGAGUAUCAUCAAGUGC').type_rna() == 'clover leaf loop tRNA'

<<<<<<< HEAD
=======
<<<<<<< HEAD
def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'
    assert RNA('GCCACCUAG').get_aa_sequence() == 'Ala-Thr-Stop'

def test_check_polyA():
    assert RNA('A' * 50).check_polyA()
    assert RNA('A' * 49).check_polyA() is False


def test_reverse_sequence_works():
    assert RNA('GUCA').reverse_sequence == RNA('ACUG')
    assert RNA('ACUG').reverse_sequence == RNA('GUCA')


def test_rna_start_codon():
    assert RNA('AUG').rna_start_codon

>>>>>>> 8ae8dde00c0f7e6165e8232e75863c3faf433371
def test_mutated_sequence_works():
    #assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == True
    assert RNA('GGGGGGGGGGUGGGGGGGGG')._check_if_mutated == print('The fish is mutated')
    assert RNA('GGGGGGGGGGUGGGGUUGGG')._check_if_mutated == print('The fish is not mutated')

<<<<<<< HEAD
=======

def test_check_polyA():
    assert RNA('A'*50)._check_polyA() == 'Sequence contains a poly A tail of 50 adenines'

>>>>>>> 8ae8dde00c0f7e6165e8232e75863c3faf433371
