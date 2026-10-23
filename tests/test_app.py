import unittest
from app import calculate, index


class TestApp(unittest.TestCase):
    #tests calculate
    def test_expression_vide(self):
        with self.assertRaises(ValueError):
            calculate('')

    def test_expression_non_string(self):
        with self.assertRaises(ValueError):
            calculate(734)

    def test_expression_uniquement_espaces(self):
        with self.assertRaises(ValueError):
            calculate('            ')

    def test_operateur_droite(self):
        with self.assertRaises(ValueError):
            calculate('+23')

    def test_operateur_gauche(self):
        with self.assertRaises(ValueError):
            calculate('23+')

    def test_aucun_operateur(self):
        with self.assertRaises(ValueError):
            calculate('123')

    def test_deux_operateurs(self):
        with self.assertRaises(ValueError):
            calculate('2+-4')

    def test_trois_operateurs(self):
        with self.assertRaises(ValueError):
            calculate('1+++4')

    def test_espace_operateur_nombre(self):
        with self.assertRaises(ValueError):
            calculate(' +4')

    def test_nombre_operateur_espace(self):
        with self.assertRaises(ValueError):
            calculate('2+ ')

    def test_espace_dans_un_nombre(self):
        with self.assertRaises(ValueError):
            calculate('3 3+3')

    def test_uniquement_operateur(self):
        with self.assertRaises(ValueError):
            calculate('+')

    def test_operande_a_pas_float(self):
        with self.assertRaises(ValueError):
            calculate('test/2')

    def test_operande_b_pas_float(self):
        with self.assertRaises(ValueError):
            calculate('100*test')

    def test_operande_a_et_b_pas_float(self):
        with self.assertRaises(ValueError):
            calculate('test-test')

    def test_operande_a_et_b_float(self):
        self.assertEqual(68, calculate('23+45'))

    def test_soustraction_positive(self):
        self.assertEqual(7, calculate('10-3'))

    def test_soustraction_negative(self):
        self.assertEqual(-7, calculate('3-10'))

    def test_addition(self):
        self.assertEqual(16, calculate('8+8'))

    def test_division_entier(self):
        self.assertEqual(5, calculate('10/2'))

    def test_division_float(self):
        self.assertEqual(0.75, calculate('3/4'))

    def test_division_irrationnel(self):
        expect = 1/3
        self.assertEqual(expect, calculate('1/3'))

    def test_multiplication(self):
        self.assertEqual(60, calculate('5*12'))

    def test_float_entree(self):
        with self.assertRaises(ValueError):
            calculate('3.5*5')

    def test_inf(self):
        with self.assertRaises(ValueError):
            calculate('inf+5')

    def test_inf_majuscule(self):
        with self.assertRaises(ValueError):
            calculate('INF+1')

    def test_nan(self):
        with self.assertRaises(ValueError):
            calculate('8*nan')

    def test_ecriture_alternative_operande(self):
        with self.assertRaises(ValueError):
            calculate('1_000 + 40_000')

    def test_notation_scientifique(self):
        self.assertEqual(17, calculate('1e1+7'))

    def test_notation_scientifique_plus(self):
        with self.assertRaises(ValueError):
            calculate('1e+1 + 7')

    def test_division_0(self):
        with self.assertRaises(ValueError):
            calculate('2/0')

    def test_max_float(self):
        with self.assertRaises(ValueError):
            grand_nombre = '9' * 500
            calculate(f"{grand_nombre} + 1")

    def test_None(self):
        with self.assertRaises(ValueError):
            calculate(None)

    def test_None_with_operator(self):
        with self.assertRaises(ValueError):
            calculate('None+2')

    def test_True(self):
        with self.assertRaises(ValueError):
            calculate('True')

    def test_False(self):
        with self.assertRaises(ValueError):
            calculate('False')

    #tests index
    def test_requete_patch(self):
        #should not be able to use this type of request
    
    def test_requete_get(self):
        with self.assertRaises(ValueError):
            index()

    def test_requete_post(self):

    def test_expression_vide(self):

    def test_operandes_pas_chiffres(self):

    def test_expression_pas_string(self):

    def test_expression_aucun_operateur(self):

    def test_expression_deux_operateurs(self):

    def test_expression_operateur_debut(self):

    def test_expression_operateur_fin(self):
